import numpy as np
import matplotlib.pyplot as plt

# Data dari Example 3
x = np.array([0,1,2,3,4,5])
y = np.array([2.1,7.7,13.6,27.2,40.9,61.1])
# Linear regression y=a0​+a1​x
coeff_linear = np.polyfit(x, y, 1)
y_linear = np.polyval(coeff_linear, x)

print("Linear Coeff:", coeff_linear)
# Polynomial orde 2 y=a0​+a1​x+a2x​^2
coeff_poly = np.polyfit(x, y, 2)
y_poly = np.polyval(coeff_poly, x)

print("Polynomial Coeff:", coeff_poly)
# Nonlinear (eksponensial) y=ae^bx
log_y = np.log(y)

coeff_exp = np.polyfit(x, log_y, 1)
a = np.exp(coeff_exp[1])
b = coeff_exp[0]

y_exp = a * np.exp(b * x)

print("Nonlinear (exp): a =", a, "b =", b)
plt.scatter(x, y, color='black', label='Data Asli')

plt.plot(x, y_linear, label='Linear Fit')
plt.plot(x, y_poly, label='Polynomial Fit')
plt.plot(x, y_exp, label='Nonlinear Fit')

plt.legend()
plt.title("Least Squares Comparison")
plt.xlabel("x")
plt.ylabel("y")

plt.show()