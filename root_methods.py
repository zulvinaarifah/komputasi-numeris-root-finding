# root_methods.py

# Fungsi utama
def f(x):
    return x**3 - 3*x**2 + 1

# Turunan untuk Newton (nanti bisa dipakai jika ingin Newton-Raphson)
def df(x):
    return 3*x**2 - 6*x

# Metode Bisection
def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        print("Interval tidak memenuhi syarat!")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        print(f"Iterasi {i+1}: c = {c}, f(c) = {f(c)}")

        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

# Bagian ini hanya dijalankan kalau file dijalankan langsung
if __name__ == "__main__":
    print("=== Metode Bisection ===")
    a = 0
    b = 2
    root = bisection(a, b)
    if root is not None:
        print(f"Akar ditemukan: {root}")
    else:
        print("Tidak ditemukan akar pada interval ini.")