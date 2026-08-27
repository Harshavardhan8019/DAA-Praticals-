# Practical 12: Travelling Salesman Problem (Dynamic Programming - Held-Karp Algorithm)

This directory contains the Python implementation of the **Travelling Salesman Problem (TSP)** solved using the **Held-Karp Dynamic Programming algorithm** with **Bitmask State Representation**, alongside a comparison against the naive **Brute-Force Permutation** method.

---

## 📌 Problem Overview & Paradigm

Given a set of $N$ cities and pairwise distances $d(i, j)$ between them, find the minimum cost tour that starts at a designated origin city (e.g., City 0), visits every other city exactly once, and returns to the origin city.

### Methods Implemented

1. **Held-Karp Dynamic Programming (`tsp_held_karp(matrix)`)**
   - Uses bitmasks to represent subsets of visited cities. State is defined as $(S, u)$, representing the minimum cost to complete the tour starting at city $u$ having visited city subset $S$.
   - **Recurrence Relation:**
     $$g(S, u) = \min_{v \notin S} \left( d(u, v) + g(S \cup \{v\}, v) \right)$$
   - **Base Case:** $g(\text{All Cities}, u) = d(u, 0)$ (return cost to start city 0).
   - **Time Complexity:** $\mathcal{O}(N^2 \cdot 2^N)$
   - **Space Complexity:** $\mathcal{O}(N \cdot 2^N)$

2. **Brute-Force Permutations (`tsp_brute_force(matrix)`)**
   - Generates all $(N-1)!$ possible tour permutations.
   - **Time Complexity:** $\mathcal{O}(N!)$
   - **Space Complexity:** $\mathcal{O}(N)$

---

## ⚡ Complexity Summary

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Guarantees Optimality? |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Held-Karp DP** | $\mathcal{O}(N^2 \cdot 2^N)$ | $\mathcal{O}(N^2 \cdot 2^N)$ | $\mathcal{O}(N^2 \cdot 2^N)$ | $\mathcal{O}(N \cdot 2^N)$ | Dynamic Programming (Bitmask) | ✅ Yes (Always Optimal) |
| **Brute-Force** | $\mathcal{O}(N!)$ | $\mathcal{O}(N!)$ | $\mathcal{O}(N!)$ | $\mathcal{O}(N)$ | Exhaustive Search | ✅ Yes (Always Optimal) |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_12` directory:
   ```bash
   cd practical_12
   ```
3. Execute the Python script:
   ```bash
   python travelling_salesman.py
   ```

---

## 📋 Sample Output

```text
==================================================
   TRAVELLING SALESMAN PROBLEM (HELD-KARP DP)    
==================================================
Default Distance Matrix (4 Cities):
From\To     City 0    City 1    City 2    City 3
--------------------------------------------------
City 0           0        10        15        20
City 1          10         0        35        25
City 2          15        35         0        30
City 3          20        25        30         0
--------------------------------------------------

Use custom input? (y/N): n

--- Running Dynamic Programming (Held-Karp) Solver ---
--- Running Brute-Force Permutation Solver ---

========== OPTIMAL TOUR PATH ==========
Tour Path : City 0 -> City 1 -> City 3 -> City 2 -> City 0

========== RESULTS & METHOD COMPARISON ==========
Method          | Min Tour Cost   | Execution Time (ns) 
-------------------------------------------------------
Held-Karp (DP)  | 80              | 36400.00            
Brute-Force     | 80              | 28900.00            
=======================================================
```

---

## 📖 Key Takeaways & Conclusion

1. **Exponential Optimization**:
   - The Held-Karp DP algorithm reduces TSP complexity from factorial time $\mathcal{O}(N!)$ to exponential time $\mathcal{O}(N^2 2^N)$.
2. **Practical Applicability**:
   - Held-Karp makes exact TSP solutions feasible for up to $N \approx 20$ cities, whereas Brute-Force stalls for $N \ge 12$.
