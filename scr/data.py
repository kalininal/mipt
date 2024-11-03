import numpy as np
from math import sqrt

class Data:
    """
    Класс Data представляет данные для эксперимента, включая значения x и y, а также их системные погрешности.

    Атрибуты:
    ----------
    val_x : list[float]
        Список значений переменной x.
    val_y : list[float]
        Список значений переменной y.
    error_x : list[float]
        Список системных погрешностей для значений x.
    error_y : list[float]
        Список системных погрешностей для значений y.

    Методы:
    ----------
    add_var_and_error(x: float, y: float, err_x: float, err_y: float) -> None:
        Добавляет значение переменных x, y и их погрешностей в соответствующие списки.
    del_var_and_error(var_id: int) -> None:
        Удаляет значение переменных и их погрешностей по индексу.
    add_list_vals(vals_x: list[float], vals_y: list[float]) -> None:
        Устанавливает списки значений x и y.
    add_list_errors(errors_x: list[float], errors_y: list[float]) -> None:
        Устанавливает списки погрешностей x и y.
    get_pair_val() -> np.array:
        Возвращает массив пар значений (x, y).
    get_pair_error() -> np.array:
        Возвращает массив пар погрешностей (error_x, error_y).
    get_val_x() -> list[float]:
        Возвращает список значений x.
    get_val_y() -> list[float]:
        Возвращает список значений y.
    get_error_x() -> list[float]:
        Возвращает список погрешностей x.
    get_error_y() -> list[float]:
        Возвращает список погрешностей y.
    """

    val_x: list[float]
    val_y: list[float]
    error_x: list[float]
    error_y: list[float]

    def __init__(self):
        self.val_x = []
        self.val_y = []
        self.error_x = []
        self.error_y = []

    def add_var_and_error(self, x: float, y: float, err_x: float, err_y: float) -> None:
        """
        Удаляет значения переменных и их погрешностей по индексу var_id.
        """
        self.val_x.append(x)
        self.val_y.append(y)
        self.error_x.append(err_x)
        self.error_y.append(err_y)

    def del_var_and_error(self, var_id: int) -> None:
        self.val_x.remove(var_id)
        self.val_y.remove(var_id)
        self.error_x.remove(var_id)
        self.error_y.remove(var_id)

    def add_list_vals(self, vals_x: list[float], vals_y: list[float]) -> None:
        self.val_x = vals_x
        self.val_y = vals_y

    def add_list_errors(self, errors_x: list[float], errors_y: list[float]) -> None:
        self.error_x = errors_x
        self.error_y = errors_y

    def get_pair_val(self) -> np.array(list[float]):
        return np.array(list(zip(self.val_x, self.val_y)))

    def get_pair_error(self) -> np.array(list[float]):
        return np.array(list(zip(self.error_x, self.error_y)))

    def get_val_x(self) -> list[float]:
        return self.val_x

    def get_val_y(self) -> list[float]:
        return self.val_y

    def get_error_x(self) -> list[float]:
        return self.error_x

    def get_error_y(self) -> list[float]:
        return self.error_y

class Errors:
    """
    Класс Errors используется для расчета общих погрешностей измерений, включая системные и случайные погрешности.

    Атрибуты:
    ----------
    sigma : list[float]
        Список суммарных погрешностей, вычисленных для каждого значения.
    sigma_syst : list[float]
        Список системных погрешностей.
    sigma_rand : float
        Случайная погрешность, рассчитанная для значений.
    val : list[float]
        Список значений, для которых рассчитываются погрешности.
    val_avg : float
        Среднее значение val, рассчитанное для расчета случайной погрешности.

    Методы:
    ----------
    calculate_sigma() -> None:
        Вычисляет суммарную погрешность для каждого значения, комбинируя системную и случайную погрешности.
    calculate_sigma_rand() -> None:
        Вычисляет случайную погрешность на основе среднего квадратичного отклонения значений.
    add_val_with_sigma(value: list[float], sigma_syst: list[float]) -> None:
        Устанавливает значения и соответствующие системные погрешности.
    get_value() -> list[float]:
        Возвращает список значений.
    get_error() -> list[float]:
        Возвращает список суммарных погрешностей.
    """

    sigma: list[float]
    sigma_syst: list[float]
    sigma_rand: float
    sigma: list[float]
    val: list[float]
    val_avg: float

    def __init__(self):
        self.sigma = []

    def calculate_sigma(self) -> None:
        """
        Вычисляет общую погрешность для каждого значения, используя формулу:
        sigma = sqrt(sigma_rand^2 + sigma_syst^2).
        """
        self.calculate_sigma_rand()
        for index in range(len(self.sigma_syst)):
            self.sigma.append(sqrt(self.sigma_rand ** 2 + self.sigma_syst[index] ** 2))

    def calculate_sigma_rand(self) -> None:
        """
        Вычисляет случайную погрешность на основе среднеквадратичного отклонения значений от среднего.
        """
        self.val_avg = 0
        self.sigma_rand = 0
        for elem in self.val:
            self.val_avg += elem
        self.val_avg /= len(self.val)
        for elem in self.val:
            self.sigma_rand += (elem - self.val_avg) ** 2
        self.sigma_rand = sqrt(self.sigma_rand) / len(self.val)

    def add_val_with_sigma(self, value, sigma_syst) -> None:
        """
        Устанавливает значения и их системные погрешности.

        Parameters:
            value (list[float]): Список значений.
            sigma_syst (list[float]): Список системных погрешностей.
        """
        self.val = value
        self.sigma_syst = sigma_syst

    def get_value(self) -> list[float]:
        return self.val

    def get_error(self) -> list[float]:
        return self.sigma
