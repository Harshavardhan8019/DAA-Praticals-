import time

INF = float('inf')


def matrix_chain_order(dimensions):
    """
    Dynamic Programming solution for Matrix Chain Multiplication.
    
    Given a sequence of matrices A1, A2, ..., An with dimensions defined by 
    array p where matrix Ai has dimension p[i-1] x p[i], computes the minimum 
    number of scalar multiplications needed to compute the product A1..An.
    
    Time Complexity: O(n^3)
    Space Complexity: O(n^2)
    
    :param dimensions: List of matrix dimensions where Ai is dimensions[i-1] x dimensions[i]
    :return: (m_table, s_table, min_cost)
    """
    n = len(dimensions) - 1  # Number of matrices
    # m[i][j] stores minimum cost of multiplying Ai..Aj
    m = [[0] * (n + 1) for _ in range(n + 1)]
    # s[i][j] stores index k where optimal split occurs Ai..Ak * Ak+1..Aj
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # L is chain length
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = INF
            for k in range(i, j):
                # q = cost/scalar multiplications
                q = m[i][k] + m[k + 1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s, m[1][n]


def get_optimal_parenthesization(s, i, j):
    """
    Constructs the string representation of optimal matrix parenthesization.
    """
    if i == j:
        return f"A{i}"
    else:
        left = get_optimal_parenthesization(s, i, s[i][j])
        right = get_optimal_parenthesization(s, s[i][j] + 1, j)
        return f"({left}{right})"


def print_dp_tables(dimensions, m, s):
    """Prints formatted m (cost) and s (split) DP tables."""
    n = len(dimensions) - 1
    print("\n========== M TABLE (Minimum Scalar Multiplications) ==========")
    header = f"{'i\\j':<6}" + "".join([f"{'j=' + str(j):>8}" for j in range(1, n + 1)])
    print(header)
    print("-" * len(header))
    for i in range(1, n + 1):
        row = f"i={i:<4}"
        for j in range(1, n + 1):
            if j < i:
                row += f"{'-':>8}"
            else:
                row += f"{m[i][j]:>8}"
        print(row)
    print("-" * len(header))

    print("\n========== S TABLE (Optimal Split Index k) ==========")
    print(header)
    print("-" * len(header))
    for i in range(1, n + 1):
        row = f"i={i:<4}"
        for j in range(1, n + 1):
            if j <= i:
                row += f"{'-':>8}"
            else:
                row += f"{s[i][j]:>8}"
        print(row)
    print("-" * len(header))


def main():
    print("==================================================")
    print("   MATRIX CHAIN MULTIPLICATION (DYNAMIC PROGRAMMING)")
    print("==================================================")

    # Default dimensions: Matrix A1(10x30), A2(30x5), A3(5x60), A4(60x10), A5(10x20), A6(20x25)
    default_dims = [10, 30, 5, 60, 10, 20, 25]

    print("Default Matrix Dimensions Sequence p:")
    print(f"  p = {default_dims}")
    for i in range(1, len(default_dims)):
        print(f"  - Matrix A{i}: {default_dims[i-1]} x {default_dims[i]}")

    user_choice = input("\nUse custom input? (y/N): ").strip().lower()
    if user_choice == 'y':
        try:
            dims_str = input("Enter dimension array p separated by spaces (e.g. 10 30 5 60): ")
            dimensions = list(map(int, dims_str.split()))
            if len(dimensions) < 2:
                raise ValueError("Need at least 2 dimensions for 1 matrix")
        except Exception as e:
            print(f"Invalid input ({e})! Falling back to default dimensions.")
            dimensions = default_dims
    else:
        dimensions = default_dims

    n = len(dimensions) - 1
    print("\n--- Running Dynamic Programming Matrix Chain Order ---")
    start_time = time.perf_counter()
    m_table, s_table, min_cost = matrix_chain_order(dimensions)
    end_time = time.perf_counter()
    execution_time_ns = (end_time - start_time) * 1e9

    print_dp_tables(dimensions, m_table, s_table)

    optimal_paren = get_optimal_parenthesization(s_table, 1, n)

    print("\n========== RESULTS SUMMARY ==========")
    print(f"Number of Matrices           : {n}")
    print(f"Optimal Parenthesization     : {optimal_paren}")
    print(f"Minimum Scalar Multiplications: {min_cost}")
    print(f"Execution Time               : {execution_time_ns:.2f} ns")
    print("======================================")


if __name__ == "__main__":
    main()
