import numpy as np

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

    def get_pair_val(self) -> np.array(list[float]):
        return np.array(list(zip(self.val_x, self.val_y)))

    def get_pair_error(self) -> np.array(list[float]):
        return np.array(list(zip(self.error_x, self.error_y)))
