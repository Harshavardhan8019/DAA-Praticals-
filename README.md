# Design & Analysis of Algorithms (DAA) Laboratory Practicals

![Python](https://img.shields.io/badge/Language-Python%203.x-blue.svg)
![Subject](https://img.shields.io/badge/Subject-Design%20%26%20Analysis%20of%20Algorithms-orange.svg)
![Author](https://img.shields.io/badge/Author-Harshavardhan-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

Welcome to the **Design & Analysis of Algorithms (DAA)** laboratory practicals repository maintained by **Harshavardhan**. This repository contains clean, modular Python implementations of core fundamental algorithms, data structures, and empirical execution time analysis across multiple algorithmic paradigms.

---

## 📂 Repository Structure

The practicals are organized into dedicated modules for each laboratory experiment:

```text
DAA-Practicals/
├── practical_1/               # Practical 1: Sorting Algorithms & Performance Analysis
│   ├── bubblesort.py          # Optimized Bubble Sort implementation
│   ├── insertionsort.py       # Insertion Sort implementation
│   ├── mergesort.py           # Merge Sort (Divide & Conquer) implementation
│   ├── quicksort.py           # Quick Sort (Partitioning) implementation
│   ├── selectionsort.py       # Selection Sort implementation
│   └── README.md              # Detailed documentation for Practical 1
│
├── practical_2/               # Practical 2: Searching Algorithms & Time Measurement
│   ├── binary_search.py       # Binary Search (Logarithmic search)
│   ├── linear_search.py       # Linear Search (Sequential search)
│   └── README.md              # Detailed documentation for Practical 2
│
├── practical_3/               # Practical 3: Max Heap Data Structures & Operations
│   ├── max_heap.py            # Max Heap (Heapify, Build Heap, Insert, Delete)
│   └── README.md              # Detailed documentation for Practical 3
│
├── practical_4/               # Practical 4: Factorial (Iterative vs. Recursive Analysis)
│   ├── factorial.py           # Iterative and Recursive Factorial implementations
│   └── README.md              # Detailed documentation for Practical 4
│
├── practical_5/               # Practical 5: 0/1 Knapsack Problem (Dynamic Programming)
│   ├── knapsack.py            # Tabulation Dynamic Programming 0/1 Knapsack
│   └── README.md              # Detailed documentation for Practical 5
│
├── practical_6/               # Practical 6: Matrix Chain Multiplication (Dynamic Programming)
│   ├── matrix_chain_multiplication.py # DP Matrix Chain Order & Parenthesization
│   └── README.md              # Detailed documentation for Practical 6
│
├── practical_7/               # Practical 7: Coin Change Problem (Greedy vs. DP Analysis)
│   ├── coin_change.py         # Greedy vs Dynamic Programming Coin Change
│   └── README.md              # Detailed documentation for Practical 7
│
├── practical_8/               # Practical 8: Graph Traversal Algorithms (DFS & BFS)
│   ├── graph_traversal.py     # Depth-First Search & Breadth-First Search
│   └── README.md              # Detailed documentation for Practical 8
│
├── practical_9/               # Practical 9: Prim's Algorithm (Greedy MST)
│   ├── prims_algorithm.py     # Prim's Minimum Spanning Tree with Min-Heap
│   └── README.md              # Detailed documentation for Practical 9
│
├── practical_10/              # Practical 10: Kruskal's Algorithm (Greedy MST with DSU)
│   ├── kruskals_algorithm.py  # Kruskal's Minimum Spanning Tree with DSU
│   └── README.md              # Detailed documentation for Practical 10
│
├── practical_11/              # Practical 11: Floyd-Warshall Algorithm (All-Pairs Shortest Path)
│   ├── floyd_warshall.py      # Floyd-Warshall All-Pairs Shortest Path DP
│   └── README.md              # Detailed documentation for Practical 11
│
├── practical_12/              # Practical 12: Travelling Salesman Problem (Held-Karp DP)
│   ├── travelling_salesman.py # Bitmask DP Held-Karp vs Brute-Force TSP
│   └── README.md              # Detailed documentation for Practical 12
│
└── README.md                  # Main Repository Overview & Documentation
```

---

## 📊 Comprehensive Algorithmic Summary

### 1️⃣ Practical 1: Sorting Algorithms Analysis
Focuses on implementing and analyzing five basic and advanced sorting techniques.

| Algorithm | Best Case | Average Case | Worst Case | Space Complexity | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Bubble Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Brute Force / Exchange | [`bubblesort.py`](file:///practical_1/bubblesort.py) |
| **Insertion Sort** | $\mathcal{O}(n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Incremental Insertion | [`insertionsort.py`](file:///practical_1/insertionsort.py) |
| **Selection Sort** | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ | Selection | [`selectionsort.py`](file:///practical_1/selectionsort.py) |
| **Merge Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ | Divide & Conquer | [`mergesort.py`](file:///practical_1/mergesort.py) |
| **Quick Sort** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ | Divide & Conquer | [`quicksort.py`](file:///practical_1/quicksort.py) |

### 2️⃣ Practical 2: Searching Algorithms & Runtime Analysis
Compares sequential search vs. logarithmic search efficiency on static and dynamic inputs.

| Algorithm | Best Case | Average Case | Worst Case | Pre-condition | Space Complexity | Script |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Linear Search** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | None (Works on unsorted) | $\mathcal{O}(1)$ | [`linear_search.py`](file:///practical_2/linear_search.py) |
| **Binary Search** | $\mathcal{O}(1)$ | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Array must be **Sorted** | $\mathcal{O}(1)$ | [`binary_search.py`](file:///practical_2/binary_search.py) |

### 3️⃣ Practical 3: Max Heap Data Structure
Demonstrates tree-based priority queue construction and manipulation routines.

| Operation | Time Complexity | Auxiliary Space | Description | Script |
| :--- | :---: | :---: | :--- | :---: |
| **Heapify** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Maintains heap invariant top-down | [`max_heap.py`](file:///practical_3/max_heap.py) |
| **Build Max Heap** | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Constructs max heap from raw array | [`max_heap.py`](file:///practical_3/max_heap.py) |
| **Insert Element** | $\mathcal{O}(\log n)$ | $\mathcal{O}(1)$ | Adds item and sifts upward | [`max_heap.py`](file:///practical_3/max_heap.py) |
| **Delete Maximum** | $\mathcal{O}(\log n)$ | $\mathcal{O}(\log n)$ | Extracts root item & restores heap | [`max_heap.py`](file:///practical_3/max_heap.py) |

### 4️⃣ Practical 4: Factorial Calculation (Iterative vs. Recursive)
Compares iterative accumulation versus recursive divide-and-conquer function calls for computing factorial numbers.

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Iterative Factorial** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Iterative Accumulation | [`factorial.py`](file:///practical_4/factorial.py) |
| **Recursive Factorial** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Recursive / Decrease-and-Conquer | [`factorial.py`](file:///practical_4/factorial.py) |

### 5️⃣ Practical 5: 0/1 Knapsack Problem (Dynamic Programming)
Solves the 0/1 Knapsack decision and value optimization problem using 2D Dynamic Programming Tabulation.

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **0/1 Knapsack (DP)** | $\mathcal{O}(n \times W)$ | $\mathcal{O}(n \times W)$ | $\mathcal{O}(n \times W)$ | $\mathcal{O}(n \times W)$ | Dynamic Programming | [`knapsack.py`](file:///practical_5/knapsack.py) |

### 6️⃣ Practical 6: Matrix Chain Multiplication (Dynamic Programming)
Computes the optimal parenthesization of a sequence of matrices to minimize total scalar multiplications.

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Matrix Chain Order (DP)** | $\mathcal{O}(n^3)$ | $\mathcal{O}(n^3)$ | $\mathcal{O}(n^3)$ | $\mathcal{O}(n^2)$ | Dynamic Programming | [`matrix_chain_multiplication.py`](file:///practical_6/matrix_chain_multiplication.py) |

### 7️⃣ Practical 7: Coin Change Problem (Greedy vs. Dynamic Programming)
Compares Greedy Choice strategy against 2D Dynamic Programming Tabulation for making change with minimum coins.

| Approach | Best Case | Average Case | Worst Case | Space Complexity | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Greedy Change** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ | Greedy Choice | [`coin_change.py`](file:///practical_7/coin_change.py) |
| **DP Change** | $\mathcal{O}(n \times \text{amount})$ | $\mathcal{O}(n \times \text{amount})$ | $\mathcal{O}(n \times \text{amount})$ | $\mathcal{O}(n \times \text{amount})$ | Dynamic Programming | [`coin_change.py`](file:///practical_7/coin_change.py) |

### 8️⃣ Practical 8: Graph Traversal Algorithms (DFS & BFS)
Implements and evaluates Depth-First Search and Breadth-First Search on Adjacency List graphs.

| Algorithm | Time Complexity | Space Complexity | Data Structure | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Depth-First Search (DFS)** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | Recursion Stack | Backtracking | [`graph_traversal.py`](file:///practical_8/graph_traversal.py) |
| **Breadth-First Search (BFS)** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | FIFO Queue (`deque`) | Level-Order | [`graph_traversal.py`](file:///practical_8/graph_traversal.py) |

### 9️⃣ Practical 9: Prim's Algorithm (Greedy MST)
Greedy vertex-based algorithm to construct Minimum Spanning Tree using Min-Heap priority queue.

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Prim's Algorithm** | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(E \log V)$ | $\mathcal{O}(V + E)$ | Greedy Choice | [`prims_algorithm.py`](file:///practical_9/prims_algorithm.py) |

### 🔟 Practical 10: Kruskal's Algorithm (Greedy MST with DSU)
Greedy edge-based algorithm to construct Minimum Spanning Tree using Disjoint Set Union (DSU) data structure.

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Kruskal's Algorithm** | $\mathcal{O}(E \log E)$ | $\mathcal{O}(E \log E)$ | $\mathcal{O}(E \log E)$ | $\mathcal{O}(V + E)$ | Greedy Choice | [`kruskals_algorithm.py`](file:///practical_10/kruskals_algorithm.py) |

### 1️⃣1️⃣ Practical 11: Floyd-Warshall Algorithm (All-Pairs Shortest Path)
Dynamic Programming algorithm to compute all-pairs shortest paths on weighted directed graphs.

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Floyd-Warshall (DP)** | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^3)$ | $\mathcal{O}(V^2)$ | Dynamic Programming | [`floyd_warshall.py`](file:///practical_11/floyd_warshall.py) |

### 1️⃣2️⃣ Practical 12: Travelling Salesman Problem (Held-Karp DP)
Dynamic Programming algorithm utilizing bitmask state representation to solve TSP in exponential time.

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Held-Karp (Bitmask DP)** | $\mathcal{O}(N^2 \cdot 2^N)$ | $\mathcal{O}(N^2 \cdot 2^N)$ | $\mathcal{O}(N^2 \cdot 2^N)$ | $\mathcal{O}(N \cdot 2^N)$ | Dynamic Programming | [`travelling_salesman.py`](file:///practical_12/travelling_salesman.py) |

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+ installed on your system.

### Running Practical Scripts

Navigate to any practical directory and execute the target Python file using your terminal:

```bash
# Practical 1: Sorting
cd practical_1 && python bubblesort.py

# Practical 2: Searching
cd practical_2 && python binary_search.py

# Practical 3: Max Heap
cd practical_3 && python max_heap.py

# Practical 4: Factorial
cd practical_4 && python factorial.py

# Practical 5: 0/1 Knapsack
cd practical_5 && python knapsack.py

# Practical 6: Matrix Chain Multiplication
cd practical_6 && python matrix_chain_multiplication.py

# Practical 7: Coin Change
cd practical_7 && python coin_change.py

# Practical 8: Graph Traversal
cd practical_8 && python graph_traversal.py

# Practical 9: Prim's MST
cd practical_9 && python prims_algorithm.py

# Practical 10: Kruskal's MST
cd practical_10 && python kruskals_algorithm.py

# Practical 11: Floyd-Warshall
cd practical_11 && python floyd_warshall.py

# Practical 12: Travelling Salesman Problem
cd practical_12 && python travelling_salesman.py
```

---

## ⚡ Key Insights & Empirical Findings

1. **Sorting Performance**:
   - Divide-and-Conquer algorithms ($\mathcal{O}(n \log n)$) like **Merge Sort** and **Quick Sort** scale significantly better than quadratic algorithms ($\mathcal{O}(n^2)$) as input size $n$ grows larger.
2. **Search Optimization**:
   - **Binary Search** outperforms Linear Search exponentially on large datasets, reducing search steps from $n$ to $\log_2(n)$.
3. **Heap Structure Efficiency**:
   - Building a heap takes linear time $\mathcal{O}(n)$, allowing fast construction of Priority Queues with $\mathcal{O}(\log n)$ logarithmic insertion and deletion costs.
4. **Recursion vs. Iteration Trade-offs**:
   - Both iterative and recursive factorial achieve $\mathcal{O}(n)$ time complexity, but the iterative version is strictly more space-efficient ($\mathcal{O}(1)$ auxiliary space) by eliminating call stack overhead.
5. **0/1 Knapsack Optimization**:
   - Dynamic Programming solves the 0/1 Knapsack problem in pseudo-polynomial time $\mathcal{O}(n \times W)$, guaranteeing an optimal subset selection where item values are maximized without exceeding capacity $W$.
6. **Matrix Chain Multiplication**:
   - Dynamic Programming reduces matrix parenthesization complexity from Catalan time $\Omega(4^n / n^{3/2})$ to polynomial time $\mathcal{O}(n^3)$.
7. **Greedy vs. Dynamic Programming Trade-offs**:
   - For Coin Change, **Greedy Choice** is fast ($\mathcal{O}(n \log n)$) but fails to guarantee global optimality on arbitrary coin denominations. **Dynamic Programming** guarantees an optimal minimum coin solution ($\mathcal{O}(n \times \text{amount})$).
8. **Graph Traversal Paradigms**:
   - **DFS** uses stack frames for deep path-finding and cycle detection. **BFS** uses a FIFO queue for level-order exploration and shortest paths in unweighted graphs. Both run in linear time $\mathcal{O}(V + E)$.
9. **Minimum Spanning Trees (Prim vs. Kruskal)**:
   - **Prim's Algorithm** ($\mathcal{O}(E \log V)$) grows trees from vertices, excelling on dense graphs ($E \approx V^2$). **Kruskal's Algorithm** ($\mathcal{O}(E \log E)$) processes global edges using Disjoint Set Union (DSU), excelling on sparse graphs ($E \ll V^2$).
10. **All-Pairs Shortest Paths**:
    - **Floyd-Warshall** computes shortest paths between all pairs of nodes in $\mathcal{O}(V^3)$ time, outperforming repeated single-source shortest path execution on dense graphs.
11. **Exact NP-Hard Problem Optimization (TSP)**:
    - **Held-Karp DP with Bitmasking** optimizes TSP from factorial time $\mathcal{O}(N!)$ to exponential time $\mathcal{O}(N^2 \cdot 2^N)$, making exact solutions feasible for larger problem sizes.

---

## 👤 Author

Developed and maintained by **Harshavardhan**  
GitHub: [@Harshavardhan8019](https://github.com/Harshavardhan8019)  
Repository: [DAA-Praticals-](https://github.com/Harshavardhan8019/DAA-Praticals-)
