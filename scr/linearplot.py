import numpy as np
import matplotlib.pyplot as plt

def linear_plot(points: np.array(list[float]), errors: np.array(list[float])) -> None:

    # Разделение на x и y
    x_coords = points[:, 0]
    y_coords = points[:, 1]
    dy = errors[:, 1]  # вертикальные погрешности
    dx = errors[:, 0]  # горизонтальные погрешности

    # Использование вертикальных погрешностей как весов
    weights = 1 / dy**2

    # Линейная регрессия с использованием весов
    A = np.vstack([x_coords, np.ones(len(x_coords))]).T
    W = np.diag(weights)
    Theta = np.linalg.inv(A.T @ W @ A) @ (A.T @ W @ y_coords)
    a, b = Theta

    # Вычисление ошибок параметров
    C = np.linalg.inv(A.T @ W @ A)
    a_error = np.sqrt(C[0, 0])
    b_error = np.sqrt(C[1, 1])

    # Построение прямой
    y_fit = a * x_coords + b

    # Настройка графика
    plt.errorbar(x_coords, y_coords, xerr=dx, yerr=dy, fmt='o', label='Точки с погрешностями')
    plt.plot(x_coords, y_fit, 'r-', label=f'Линейная регрессия\na = {a:.3f} +- {a_error:.3f}, b = {b:.3f} +- {b_error:.3f}')
    plt.title('График с погрешностями и линейной регрессией')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid()


    # Точка пересечения с осью OX
    x_intercept = -b / a
    x_intercept_error = np.sqrt((b_error / a) ** 2 + (b * a_error / a ** 2) ** 2)

    print(a_error, b_error)
    print(f"Точка пересечения с осью OX (x-перехват): {x_intercept:.6f}")
    print(f"Погрешность x-перехвата: {x_intercept_error:.6f}")
    plt.show()
