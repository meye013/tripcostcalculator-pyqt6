import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QComboBox,QVBoxLayout,QWidget,QHBoxLayout)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        layout = QVBoxLayout()

        btnlayout = QVBoxLayout()

        layout.addLayout(btnlayout)

        layout.addWidget(QPushButton("Push Me"))

        Botton = QPushButton("Push Me")
        Botton.layout = (btnlayout)
        self.setCentralWidget(Botton)
        Botton.setFixedSize(QSize(100,50))

        self.setFixedSize(QSize(300,300))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()