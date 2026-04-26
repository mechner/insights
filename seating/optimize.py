#!/usr/bin/env python3
"""Seating schedule optimizer. Stochastic search + local search."""

import csv
import itertools
import random
import math
from collections import defaultdict

random.seed(42)

# --- Data Loading ---

# Cluster definitions: name -> {size, home_neighborhoods: {neighborhood: seat_demand}}
# Most clusters map 1:1 to a neighborhood group. Pragma splits across MechCoop and Scarpati.
CLUSTER_INFO = {}

with open('people.csv', encoding='latin-1') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get('Include H/C', '').strip() != 'Y':
            continue
        c1 = row.get('Cluster 1', '').strip()
        if not c1:
            continue
        group = row.get('Group', '').strip()
        if c1 not in CLUSTER_INFO:
            CLUSTER_INFO[c1] = {'size': 0, 'group': group}
        CLUSTER_INFO[c1]['size'] += 1

CLUSTERS = list(sorted(CLUSTER_INFO.keys()))
CLUSTER_SIZES = {c: CLUSTER_INFO[c]['size'] for c in CLUSTERS}

# Neighborhood seats (MechCoop = Cooper + Mechner)
NEIGHBORHOOD_SEATS = {}
with open('neighborhoods.csv', encoding='latin-1') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['ExCo-1'].strip()
        if name == 'Grand Total':
            continue
        seats = int(row['Seats per Neighborhood'].strip())
        NEIGHBORHOOD_SEATS[name] = seats

# Combine Cooper + Mechner -> MechCoop
NEIGHBORHOOD_SEATS['MechCoop'] = NEIGHBORHOOD_SEATS.pop('Cooper', 0) + NEIGHBORHOOD_SEATS.pop('Mechner', 0)
# Remove Quan (1 seat, not relevant)
NEIGHBORHOOD_SEATS.pop('Quan', None)

# Map clusters to home neighborhoods for seat demand
# Pragma: 48 in MechCoop, 6 in Scarpati (Pragma-Infra)
CLUSTER_NEIGHBORHOOD_DEMAND = {}
for c in CLUSTERS:
    group = CLUSTER_INFO[c]['group']
    if c == 'Pragma':
        CLUSTER_NEIGHBORHOOD_DEMAND[c] = {'MechCoop': 48, 'Scarpati': 6}
    else:
        CLUSTER_NEIGHBORHOOD_DEMAND[c] = {group: CLUSTER_SIZES[c]}

# Affinities
AFFINITIES = []
with open('affinities.csv', encoding='latin-1') as f:
    reader = csv.DictReader(f)
    for row in reader:
        a = row['Cluster_A'].strip()
        b = row['Cluster_B'].strip()
        penalty = float(row['SplitPenalty'].strip())
        AFFINITIES.append((a, b, penalty))

# --- Schedule representation ---
DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
# All C(5,3) = 10 possible 3-day schedules
ALL_SCHEDULES = list(itertools.combinations(range(5), 3))
TOTAL_SEATS = 185

# Day preference penalties (per person-day)
DAY_PENALTY = {0: 0.3, 1: 0.0, 2: 0.0, 3: 0.0, 4: 1.0}  # Mon=0.3, Fri=1.0

def evaluate(assignment):
    """
    assignment: dict cluster_name -> schedule_index (into ALL_SCHEDULES)
    Returns (utility, details_dict). Higher utility = better.
    """
    schedules = {c: ALL_SCHEDULES[assignment[c]] for c in CLUSTERS}

    # 1. Check capacity constraint
    daily_counts = [0] * 5
    for c in CLUSTERS:
        for d in schedules[c]:
            daily_counts[d] += CLUSTER_SIZES[c]
    for d in range(5):
        if daily_counts[d] > TOTAL_SEATS:
            return -1e9, {'violation': f'{DAYS[d]}: {daily_counts[d]} > {TOTAL_SEATS}'}

    # 2. Day preference penalty
    day_penalty_total = 0.0
    cluster_day_penalties = {}
    for c in CLUSTERS:
        cp = sum(DAY_PENALTY[d] for d in schedules[c]) * CLUSTER_SIZES[c]
        cluster_day_penalties[c] = cp
        day_penalty_total += cp

    # 3. Affinity penalty (per person-day of the smaller cluster, for days not overlapping)
    affinity_penalty_total = 0.0
    affinity_details = []
    for a, b, weight in AFFINITIES:
        if a not in schedules or b not in schedules:
            continue
        overlap = len(set(schedules[a]) & set(schedules[b]))
        non_overlap = 3 - overlap
        smaller_size = min(CLUSTER_SIZES[a], CLUSTER_SIZES[b])
        penalty = weight * non_overlap * smaller_size
        affinity_penalty_total += penalty
        affinity_details.append((a, b, overlap, weight, penalty))

    # 4. Fairness: variance in per-person undesirable-day burden
    burdens = []
    for c in CLUSTERS:
        per_person = sum(DAY_PENALTY[d] for d in schedules[c])
        burdens.append(per_person)
    mean_burden = sum(burdens) / len(burdens)
    variance = sum((b - mean_burden) ** 2 for b in burdens) / len(burdens)
    # Penalty scales with total headcount to make it comparable
    fairness_penalty = variance * sum(CLUSTER_SIZES.values()) * 2.0

    total_penalty = day_penalty_total + affinity_penalty_total + fairness_penalty
    utility = -total_penalty

    details = {
        'schedules': schedules,
        'daily_counts': daily_counts,
        'day_penalty': day_penalty_total,
        'affinity_penalty': affinity_penalty_total,
        'fairness_penalty': fairness_penalty,
        'cluster_day_penalties': cluster_day_penalties,
        'affinity_details': affinity_details,
        'total_penalty': total_penalty,
    }
    return utility, details


def random_feasible():
    """Generate a random feasible assignment."""
    for _ in range(10000):
        assignment = {c: random.randint(0, 9) for c in CLUSTERS}
        u, d = evaluate(assignment)
        if u > -1e8:
            return assignment
    return None


def local_search(assignment, max_iters=50000):
    """Hill-climbing: try changing one cluster's schedule at a time."""
    best_u, best_d = evaluate(assignment)
    best_assignment = dict(assignment)
    no_improve = 0
    for i in range(max_iters):
        c = random.choice(CLUSTERS)
        old = assignment[c]
        new = random.randint(0, 9)
        if new == old:
            continue
        assignment[c] = new
        u, d = evaluate(assignment)
        if u > best_u:
            best_u = u
            best_d = d
            best_assignment = dict(assignment)
            no_improve = 0
        else:
            assignment[c] = old
            no_improve += 1
        if no_improve > 5000:
            break
    return best_assignment, best_u, best_d


def optimize(restarts=200, local_iters=50000):
    """Multi-restart stochastic local search."""
    best_assignment = None
    best_u = -1e18
    best_d = None
    for r in range(restarts):
        a = random_feasible()
        if a is None:
            continue
        a, u, d = local_search(a, local_iters)
        if u > best_u:
            best_u = u
            best_d = d
            best_assignment = dict(a)
            if r % 20 == 0:
                print(f'  Restart {r}: new best utility = {best_u:.2f}')
    return best_assignment, best_u, best_d


def format_results(assignment, utility, details):
    """Generate schedule.md content."""
    schedules = details['schedules']
    daily_counts = details['daily_counts']
    lines = []
    lines.append('# Seating Schedule')
    lines.append('')
    lines.append(f'Total utility: {utility:.2f} (day penalty: {details["day_penalty"]:.1f}, '
                 f'affinity penalty: {details["affinity_penalty"]:.1f}, '
                 f'fairness penalty: {details["fairness_penalty"]:.1f})')
    lines.append('')

    # Schedule grid
    lines.append('## Schedule Grid')
    lines.append('')
    header = f'| {"Cluster":20s} | Size | Mon | Tue | Wed | Thu | Fri |'
    lines.append(header)
    lines.append(f'|{"-"*22}|------|-----|-----|-----|-----|-----|')
    for c in sorted(CLUSTERS, key=lambda x: (-CLUSTER_SIZES[x], x)):
        sched = schedules[c]
        days_str = ' | '.join('X' if d in sched else '.' for d in range(5))
        lines.append(f'| {c:20s} | {CLUSTER_SIZES[c]:4d} |  {days_str}  |')
    lines.append(f'| {"**Daily Total**":20s} | {"":4s} | {"  |  ".join(str(daily_counts[d]) for d in range(5))} |')
    lines.append(f'| {"**Capacity**":20s} | {"":4s} | {"  |  ".join(["185"]*5)} |')
    lines.append('')

    # Per-day neighborhood analysis
    lines.append('## Neighborhood Seat Analysis')
    lines.append('')
    for d in range(5):
        lines.append(f'### {DAYS[d]} ({daily_counts[d]} people in office)')
        lines.append('')
        lines.append(f'| {"Neighborhood":15s} | Seats | Demand | Surplus | Present Clusters |')
        lines.append(f'|{"-"*17}|-------|--------|---------|------------------|')

        present_clusters_by_hood = defaultdict(list)
        demand_by_hood = defaultdict(int)
        for c in CLUSTERS:
            if d in schedules[c]:
                for hood, seats_needed in CLUSTER_NEIGHBORHOOD_DEMAND[c].items():
                    present_clusters_by_hood[hood].append(c)
                    demand_by_hood[hood] += seats_needed

        overflow_hoods = {}
        donor_hoods = {}
        for hood in sorted(NEIGHBORHOOD_SEATS.keys()):
            seats = NEIGHBORHOOD_SEATS[hood]
            demand = demand_by_hood.get(hood, 0)
            surplus = seats - demand
            present = ', '.join(present_clusters_by_hood.get(hood, ['-']))
            lines.append(f'| {hood:15s} | {seats:5d} | {demand:6d} | {surplus:+7d} | {present} |')
            if surplus < 0:
                overflow_hoods[hood] = -surplus
            elif surplus > 0:
                donor_hoods[hood] = surplus

        lines.append('')
        if overflow_hoods:
            lines.append('**Borrowing needed:**')
            for hood, need in overflow_hoods.items():
                donors = ', '.join(f'{dh} ({donor_hoods[dh]} avail)' for dh in donor_hoods)
                lines.append(f'- {hood} needs {need} extra seats; available from: {donors}')
            lines.append('')

    # Affinity overlap
    lines.append('## Affinity Overlap')
    lines.append('')
    lines.append(f'| {"Cluster A":20s} | {"Cluster B":20s} | Weight | Overlap | Penalty |')
    lines.append(f'|{"-"*22}|{"-"*22}|--------|---------|---------|')
    for a, b, overlap, weight, penalty in details['affinity_details']:
        lines.append(f'| {a:20s} | {b:20s} | {weight:6.2f} | {overlap}/3     | {penalty:7.1f} |')
    lines.append('')

    # Undesirable day burden
    lines.append('## Undesirable Day Burden')
    lines.append('')
    lines.append(f'| {"Cluster":20s} | Size | Schedule       | Per-Person | Total  |')
    lines.append(f'|{"-"*22}|------|----------------|------------|--------|')
    for c in sorted(CLUSTERS, key=lambda x: (-CLUSTER_SIZES[x], x)):
        sched = schedules[c]
        sched_str = ','.join(DAYS[d] for d in sched)
        per_person = sum(DAY_PENALTY[d] for d in sched)
        total = per_person * CLUSTER_SIZES[c]
        lines.append(f'| {c:20s} | {CLUSTER_SIZES[c]:4d} | {sched_str:14s} | {per_person:10.2f} | {total:6.1f} |')
    lines.append('')

    return '\n'.join(lines)


if __name__ == '__main__':
    print('Optimizing seating schedule...')
    print(f'Clusters: {len(CLUSTERS)}, Total people: {sum(CLUSTER_SIZES.values())}, Seats: {TOTAL_SEATS}')
    print(f'Neighborhoods: {NEIGHBORHOOD_SEATS}')
    print()

    assignment, utility, details = optimize(restarts=200, local_iters=50000)

    if assignment is None:
        print('ERROR: No feasible solution found!')
    else:
        print(f'\nBest utility: {utility:.2f}')
        md = format_results(assignment, utility, details)
        with open('schedule.md', 'w') as f:
            f.write(md)
        print('\nResults written to schedule.md')
        print(md)
