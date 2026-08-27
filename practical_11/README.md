# Practical 11: Floyd-Warshall Algorithm (All-Pairs Shortest Path)

This directory contains the Python implementation of the **Floyd-Warshall Algorithm** for finding **All-Pairs Shortest Paths** in a directed, weighted graph using **Dynamic Programming**.

---

## 📌 Problem Overview & Paradigm

Given a directed weighted graph $G = (V, E)$ represented as an adjacency matrix, compute the shortest path distances between every pair of vertices $i, j \in V$.

### Method Implemented

- **Floyd-Warshall Tabulation (`floyd_warshall(graph)`)**
  - Maintains a 2D distance matrix $dist[i][j]$ and a predecessor matrix $next\_node[i][j]$.
  - Iterates through all possible intermediate vertices $k \in \{0, 1, \dots, V-1\}$ and updates paths:
  - **Recurrence Relation:**
    $$D^{(k)}[i][j] = \min\left(D^{(k-1)}[i][j], \; D^{(k-1)}[i][k] + D^{(k-1)}[k][j]\right)$$
  - **Time Complexity:** $\mathcal{O}(V^3)$ (three nested loops over vertices).
  - **Space Complexity:** $\mathcal{O}(V^2)$ for intermediate matrices.

---

## ⚡ Complexity Summary

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Guarantees Optimality? |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Floyd-Warshall (DP)** | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^2)$ | Dynamic Programming | ✅ Yes (Detects negative cycles) |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_11` directory:
   ```bash
   cd practical_11
   ```
3. Execute the Python script:
   ```bash
   python floyd_warshall.py
   ```

---

## 📋 Sample Output

```text
==================================================
      FLOYD-WARSHALL ALL-PAIRS SHORTEST PATH      
==================================================
Default Graph Adjacency Weight Matrix:

========== ALL-PAIRS SHORTEST DISTANCE MATRIX ==========
From\To Node    0   Node    1   Node    2   Node    3
-----------------------------------------------------
Node 0          0          3        INF          7
Node 1          8          0          2        INF
Node 2          5        INF          0          1
Node 3          2        INF        INF          0
-----------------------------------------------------

Use custom input? (y/N): n

--- Running Floyd-Warshall Dynamic Programming Solver ---

========== ALL-PAIRS SHORTEST DISTANCE MATRIX ==========
From\To Node    0   Node    1   Node    2   Node    3
-----------------------------------------------------
Node 0          0          3          5          6
Node 1          5          0          2          3
Node 2          3          6          0          1
Node 3          2          5          7          0
-----------------------------------------------------

========== SAMPLE PATH RECONSTRUCTIONS ==========
Source   -> Target   | Cost   | Path                
------------------------------------------------
Node 0   -> Node 1   | 3      | 0 -> 1              
Node 0   -> Node 2   | 5      | 0 -> 1 -> 2         
Node 0   -> Node 3   | 6      | 0 -> 1 -> 2 -> 3    
...

========== RESULTS SUMMARY ==========
Total Vertices (V)    : 4
Execution Time        : 19800.00 ns
======================================
```

---

## 📖 Key Takeaways & Conclusion

1. **All-Pairs Distance Matrix**:
   - Unlike Dijkstra's or Bellman-Ford algorithms which compute single-source shortest paths, Floyd-Warshall computes shortest paths between all pairs of nodes simultaneously in $\mathcal{O}(V^3)$ time.
2. **Dense Graph Suitability**:
   - Highly effective for dense graphs ($E \approx V^2$) where running Dijkstra $V$ times would take $\mathcal{O}(V E \log V) \approx \mathcal{O}(V^3 \log V)$.
