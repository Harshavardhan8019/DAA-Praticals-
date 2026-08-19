# Practical 4: Factorial Calculation (Iterative vs. Recursive Analysis)

This directory contains the Python implementation of **Factorial Calculation** using both **Iterative** and **Recursive** approaches. The program computes the factorial for non-negative integers using both paradigms, compares their performance, and measures execution time with high precision using `time.perf_counter()`.

---

## 📌 Factorial Concept & Paradigms

The factorial of a non-negative integer $n$, denoted by $n!$, is the product of all positive integers less than or equal to $n$:

$$n! = \begin{cases} 1 & \text{if } n = 0 \text{ or } n = 1 \\ n \times (n-1) \times (n-2) \times \dots \times 1 & \text{if } n > 1 \end{cases}$$

### Methods Implemented

1. **Iterative Method (`factorial_iterative(n)`)**
   - Uses an explicit loop running from $1$ to $n$ to incrementally compute the running product.
   - **Time Complexity:** $O(n)$
   - **Space Complexity:** $O(1)$ (constant space, no call stack overhead).

2. **Recursive Method (`factorial_recursive(n)`)**
   - Expresses the problem in terms of itself using the recurrence relation $T(n) = T(n-1) + O(1)$, with base cases $0! = 1$ and $1! = 1$.
   - **Time Complexity:** $O(n)$
   - **Space Complexity:** $O(n)$ (due to function call stack frames).

---

## ⚡ Complexity Summary

| Approach | Best Case | Average Case | Worst Case | Auxiliary Space Complexity | Paradigm |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Iterative Method** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Iterative Accumulation |
| **Recursive Method** | $\mathcal{O}(1)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ (Call Stack) | Divide & Conquer / Decrease & Conquer |

---

## 💻 How to Run

1. Open your terminal or command prompt.
2. Navigate to the `practical_4` directory:
   ```bash
   cd practical_4
   ```
3. Run the Python script:
   ```bash
   python factorial.py
   ```

---

## 📋 Sample Input & Output

### Example 1 (Standard Positive Input):
```text
Enter a number: 5

Factorial using Iterative Method: 120
Factorial using Recursive Method: 120

Execution Time: 0.00004520 seconds
```

### Example 2 (Base Case):
```text
Enter a number: 0

Factorial using Iterative Method: 1
Factorial using Recursive Method: 1

Execution Time: 0.00002130 seconds
```

### Example 3 (Negative Input):
```text
Enter a number: -5
Factorial is not defined for negative numbers.
```

---

## 📖 Summary
This practical demonstrates two fundamental programming paradigms—iteration and recursion—to solve the factorial problem in Python. While both achieve a linear $O(n)$ time complexity, the iterative approach avoids the additional $O(n)$ call stack space overhead incurred by recursion.

## 🎯 Conclusion
- **Iterative Approach**: Highly efficient in terms of memory utilization ($O(1)$ auxiliary space) and immune to recursion depth limits.
- **Recursive Approach**: Provides clean, expressive mathematical formulation mirroring inductive definitions, but introduces stack frame overhead proportional to $n$.
