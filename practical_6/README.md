# Practical 6: Matrix Chain Multiplication (Dynamic Programming Analysis)

This directory contains the Python implementation of the **Matrix Chain Multiplication Problem** solved using the **Dynamic Programming (DP)** paradigm. The program calculates the minimum number of scalar multiplications required to multiply a chain of matrices $A_1, A_2, \dots, A_n$ and outputs the optimal parenthesization sequence, full $m$ and $s$ DP matrices, and execution timing.

---

## 📌 Problem Overview & Paradigm

Given a sequence of matrices $\langle A_1, A_2, \dots, A_n \rangle$ where matrix $A_i$ has dimensions $p_{i-1} \times p_i$, find the optimal parenthesization that minimizes the total number of scalar multiplications required to compute the product $A_1 A_2 \dots A_n$.

### Method Implemented

- **Dynamic Programming Tabulation (`matrix_chain_order(dimensions)`)**
  - Constructs a 2D matrix $m[i][j]$ representing the minimum scalar multiplications needed to evaluate $A_i \dots A_j$, and $s[i][j]$ storing the optimal split index $k$.
  - **Recurrence Relation:**
    $$m[i][j] = \begin{cases} 0 & \text{if } i = j \\ \min_{i \le k < j} \left( m[i][k] + m[k+1][j] + p_{i-1} p_k p_j \right) & \text{if } i < j \end{cases}$$
  - **Time Complexity:** $\mathcal{O}(n^3)$ (three nested loops over chain lengths, starting positions, and split points).
  - **Space Complexity:** $\mathcal{O}(n^2)$ for the lookup matrices $m$ and $s$.

---

## ⚡ Complexity Summary

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space | Paradigm | Guarantees Optimality? |
| :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **Dynamic Programming (Tabulation)** | $\mathcal{O}(n^3)$ | $\mathcal{O}(n^3)$ | $\mathcal{O}(n^3)$ | $\mathcal{O}(n^2)$ | Dynamic Programming | ✅ Yes (Always Optimal) |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_6` directory:
   ```bash
   cd practical_6
   ```
3. Execute the Python script:
   ```bash
   python matrix_chain_multiplication.py
   ```

---

## 📋 Sample Output

```text
==================================================
   MATRIX CHAIN MULTIPLICATION (DYNAMIC PROGRAMMING)
==================================================
Default Matrix Dimensions Sequence p:
  p = [10, 30, 5, 60, 10, 20, 25]
  • Matrix A1: 10 x 30
  • Matrix A2: 30 x 5
  • Matrix A3: 5 x 60
  • Matrix A4: 60 x 10
  • Matrix A5: 10 x 20
  • Matrix A6: 20 x 25

Use custom input? (y/N): n

--- Running Dynamic Programming Matrix Chain Order ---

========== M TABLE (Minimum Scalar Multiplications) ==========
i\j       j=1   j=2   j=3   j=4   j=5   j=6
--------------------------------------------------
i=1         0  1500  4500  2200  3600  5125
i=2         -     0  9000  2100  4100  5850
i=3         -     -     0  3000  3500  4750
i=4         -     -     -     0 12000 14500
i=5         -     -     -     -     0  5000
i=6         -     -     -     -     -     0
--------------------------------------------------

========== S TABLE (Optimal Split Index k) ==========
i\j       j=1   j=2   j=3   j=4   j=5   j=6
--------------------------------------------------
i=1         -     1     1     3     3     3
i=2         -     -     2     3     3     3
i=3         -     -     -     3     3     3
i=4         -     -     -     -     4     5
i=5         -     -     -     -     -     5
i=6         -     -     -     -     -     -
--------------------------------------------------

========== RESULTS SUMMARY ==========
Number of Matrices           : 6
Optimal Parenthesization     : ((A1(A2A3))((A4A5)A6))
Minimum Scalar Multiplications: 15125
Execution Time               : 35200.00 ns
======================================
```

---

## 📖 Key Takeaways & Conclusion

1. **Exponential Search Space Reduction**:
   - The naive brute-force exhaustive evaluation of all parenthesizations takes Catalan time $\Omega(4^n / n^{3/2})$. Dynamic Programming reduces this to polynomial time $\mathcal{O}(n^3)$.
2. **Optimal Substructure**:
   - Optimal solution to the problem contains optimal solutions to subproblems (evaluating optimal sub-chains $A_i \dots A_k$ and $A_{k+1} \dots A_j$).
