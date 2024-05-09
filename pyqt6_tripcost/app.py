import sys
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QDoubleSpinBox, QVBoxLayout ,QWidget ,QHBoxLayout, QLabel, QLayout)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        self.setContentsMargins(12,12,12,12)
        self.resize(500,300)
        
        self.main = QWidget()
        self.main_layout = QHBoxLayout()
        self.main.setLayout(self.main_layout)
        self.setCentralWidget(self.main)
        
        self.left_panel = QWidget()
        self.left_panel_layout = QVBoxLayout()
        self.left_panel.setLayout(self.left_panel_layout)
        self.main_layout.addWidget(self.left_panel_layout)

        self.right_panel = QWidget()
        self.right_panel_layout = QVBoxLayout()
        self.right_panel.setLayout(self.right_panel_layout)
        self.main_layout.addWidget(self.right_panel_layout)

        self.title = QLabel("Trip Cost Calculator")
        self.main_layout.addWidget(self.title)
        font = self.title.font()
        font.setPointSize(30)
        self.title.setFont(font)


        


app = QApplication(sys.argv)
app.setStyle("Fusion")
window = MainWindow()
window.show()

app.exec()