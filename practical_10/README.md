# Practical 10: Kruskal's Algorithm (Greedy Minimum Spanning Tree)

This directory contains the Python implementation of **Kruskal's Algorithm** for finding the **Minimum Spanning Tree (MST)** of a connected, undirected, edge-weighted graph using **Disjoint Set Union (DSU)** with **Path Compression** and **Union by Rank**.

---

## 📌 Problem Overview & Paradigm

Given a connected graph $G = (V, E)$, Kruskal's algorithm constructs a Minimum Spanning Tree by sorting all graph edges in non-decreasing order of weight and greedily adding edges that do not form a cycle.

### Method Implemented

- **Kruskal's Algorithm with DSU (`kruskals_mst(num_vertices, edges)`)**
  - Sorts all edges in non-decreasing order: $\mathcal{O}(E \log E)$.
  - Uses Disjoint Set Union (DSU) to test if adding an edge forms a cycle:
    - **`find(u)`:** Path compression flattens tree height to nearly $\mathcal{O}(1)$.
    - **`union(u, v)`:** Union by rank attaches smaller tree under root of larger tree.
  - **Time Complexity:** $\mathcal{O}(E \log E)$ or $\mathcal{O}(E \log V)$.
  - **Space Complexity:** $\mathcal{O}(V + E)$ for DSU parent/rank arrays and edge lists.

---

## ⚡ Complexity Summary

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Guarantees Optimality? |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Kruskal's (DSU)** | $\mathcal{O}(E \log E)$ | $\mathcal{O}(E \log E)$ | $\mathcal{O}(E \log E)$ | $\mathcal{O}(V + E)$ | Greedy Paradigm | ✅ Yes (Always Optimal) |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_10` directory:
   ```bash
   cd practical_10
   ```
3. Execute the Python script:
   ```bash
   python kruskals_algorithm.py
   ```

---

## 📋 Sample Output

```text
==================================================
      KRUSKAL'S MINIMUM SPANNING TREE (MST)       
==================================================
Default Graph Edges:
  Edge (0 -- 1) with weight 4
  Edge (0 -- 2) with weight 4
  Edge (1 -- 2) with weight 2
  Edge (1 -- 3) with weight 6
  Edge (2 -- 3) with weight 8
  Edge (2 -- 4) with weight 9
  Edge (3 -- 4) with weight 7
  Edge (3 -- 5) with weight 5
  Edge (4 -- 5) with weight 10

Use custom input? (y/N): n

--- Running Kruskal's Algorithm ---

========== SELECTED MST EDGES ==========
Step   | Edge (u -- v)   | Weight    
--------------------------------------
1      | 1 -- 2          | 2         
2      | 0 -- 1          | 4         
3      | 3 -- 5          | 5         
4      | 1 -- 3          | 6         
5      | 3 -- 4          | 7         
--------------------------------------

========== RESULTS SUMMARY ==========
Total Vertices (V)    : 6
Total Graph Edges (E) : 9
MST Edges Selected    : 5
Edges Skipped (Cycles): 4
Total MST Weight      : 24
Execution Time        : 18100.00 ns
======================================
```

---

## 📖 Key Takeaways & Conclusion

1. **Edge-Centric Greedy Strategy**:
   - Unlike Prim's algorithm which grows a connected tree from a vertex, Kruskal's algorithm processes global edges and works exceptionally well on sparse graphs ($E \ll V^2$).
2. **Nearly Constant DSU Operations**:
   - With path compression and union by rank, DSU operations run in $\mathcal{O}(\alpha(V))$ time per operation (where $\alpha$ is the Inverse Ackermann function, effectively $\le 4$).
