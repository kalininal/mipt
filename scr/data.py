import numpy as np

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

    sigma : list[float]
        Список суммарных погрешностей, вычисленных для каждого значения.
    epsilon : list[float]
        Список абсолютных погрешностей, выраженных как доля от значений.
    val : list[float]
        Список значений, для которых рассчитываются погрешности.

    Методы:
    ----------
    get_value() -> list[float]:
        Возвращает список значений.
    get_error() -> list[float]:
        Возвращает список суммарных погрешностей.
    """

    sigma: list[float]
    epsilon: list[float]
    val: list[float]

    def __init__(self):
        self.sigma = []
        self.val = []

    def add_val_with_sigma(self, value, sigma) -> None:
        """
        Устанавливает значения и их погрешности.

        Parameters:
            value (list[float]): Список значений.
            sigma (list[float]): Список погрешностей.
        """
        self.val = value
        self.sigma = sigma

    def calculate_epsilon(self) -> None:
        """
        Рассчитывает абсолютные погрешности (epsilon) как долю от значений.

        Если списки val и sigma имеют разные размеры, выводит сообщение об ошибке.
        """
        if len(self.val) != len(self.sigma):
            print("Error. Different array sizes")
            return
        self.epsilon = []
        for index in range(len(self.val)):
            self.epsilon.append(self.sigma[index] / self.val[index])

    def get_value(self) -> list[float]:
        """
        Возвращает список значений, для которых были рассчитаны погрешности.
        """
        return self.val

    def get_error(self) -> list[float]:
        """
        Возвращает список суммарных погрешностей.
        """
        return self.sigma
