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
# Metode Newton-Raphson
def newton(x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            print("Turunan nol, tidak bisa lanjut")
            return None
        x_new = x - fx / dfx
        print(f"Newton Iter {i+1}: x = {x_new}, f(x) = {f(x_new)}")
        if abs(f(x_new)) < tol:
            return x_new
        x = x_new
    return x

# Metode Secant
def secant(x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f0, f1 = f(x0), f(x1)
        if f1 - f0 == 0:
            print("Denominator nol, tidak bisa lanjut")
            return None
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        print(f"Secant Iter {i+1}: x = {x2}, f(x) = {f(x2)}")
        if abs(f(x2)) < tol:
            return x2
        x0, x1 = x1, x2
    return x2

# Bagian main untuk eksekusi langsung
if __name__ == "__main__":
    print("=== Metode Bisection ===")
    root_bis = bisection(0, 2)
    print(f"Akar Bisection: {root_bis}\n")

    print("=== Metode Newton-Raphson ===")
    root_newton = newton(1.0)  # tebakan awal
    print(f"Akar Newton-Raphson: {root_newton}\n")

    print("=== Metode Secant ===")
    root_secant = secant(0, 2)  # dua tebakan awal
    print(f"Akar Secant: {root_secant}")