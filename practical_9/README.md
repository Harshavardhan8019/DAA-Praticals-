# Practical 9: Prim's Algorithm (Greedy Minimum Spanning Tree)

This directory contains the Python implementation of **Prim's Algorithm** for finding the **Minimum Spanning Tree (MST)** of a connected, undirected, edge-weighted graph using a **Min-Heap (Priority Queue)**.

---

## 📌 Problem Overview & Paradigm

Given a connected, undirected graph $G = (V, E)$ with non-negative edge weights, a **Minimum Spanning Tree (MST)** is a subset of edges that connects all $V$ vertices without any cycles while minimizing the total edge weight.

### Method Implemented

- **Prim's Algorithm (`prims_mst(graph, start_vertex)`)**
  - Starts at an arbitrary seed vertex $s$ and grows the MST incrementally.
  - At each step, greedily selects the minimum weight edge $(u, v)$ connecting a vertex $u$ in the tree to a vertex $v$ outside the tree.
  - **Greedy Choice Property:** A locally optimal choice of the minimum cut edge yields a globally optimal MST.
  - **Time Complexity:** $\mathcal{O}(E \log V)$ using Min-Heap priority queue.
  - **Space Complexity:** $\mathcal{O}(V + E)$ for adjacency list and heap storage.

---

## ⚡ Complexity Summary

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Guarantees Optimality? |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Prim's (Min-Heap)** | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(V + E)$ | Greedy Paradigm | ✅ Yes (Always Optimal) |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_9` directory:
   ```bash
   cd practical_9
   ```
3. Execute the Python script:
   ```bash
   python prims_algorithm.py
   ```

---

## 📋 Sample Output

```text
==================================================
        PRIM'S MINIMUM SPANNING TREE (MST)         
==================================================
Default Graph Adjacency List:
  Node 0 -> Node 1 (weight 2), Node 3 (weight 3)
  Node 1 -> Node 0 (weight 2), Node 2 (weight 3), Node 4 (weight 8)
  Node 2 -> Node 1 (weight 3), Node 3 (weight 7), Node 4 (weight 6)
  Node 3 -> Node 0 (weight 3), Node 2 (weight 7), Node 4 (weight 1)
  Node 4 -> Node 1 (weight 8), Node 2 (weight 6), Node 3 (weight 1)

Use custom input? (y/N): n

--- Running Prim's Algorithm ---

========== MINIMUM SPANNING TREE EDGES ==========
Step   | Edge (u -> v)   | Weight    
--------------------------------------
1      | 0 -- 1          | 2         
2      | 1 -- 2          | 3         
3      | 0 -- 3          | 3         
4      | 3 -- 4          | 1         
--------------------------------------

========== RESULTS SUMMARY ==========
Total Vertices (V)    : 5
MST Edge Count        : 4
Total MST Weight      : 9
Execution Time        : 14200.00 ns
======================================
```

---

## 📖 Key Takeaways & Conclusion

1. **Greedy Spanning Tree Construction**:
   - Prim's algorithm operates on vertices, making it ideal for dense graphs ($E \approx V^2$).
2. **Min-Heap Efficiency**:
   - Using `heapq` reduces edge extraction cost from $\mathcal{O}(V)$ to $\mathcal{O}(\log V)$, enabling fast scale to large graphs.
