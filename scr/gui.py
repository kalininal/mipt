import tkinter as tk
from data import *

class Gui:
    def __init__(self):
        # Создаем главное окно
        self.root = tk.Tk()
        self.root.title("Считывание текста из полей")

        # Создаем пять текстовых полей
        self.label_sep = tk.Label(self.root, text="Введите разделитель")
        self.label_sep.pack()
        self.text_box_sep = tk.Text(self.root, height=1, width=10)
        self.text_box_sep.pack(pady=5)

        self.label_x = tk.Label(self.root, text="Введите значение x")
        self.label_x.pack()
        self.text_box1 = tk.Text(self.root, height=3, width=40)
        self.text_box1.pack(pady=5)

        self.label_y = tk.Label(self.root, text="Введите значение y")
        self.label_y.pack()
        self.text_box2 = tk.Text(self.root, height=3, width=40)
        self.text_box2.pack(pady=5)

        self.label_error_x = tk.Label(self.root, text="Введите значение системной погрешности x")
        self.label_error_x.pack()
        self.text_box3 = tk.Text(self.root, height=3, width=40)
        self.text_box3.pack(pady=5)

        self.label_error_y = tk.Label(self.root, text="Введите значение системной погрешности y")
        self.label_error_y.pack()
        self.text_box4 = tk.Text(self.root, height=3, width=40)
        self.text_box4.pack(pady=5)

        # Создаем кнопку для считывания текста
        self.button = tk.Button(self.root, text="Считать текст", command=self.get_text_to_data)
        self.button.pack(pady=10)

    def get_text_to_data(self):
        separator = str(self.text_box_sep.get("1.0", tk.END).strip())
        if separator == '':
            separator = ' '
        self.text1 = list(map(float, self.text_box1.get("1.0", tk.END).strip().split(separator)))
        self.text2 = list(map(float, self.text_box2.get("1.0", tk.END).strip().split(separator)))
        self.text3 = list(map(float, self.text_box3.get("1.0", tk.END).strip().split(separator)))
        self.text4 = list(map(float, self.text_box4.get("1.0", tk.END).strip().split(separator)))

    def get_data(self) -> Data:
        # Считываем содержимое из каждого текстового поля
        data = Data()
        data.add_list_vals(self.text1, self.text2)
        data.add_list_errors(self.text3, self.text4)
        return data