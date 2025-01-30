from scr.linearplot import linear_plot
from scr.data import Data, Errors
from scr.gui import Gui

def main():
    # Создаём интерфейс
    gui = Gui()
    gui.root.mainloop()

    # Импортируем дату
    data = gui.get_data()

    # Обрабатываем данные
    errors_x = Errors()
    errors_y = Errors()
    errors_x.add_val_with_sigma(data.get_val_x(), data.get_error_x())
    errors_y.add_val_with_sigma(data.get_val_y(), data.get_error_y())

    data.add_list_errors(errors_x.get_error(), errors_y.get_error())

    # Строим график
    linear_plot(data.get_pair_val(), data.get_pair_error())

if __name__ == "__main__":
    main()
