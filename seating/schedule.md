# Seating Schedule

Total utility: -71.47 (day penalty: 51.3, affinity penalty: 14.2, fairness penalty: 6.0)

## Schedule Grid

| Cluster              | Size | Mon | Tue | Wed | Thu | Fri |
|----------------------|------|-----|-----|-----|-----|-----|
| Kittle               |   63 |  X | . | X | X | .  |
| Pragma               |   54 |  . | X | X | X | .  |
| Xpro                 |   27 |  X | X | . | X | .  |
| Alex-Data            |   26 |  X | X | X | . | .  |
| Scarp-Infra          |   14 |  . | X | X | X | .  |
| Scarp-Cloud          |   11 |  X | X | . | X | .  |
| Alex-Research        |    8 |  X | X | X | . | .  |
| Bala                 |    8 |  X | X | . | X | .  |
| Varma                |    8 |  X | X | . | X | .  |
| BL-Mod               |    7 |  X | X | X | . | .  |
| Scarp-Database       |    7 |  X | X | X | . | .  |
| LBA                  |    6 |  X | X | X | . | .  |
| **Daily Total**      |      | 171  |  176  |  185  |  185  |  0 |
| **Capacity**         |      | 185  |  185  |  185  |  185  |  185 |

## Neighborhood Seat Analysis

### Mon (171 people in office)

| Neighborhood    | Seats | Demand | Surplus | Present Clusters |
|-----------------|-------|--------|---------|------------------|
| Alexandre       |    31 |     34 |      -3 | Alex-Data, Alex-Research |
| Bala            |     7 |      8 |      -1 | Bala |
| Kittle          |    56 |     70 |     -14 | BL-Mod, Kittle |
| MechCoop        |    56 |     33 |     +23 | LBA, Xpro |
| Scarpati        |    26 |     18 |      +8 | Scarp-Cloud, Scarp-Database |
| Varma           |     7 |      8 |      -1 | Varma |

**Borrowing needed:**
- Alexandre needs 3 extra seats; available from: MechCoop (23 avail), Scarpati (8 avail)
- Bala needs 1 extra seats; available from: MechCoop (23 avail), Scarpati (8 avail)
- Kittle needs 14 extra seats; available from: MechCoop (23 avail), Scarpati (8 avail)
- Varma needs 1 extra seats; available from: MechCoop (23 avail), Scarpati (8 avail)

### Tue (176 people in office)

| Neighborhood    | Seats | Demand | Surplus | Present Clusters |
|-----------------|-------|--------|---------|------------------|
| Alexandre       |    31 |     34 |      -3 | Alex-Data, Alex-Research |
| Bala            |     7 |      8 |      -1 | Bala |
| Kittle          |    56 |      7 |     +49 | BL-Mod |
| MechCoop        |    56 |     81 |     -25 | LBA, Pragma, Xpro |
| Scarpati        |    26 |     38 |     -12 | Pragma, Scarp-Cloud, Scarp-Database, Scarp-Infra |
| Varma           |     7 |      8 |      -1 | Varma |

**Borrowing needed:**
- Alexandre needs 3 extra seats; available from: Kittle (49 avail)
- Bala needs 1 extra seats; available from: Kittle (49 avail)
- MechCoop needs 25 extra seats; available from: Kittle (49 avail)
- Scarpati needs 12 extra seats; available from: Kittle (49 avail)
- Varma needs 1 extra seats; available from: Kittle (49 avail)

### Wed (185 people in office)

| Neighborhood    | Seats | Demand | Surplus | Present Clusters |
|-----------------|-------|--------|---------|------------------|
| Alexandre       |    31 |     34 |      -3 | Alex-Data, Alex-Research |
| Bala            |     7 |      0 |      +7 | - |
| Kittle          |    56 |     70 |     -14 | BL-Mod, Kittle |
| MechCoop        |    56 |     54 |      +2 | LBA, Pragma |
| Scarpati        |    26 |     27 |      -1 | Pragma, Scarp-Database, Scarp-Infra |
| Varma           |     7 |      0 |      +7 | - |

**Borrowing needed:**
- Alexandre needs 3 extra seats; available from: Bala (7 avail), MechCoop (2 avail), Varma (7 avail)
- Kittle needs 14 extra seats; available from: Bala (7 avail), MechCoop (2 avail), Varma (7 avail)
- Scarpati needs 1 extra seats; available from: Bala (7 avail), MechCoop (2 avail), Varma (7 avail)

### Thu (185 people in office)

| Neighborhood    | Seats | Demand | Surplus | Present Clusters |
|-----------------|-------|--------|---------|------------------|
| Alexandre       |    31 |      0 |     +31 | - |
| Bala            |     7 |      8 |      -1 | Bala |
| Kittle          |    56 |     63 |      -7 | Kittle |
| MechCoop        |    56 |     75 |     -19 | Pragma, Xpro |
| Scarpati        |    26 |     31 |      -5 | Pragma, Scarp-Cloud, Scarp-Infra |
| Varma           |     7 |      8 |      -1 | Varma |

**Borrowing needed:**
- Bala needs 1 extra seats; available from: Alexandre (31 avail)
- Kittle needs 7 extra seats; available from: Alexandre (31 avail)
- MechCoop needs 19 extra seats; available from: Alexandre (31 avail)
- Scarpati needs 5 extra seats; available from: Alexandre (31 avail)
- Varma needs 1 extra seats; available from: Alexandre (31 avail)

### Fri (0 people in office)

| Neighborhood    | Seats | Demand | Surplus | Present Clusters |
|-----------------|-------|--------|---------|------------------|
| Alexandre       |    31 |      0 |     +31 | - |
| Bala            |     7 |      0 |      +7 | - |
| Kittle          |    56 |      0 |     +56 | - |
| MechCoop        |    56 |      0 |     +56 | - |
| Scarpati        |    26 |      0 |     +26 | - |
| Varma           |     7 |      0 |      +7 | - |

## Affinity Overlap

| Cluster A            | Cluster B            | Weight | Overlap | Penalty |
|----------------------|----------------------|--------|---------|---------|
| Kittle               | BL-Mod               |   0.30 | 2/3     |     2.1 |
| Alex-Data            | Alex-Research        |   0.30 | 3/3     |     0.0 |
| Scarp-Infra          | Scarp-Cloud          |   0.30 | 2/3     |     3.3 |
| Xpro                 | BL-Mod               |   0.30 | 2/3     |     2.1 |
| Scarp-Infra          | Scarp-Database       |   0.30 | 2/3     |     2.1 |
| Scarp-Cloud          | Scarp-Database       |   0.30 | 2/3     |     2.1 |
| Pragma               | Scarp-Infra          |   0.80 | 3/3     |     0.0 |
| Pragma               | BL-Mod               |   0.30 | 2/3     |     2.1 |
| Pragma               | Alex-Research        |   0.05 | 2/3     |     0.4 |

## Undesirable Day Burden

| Cluster              | Size | Schedule       | Per-Person | Total  |
|----------------------|------|----------------|------------|--------|
| Kittle               |   63 | Mon,Wed,Thu    |       0.30 |   18.9 |
| Pragma               |   54 | Tue,Wed,Thu    |       0.00 |    0.0 |
| Xpro                 |   27 | Mon,Tue,Thu    |       0.30 |    8.1 |
| Alex-Data            |   26 | Mon,Tue,Wed    |       0.30 |    7.8 |
| Scarp-Infra          |   14 | Tue,Wed,Thu    |       0.00 |    0.0 |
| Scarp-Cloud          |   11 | Mon,Tue,Thu    |       0.30 |    3.3 |
| Alex-Research        |    8 | Mon,Tue,Wed    |       0.30 |    2.4 |
| Bala                 |    8 | Mon,Tue,Thu    |       0.30 |    2.4 |
| Varma                |    8 | Mon,Tue,Thu    |       0.30 |    2.4 |
| BL-Mod               |    7 | Mon,Tue,Wed    |       0.30 |    2.1 |
| Scarp-Database       |    7 | Mon,Tue,Wed    |       0.30 |    2.1 |
| LBA                  |    6 | Mon,Tue,Wed    |       0.30 |    1.8 |
