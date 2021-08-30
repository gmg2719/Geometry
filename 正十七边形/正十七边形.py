import sympy as sp

x = sp.symbols("x")
"""
A=1
B=8
C=8
"""


def cos(a, b, c):
    return (a * a + b * b - c * c) / (2 * a * b)


cosA = cos(x, x, 1)
sinA = sp.sqrt(1 - cosA ** 2)
cosB = cos(x, 1, x)
cos2A = cosA ** 2 - sinA ** 2
sin2A = sp.sqrt(1 - cos2A ** 2)
cos4A = cos2A ** 2 - sin2A ** 2
sin4A = 2 * sin2A * cos2A
cos8A = cos4A ** 2 - sin4A ** 2
f = cos8A - cosB
f = f.simplify()
print(f)
print("=======")
ans = sp.solve(f, x)
print(ans)
