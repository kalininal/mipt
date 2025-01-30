import tkinter as tk
from tkinter import ttk
from scr.data import Data

class Gui:
    """
    Класс Gui создает графический интерфейс для ввода значений и погрешностей, которые передаются объекту класса Data.

    Атрибуты:
    ----------
    text1 : list[float]
        Массив для хранения значений x.
    text2 : list[float]
        Массив для хранения значений y.
    text3 : list[float]
        Массив для хранения значений системной погрешности x.
    text4 : list[float]
        Массив для хранения значений системной погрешности y.

    Методы:
    ----------
    __init__():
        Инициализирует интерфейс с текстовыми полями для ввода значений, разделителя и кнопкой для их считывания.
        Создает основные компоненты интерфейса: поля для ввода данных, заголовок и кнопку.

    create_input_field(label_text: str, attr_name: str, height: int):
        Создает и настраивает текстовое поле для ввода значений с меткой, сохраняет ссылку на него в атрибутах класса.

    get_text_to_data():
        Считывает значения из текстовых полей, разделяет их по заданному разделителю и сохраняет в массивы text1, text2, text3, text4.
        После считывания закрывает главное окно.

    get_data() -> Data:
        Создает и возвращает объект класса Data, добавляя в него считанные значения x, y и их погрешности.
    """

    text1: list[float]
    text2: list[float]
    text3: list[float]
    text4: list[float]

    def __init__(self):
        # Создаем главное окно
        self.root = tk.Tk()
        self.root.title("Умный обработчик данных")
        self.root.configure(bg="#f5f5f5")

        # Создаем стиль для элементов интерфейса
        style = ttk.Style()
        style.configure("TLabel", background="#f5f5f5", font=("Arial", 10))
        style.configure("TButton", font=("Arial", 10), background="#4682B4", foreground="white")
        style.map("TButton", background=[("active", "#5B9BD5")])

        # Заголовок интерфейса
        title_label = ttk.Label(self.root, text="Введите данные и погрешности", font=("Arial", 14, "bold"), background="#4682B4", foreground="white", padding=10)
        title_label.pack(fill="x", pady=(0, 10))

        # Поле для ввода разделителя
        frame_sep = tk.Frame(self.root, bg="#f5f5f5")
        frame_sep.pack(pady=(10, 5))
        ttk.Label(frame_sep, text="Разделитель: ").pack(side="left")
        self.text_box_sep = ttk.Entry(frame_sep, width=10)
        self.text_box_sep.pack(side="left", padx=5)

        # Поля для ввода значений и погрешностей
        self.create_input_field("Введите значения x:", "x", 3)
        self.create_input_field("Введите значения y:", "y", 3)
        self.create_input_field("Погрешность x:", "error_x", 3)
        self.create_input_field("Погрешность y:", "error_y", 3)

        # Кнопка для считывания текста
        self.button = ttk.Button(self.root, text="Построить график", command=self.get_text_to_data)
        self.button.pack(pady=15)

    def create_input_field(self, label_text, attr_name, height):
        """
        Создает поле ввода с меткой и текстовой областью.

        Parameters:
            label_text (str): Текст для метки.
            attr_name (str): Имя атрибута, в котором будет храниться ссылка на текстовое поле.
            height (int): Высота текстового поля.
        """
        frame = tk.Frame(self.root, bg="#f5f5f5")
        frame.pack(pady=(5, 10))
        ttk.Label(frame, text=label_text).pack(anchor="w")
        text_box = tk.Text(frame, height=height, width=40, wrap="word", font=("Arial", 10))
        text_box.pack(pady=5)
        setattr(self, f"text_box_{attr_name}", text_box)

    def get_text_to_data(self):
        """
        Считывает значения из текстовых полей, разделяет их по указанному разделителю и сохраняет в массивы text1, text2, text3, text4.
        """
        # Получаем разделитель из текстового поля и проверяем, чтобы он не был пустым
        separator = self.text_box_sep.get().strip() or " "

        # Считываем и преобразуем текстовые данные в числовые значения
        self.text1 = list(map(float, self.text_box_x.get("1.0", tk.END).strip().split(separator)))
        self.text2 = list(map(float, self.text_box_y.get("1.0", tk.END).strip().split(separator)))
        self.text3 = list(map(float, self.text_box_error_x.get("1.0", tk.END).strip().split(separator)))
        self.text4 = list(map(float, self.text_box_error_y.get("1.0", tk.END).strip().split(separator)))

        # Закрываем главное окно после считывания данных
        self.root.destroy()

    def get_data(self) -> Data:
        """
        Создает и возвращает объект Data, в который добавляются введенные значения и погрешности.
        """
        data = Data()
        data.add_list_vals(self.text1, self.text2)
        data.add_list_errors(self.text3, self.text4)
        return data