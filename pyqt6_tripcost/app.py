import sys
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QDoubleSpinBox, QVBoxLayout ,QWidget ,QHBoxLayout, QLabel, QLayout, QGridLayout)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        self.setContentsMargins(12,12,12,12)
        self.resize(200,350)
        
        self.main = QWidget()
        self.main_layout = QGridLayout()
        self.main.setLayout(self.main_layout)
        self.setCentralWidget(self.main)

        #Title
        
        self.title = QLabel("Trip Cost Calculator")
        self.main_layout.addWidget(self.title, 0, 0)
        font = self.title.font()
        font.setPointSize(20)
        self.title.setFont(font)

        #Spinbox Inputs

        self.gasprice_input = QDoubleSpinBox()
        self.main_layout.addWidget(self.gasprice_input, 1, 0)        

        self.tripdistance_input = QDoubleSpinBox()
        self.main_layout.addWidget(self.tripdistance_input, 2, 0)        

        self.fuelefficiency_input = QDoubleSpinBox()
        self.main_layout.addWidget(self.fuelefficiency_input, 3, 0)        

        #Spinbox Prefixes

        self.gasprice_input.setPrefix("Gas Price = ")
        self.tripdistance_input.setPrefix("Trip Distance = ")
        self.fuelefficiency_input.setPrefix("Fuel efficiency = ")

        #Pushbuttons
        self.calculate_button = QPushButton("Calculate")
        self.main_layout.addWidget(self.calculate_button, 5, 0)
        
        self.reset_button = QPushButton("Reset")
        self.main_layout.addWidget(self.reset_button, 6, 0)

        


app = QApplication(sys.argv)
app.setStyle("Fusion")
window = MainWindow()
window.show()

app.exec()