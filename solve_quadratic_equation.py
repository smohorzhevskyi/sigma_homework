from numpy import allclose
from cmath import sqrt


def solve_quadratic_equation(
        b: [int, float],
        c: [int, float],
        a: [int, float] = 1.0
) -> ([complex, float], [complex, float]):
    """Solve quadratic equation."""
    b, c, a = map(lambda x: x if isinstance(x, float) else float(x), (b, c, a))

    discriminant = b ** 2 - 4 * a * c

    if discriminant == 0:
        x1 = x2 = -b / (2 * a)
    else:
        x1 = (-b + sqrt(discriminant)) / (2 * a)
        x2 = (-b - sqrt(discriminant)) / (2 * a)

    return x1, x2


variants = [
    {'b': 4.0, 'c': 3.0},
    {'b': 2.0, 'c': 1.0},
    {'b': 0.5, 'c': 4.0},
    {'b': 1e10, 'c': 3.0},
    {'b': -1e10, 'c': 4.0}
]

for var in variants:
    sol1, sol2 = solve_quadratic_equation(**var)
    print(allclose(sol1 * sol2, var['c']))
