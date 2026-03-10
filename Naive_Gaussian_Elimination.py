# Naive_Gaussian_Elimination
# Forward Elimination + Backward Substitution
# =========================================================
# Metode untuk menyelesaikan sistem persamaan linear AX = B
# Tahapan:
# 1. Forward Elimination -> membentuk matriks segitiga atas
# 2. Backward Substitution -> menghitung solusi variabel
# =========================================================

def print_system(A, b):
    """Menampilkan sistem persamaan dalam bentuk matriks"""
    n = len(A)
    for i in range(n):
        print(A[i], "|", b[i])
    print()


def forward_elimination(A, b):
    """
    Tahap Forward Elimination
    Mengubah matriks A menjadi bentuk upper triangular
    """
    n = len(A)

    for k in range(n-1):   # loop untuk pivot
        print("Pivot Step", k+1)
        print("Pivot element =", A[k][k])

        for i in range(k+1, n):

            # menghitung faktor eliminasi
            factor = A[i][k] / A[k][k]

            print("Eliminasi baris", i+1, "dengan faktor =", factor)

            for j in range(k+1, n):
                A[i][j] = A[i][j] - factor * A[k][j]

            # update vektor b
            b[i] = b[i] - factor * b[k]

            # elemen di bawah pivot menjadi 0
            A[i][k] = 0

        print("Matriks setelah eliminasi:")
        print_system(A, b)


def backward_substitution(A, b):
    """
    Tahap Backward Substitution
    Menghitung solusi variabel mulai dari xn sampai x1
    """
    n = len(A)
    x = [0]*n

    # menghitung xn terlebih dahulu
    x[n-1] = b[n-1] / A[n-1][n-1]
    print("x", n, "=", x[n-1])

    # menghitung variabel lainnya
    for i in range(n-2, -1, -1):

        sum_val = b[i]

        for j in range(i+1, n):
            sum_val = sum_val - A[i][j] * x[j]

        x[i] = sum_val / A[i][i]

        print("x", i+1, "=", x[i])

    return x


# =========================================================
# PROGRAM UTAMA
# =========================================================

# contoh sistem persamaan linear
# 2x1 - x2 + x3 = 2
# 3x1 + 3x2 + 9x3 = -1
# 3x1 + 3x2 + 5x3 = 4

A = [
    [2, -1, 1],
    [3, 3, 9],
    [3, 3, 5]
]

b = [2, -1, 4]

print("Sistem Persamaan Awal:")
print_system(A, b)

# tahap eliminasi
forward_elimination(A, b)

# tahap mencari solusi
print("Backward Substitution:")
solution = backward_substitution(A, b)

print("\nSolusi akhir:")
print(solution)