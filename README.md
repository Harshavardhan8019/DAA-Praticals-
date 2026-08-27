# Design & Analysis of Algorithms (DAA) Laboratory Practicals

![Python](https://img.shields.io/badge/Language-Python%203.x-blue.svg)
![Algorithms](https://img.shields.io/badge/Subject-Design%20%26%20Analysis%20of%20Algorithms-orange.svg)
![Author](https://img.shields.io/badge/Author-Harshavardhan-brightgreen.svg)
![Status](https://img.shields.io/badge/Status-Completed-success.svg)

Welcome to the **Design & Analysis of Algorithms (DAA)** laboratory practicals repository maintained by **Harshavardhan**. This repository contains clean, modular Python implementations of core fundamental algorithms, data structures, and empirical execution time analysis across multiple algorithmic paradigms.

---

## 📂 Repository Structure

The practicals are organized into four dedicated modules:

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
├── practical_3/               # Practical 3: Heap Data Structures & Operations
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
├── practical_7/               # Practical 7: Coin Change Problem (Greedy vs. DP Analysis)
│   ├── coin_change.py         # Greedy vs Dynamic Programming Coin Change
│   └── README.md              # Detailed documentation for Practical 7
│
├── practical_8/               # Practical 8: Graph Traversal Algorithms (DFS & BFS)
│   ├── graph_traversal.py     # Depth-First Search & Breadth-First Search
│   └── README.md              # Detailed documentation for Practical 8
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

### 6️⃣ Practical 7: Coin Change Problem (Greedy vs. Dynamic Programming)
Compares Greedy Choice strategy against 2D Dynamic Programming Tabulation for making change with minimum coins.

| Approach | Best Case | Average Case | Worst Case | Space Complexity | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Greedy Change** | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(1)$ | Greedy Choice | [`coin_change.py`](file:///practical_7/coin_change.py) |
| **DP Change** | $\mathcal{O}(n \times \text{amount})$ | $\mathcal{O}(n \times \text{amount})$ | $\mathcal{O}(n \times \text{amount})$ | $\mathcal{O}(n \times \text{amount})$ | Dynamic Programming | [`coin_change.py`](file:///practical_7/coin_change.py) |

### 7️⃣ Practical 8: Graph Traversal Algorithms (DFS & BFS)
Implements and evaluates Depth-First Search and Breadth-First Search on Adjacency List graphs.

| Algorithm | Time Complexity | Space Complexity | Data Structure | Paradigm | Script |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Depth-First Search (DFS)** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | Recursion Stack | Backtracking | [`graph_traversal.py`](file:///practical_8/graph_traversal.py) |
| **Breadth-First Search (BFS)** | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ | FIFO Queue (`deque`) | Level-Order | [`graph_traversal.py`](file:///practical_8/graph_traversal.py) |

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8+ installed on your system.

### Running a Practical Script

Navigate to the respective practical directory and execute the desired Python file using the terminal:

#### 🔹 Run Practical 1 (Sorting):
```bash
cd practical_1
python bubblesort.py
python insertionsort.py
python mergesort.py
python quicksort.py
python selectionsort.py
```

#### 🔹 Run Practical 2 (Searching):
```bash
cd practical_2
python linear_search.py
python binary_search.py
```

#### 🔹 Run Practical 3 (Max Heap):
```bash
cd practical_3
python max_heap.py
```

#### 🔹 Run Practical 4 (Factorial):
```bash
cd practical_4
python factorial.py
```

#### 🔹 Run Practical 5 (0/1 Knapsack):
```bash
cd practical_5
python knapsack.py
```

#### 🔹 Run Practical 7 (Coin Change):
```bash
cd practical_7
python coin_change.py
```

#### 🔹 Run Practical 8 (Graph Traversal):
```bash
cd practical_8
python graph_traversal.py
```

---

## ⚡ Key Insights & Empirical Findings

1. **Sorting Performance**:
   - Divide-and-Conquer algorithms ($O(n \log n)$) like **Merge Sort** and **Quick Sort** scale significantly better than quadratic algorithms ($O(n^2)$) as input size $n$ grows larger.
2. **Search Optimization**:
   - **Binary Search** outperforms Linear Search exponentially on large datasets, reducing search steps from $n$ to $\log_2(n)$.
3. **Heap Structure Efficiency**:
   - Building a heap takes linear time $O(n)$, allowing fast construction of Priority Queues with $O(\log n)$ logarithmic insertion and deletion costs.
4. **Recursion vs. Iteration Trade-offs**:
   - Both iterative and recursive factorial achieve $O(n)$ time complexity, but the iterative version is strictly more space-efficient ($O(1)$ auxiliary space) by eliminating the $O(n)$ call stack frame overhead.
5. **0/1 Knapsack Optimization**:
   - Dynamic Programming solves the 0/1 Knapsack problem in pseudo-polynomial time $\mathcal{O}(n \times W)$, guaranteeing an optimal subset selection where item values are maximized without exceeding weight capacity $W$.
6. **Greedy vs. Dynamic Programming Trade-offs**:
   - For Coin Change, **Greedy Choice** is fast ($\mathcal{O}(n \log n)$) but fails to guarantee global optimality on arbitrary coin denominations. **Dynamic Programming** guarantees an optimal minimum coin solution ($\mathcal{O}(n \times \text{amount})$) at the cost of pseudo-polynomial time and 2D table space overhead.
7. **Graph Traversal Paradigms**:
   - **DFS** traverses deeply along graph branches using recursion stack frames, making it ideal for path-finding, topological ordering, and cycle detection. **BFS** explores radially level-by-level using a queue, guaranteeing the shortest path in unweighted graphs. Both achieve optimal linear time complexity $\mathcal{O}(V + E)$.

---

## 👤 Author

Developed and maintained by **Harshavardhan**  
GitHub: [@Harshavardhan8019](https://github.com/Harshavardhan8019)  
Repository: [DAA-Praticals-](https://github.com/Harshavardhan8019/DAA-Praticals-)


