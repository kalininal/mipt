import sys
sys.path.append('/home/kalinin/PycharmProjects/pythonProject/scr')
from scr.linearplot import *
from scr.data import *
from scr.gui import *

gui = Gui()
gui.root.mainloop()

data = gui.get_data()

errors_x = Errors()
errors_y = Errors()
errors_x.add_val_with_sigma(data.get_val_x(), data.get_error_x())
errors_y.add_val_with_sigma(data.get_val_y(), data.get_error_y())
errors_x.calculate_sigma()
errors_y.calculate_sigma()

data.add_list_errors(errors_x.get_error(), errors_y.get_error())

linear_plot(data.get_pair_val(), data.get_pair_error())