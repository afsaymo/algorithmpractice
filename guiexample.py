import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Algorithms with awwwwdri")

        root = QLineEdit()
        root.setMaxLength(1)
        root.setPlaceholderText("Enter root")
        #self.setCentralWidget(root)

        branches= QLineEdit()
        branches.setMaxLength(10)
        branches.setPlaceholderText("Enter branches for root")

        widgets = [
            root,
            branches
        ]

        layout =   QVBoxLayout()
        for w in widgets:
            layout.addWidget(w())

        #self.setMenuWidget(branches)
        #button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the Window.
        #self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
