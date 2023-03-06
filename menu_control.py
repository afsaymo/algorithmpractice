from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QPushButton,
    QSizePolicy, QWidget)

"""A simple widget where the user selects their preferred search algorithm, 
start and end nodes
"""
# this is where we control the algMenu
class menu_controller(QWidget):
    """A widget that allows the user to select a BFS/DFS search, start, and end points

    The widget has a combobox on the top to select which algorithm to use, followed by 
    2 comboboxes-- one labeled start one labeled end-- each containing selections A, B,
    C, or D. Below those two comboboxes is the Begin to begin the search
    """
    def __init__(self, parent = None):
        """Create a new :class: 'menu_controller' widget
        """
        super().__init__(parent)
        self.setupUi(self)
        
# make buttons

# get algorithm selection 

# make combobox for start

# combobox for end

# get values from start and end

# put them into the algorithm and return