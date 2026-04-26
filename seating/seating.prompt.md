# Seating Optimization

## Problem

We have ~236 hoteling employees across 6 groups who each need to come into the office 3 days per week, but only 185 bookable seats. The goal is to assign each cluster a 3-day weekly schedule that maximizes utility.

## Data Files

- **people.csv** (latin-1 encoded): Master employee list. Key columns:
  - `Cluster 1`: primary cluster assignment (12 clusters)
  - `Cluster 2`: secondary affinity
  - `Group`: one of Alexandre, Bala, MechCoop, Kittle, Scarpati, Varma
  - `Org4`: SCR org code used to define team boundaries
  - `Include H/C`: Y = hoteling (in scope), N = excluded

- **neighborhoods.csv**: Physical seat allocation per neighborhood. Neighborhoods map to groups:
  - Alexandre: 31 seats
  - Bala: 7 seats
  - Kittle: 56 seats
  - MechCoop (Cooper + Mechner): 56 seats
  - Scarpati: 26 seats
  - Varma: 7 seats
  - Total: 185 bookable seats

- **affinities.csv**: Pairwise cluster affinities (1-10 scale). Edit this to change how strongly clusters are pulled to co-locate.

## Clusters

12 clusters derived from groups, split by function:

| Cluster | Size | Home Neighborhood |
|---|---|---|
| Kittle | 63 | Kittle |
| BL-Mod | 7 | Kittle |
| Pragma | 51 (45 MechCoop + 6 Scarpati) | MechCoop / Scarpati |
| Xpro | 27 | MechCoop |
| Alex-Data | 26 | Alexandre |
| Alex-Research | 8 | Alexandre |
| Scarp-Infra | 14 | Scarpati |
| Scarp-Cloud | 11 | Scarpati |
| Scarp-Database | 7 | Scarpati |
| Bala | 8 | Bala |
| Varma | 8 | Varma |
| LBA | 6 | MechCoop |

## Constraints

1. **Capacity**: no more than 185 people in office on any day
2. **3 days per week**: each cluster is assigned exactly 3 of {Mon, Tue, Wed, Thu, Fri}
3. **Teams as units**: everyone in a cluster comes in on the same days

## Utility Function (what the optimizer maximizes)

1. **Day preference**: Tue/Wed/Thu are preferred. Friday is penalized (-1.0). and Monday is relatively mildly penalized (-0.3). Penalty is per person-day.
2. **Affinity co-location**: clusters listed in affinities.csv include a penalty for days the groups aren't together, using the same scale as day preference, and also to be counted per person-day (for the smaller group so as not to double-count).
3. **Fairness**: variance in undesirable-day burden across clusters is penalized, so the Mon/Fri pain is spread around.

## Seat Borrowing

Neighborhoods can "borrow" seats from each other. When a cluster is out on a given day, its home neighborhood's seats are available to overflow from other neighborhoods. The optimizer enforces the global 185-seat cap; the per-neighborhood borrowing is computed after the fact to show feasibility.

For example, on a day when Kittle (63 people) is out, 49 of Kittle's 56 seats are available for MechCoop or Scarpati overflow.

## How to Run

Use an AI assistant with access to these files. The optimization is a stochastic search:

1. Load clusters (sizes and home neighborhoods) from people.csv
2. Load affinities from affinities.csv
3. Load seat counts from neighborhoods.csv
4. Enumerate all C(5,3) = 10 possible 3-day schedules
5. Random search + local search to find the assignment of schedules to clusters that maximizes the utility function subject to the daily capacity constraint
6. Write the results to `schedule.md` in the seating directory, including:
   - A schedule grid showing each cluster's assigned days (X/.) with cluster size
   - Daily total row showing headcount per day vs. the 185-seat cap
   - A per-day neighborhood seat analysis table showing: seats available, demand from home clusters, surplus/deficit, and which clusters are present
   - For each day with overflow, a borrowing summary: which neighborhoods need extra seats and where they come from
   - Affinity overlap summary: each pair from affinities.csv with overlap days out of 3
   - Undesirable day burden per cluster (penalty x person-days)

To adjust priorities, edit affinities.csv weights and re-run.

## Key Design Decisions

- **Cluster granularity**: clusters (not individual teams) are the scheduling unit. Teams within a cluster all follow the same schedule. This keeps the system simple and manageable.
- **Org4 as team basis**: teams were originally derived from SCR org4 codes, with small teams merged into larger ones (minimum ~3-5 people). Clusters group related teams.
- **Pragma split**: 6 Pragma-Infra people sit in Scarpati neighborhood, so Pragma's seat demand is split across two neighborhoods.
- **LBA is an island**: the LB Trading + MuniBroker cluster has weak affinity to others; it schedules flexibly.
- **Others excluded**: non-tech people and managers with private desks (Include H/C = N) are outside this system.

## Open Items

- Rotation for fairness: the current schedule is static (same days every week). A 2-3 week rotation could spread Mon/Fri burden more evenly.
- Month-end coverage: certain teams must be in on month-ends (sometimes Mon/Fri); not yet modeled.
- Kittle sub-clustering: Kittle (63 people) is the largest cluster and could be split to allow more scheduling flexibility.
