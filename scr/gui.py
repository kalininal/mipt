import tkinter as tk
from data import *

class Gui:
    """
    Класс Gui создает графический интерфейс для ввода значений, которые можно считывать и передавать в объект класса Data.

    Атрибуты:
    ----------
    text1 : list
        Массив для хранения значений x.
    text2 : list
        Массив для хранения значений y.
    text3 : list
            Массив для хранения значений системной погрешности x.
    text4 : list
       Массив для хранения значений системной погрешности y.

    Методы:
    ----------
    __init__():
        Инициализирует интерфейс с текстовыми полями для ввода значений и кнопкой для их считывания.
    get_text_to_data():
        Считывает введенные значения из текстовых полей, разделяет их по заданному разделителю и сохраняет в соответствующие массивы.
    get_data() -> Data:
        Возвращает объект Data с введенными значениями и погрешностями.
    """
    # Массивы для импорта сырых данных

    text1: list[float]
    text2: list[float]
    text3: list[float]
    text4: list[float]

    def __init__(self):
        # Создаем главное окно
        self.root = tk.Tk()
        self.root.title("Умный обработчик данных лаб")

        # Создаем поле для ввода разделителя
        self.label_sep = tk.Label(self.root, text="Введите разделитель")
        self.label_sep.pack()
        self.text_box_sep = tk.Text(self.root, height=1, width=10)
        self.text_box_sep.pack(pady=5)

        # Создаем текстовое поле для ввода значений x
        self.label_x = tk.Label(self.root, text="Введите значение x")
        self.label_x.pack()
        self.text_box1 = tk.Text(self.root, height=3, width=40)
        self.text_box1.pack(pady=5)

        # Создаем текстовое поле для ввода значений y
        self.label_y = tk.Label(self.root, text="Введите значение y")
        self.label_y.pack()
        self.text_box2 = tk.Text(self.root, height=3, width=40)
        self.text_box2.pack(pady=5)

        # Создаем текстовое поле для ввода системной погрешности x
        self.label_error_x = tk.Label(self.root, text="Введите значение системной погрешности x")
        self.label_error_x.pack()
        self.text_box3 = tk.Text(self.root, height=3, width=40)
        self.text_box3.pack(pady=5)

        # Создаем текстовое поле для ввода системной погрешности y
        self.label_error_y = tk.Label(self.root, text="Введите значение системной погрешности y")
        self.label_error_y.pack()
        self.text_box4 = tk.Text(self.root, height=3, width=40)
        self.text_box4.pack(pady=5)

        # Создаем кнопку для считывания текста
        self.button = tk.Button(self.root, text="Построить график", command=self.get_text_to_data)
        self.button.pack(pady=10)

    def get_text_to_data(self):
        """
            Считывает значения из текстовых полей, разделяет их по указанному разделителю и сохраняет в массивы text1, text2, text3, text4.
        """
        # Получаем разделитель из текстового поля и проверяем, чтобы он не был пустым
        separator = str(self.text_box_sep.get("1.0", tk.END).strip())
        if separator == '':
            separator = ' '

        # Считываем и преобразуем текстовые данные в числовые значения
        self.text1 = list(map(float, self.text_box1.get("1.0", tk.END).strip().split(separator)))
        self.text2 = list(map(float, self.text_box2.get("1.0", tk.END).strip().split(separator)))
        self.text3 = list(map(float, self.text_box3.get("1.0", tk.END).strip().split(separator)))
        self.text4 = list(map(float, self.text_box4.get("1.0", tk.END).strip().split(separator)))

        # Закрываем главное окно после считывания данных
        self.root.destroy()

    def get_data(self) -> Data:
        """
            Создает и возвращает объект Data, в который добавляются введенные значения и погрешности.

            Returns:
                Data: Объект с введенными значениями x, y и их погрешностями.
        """

        data = Data()
        data.add_list_vals(self.text1, self.text2) # Добавляем значения x и y
        data.add_list_errors(self.text3, self.text4) # Добавляем погрешности x и y
        return data