import numpy as np
from math import sqrt

class Data:
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
    sigma: list[float]
    sigma_syst: list[float]
    sigma_rand: float
    sigma: list[float]
    val: list[float]
    val_avg: float

    def __init__(self):
        self.sigma = []

    def calculate_sigma(self) -> None:
        self.calculate_sigma_rand()
        for index in range(len(self.sigma_syst)):
            self.sigma.append(sqrt(self.sigma_rand ** 2 + self.sigma_syst[index] ** 2))

    def calculate_sigma_rand(self) -> None:
        self.val_avg = 0
        self.sigma_rand = 0
        for elem in self.val:
            self.val_avg += elem
        self.val_avg /= len(self.val)
        for elem in self.val:
            self.sigma_rand += (elem - self.val_avg) ** 2
        self.sigma_rand = sqrt(self.sigma_rand) / len(self.val)

    def add_val_with_sigma(self, value, sigma_syst) -> None:
        self.val = value
        self.sigma_syst = sigma_syst

    def get_value(self) -> list[float]:
        return self.val

    def get_error(self) -> list[float]:
        return self.sigma
