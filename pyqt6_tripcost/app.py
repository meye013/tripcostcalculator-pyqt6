import sys
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QDoubleSpinBox, QVBoxLayout ,QWidget ,QHBoxLayout, QLabel, QLayout, QGridLayout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        self.setContentsMargins(12,12,12,12)
        self.resize(200,330)
        
        self.main = QWidget()
        self.main_layout = QGridLayout()
        self.main.setLayout(self.main_layout)
        self.setCentralWidget(self.main)

        #title
        
        self.title = QLabel("Trip Cost Calculator")
        self.main_layout.addWidget(self.title, 0, 0)

        #spinbox Inputs

        self.gasprice_input = QDoubleSpinBox()
        self.main_layout.addWidget(self.gasprice_input, 1, 0)        

        self.tripdistance_input = QDoubleSpinBox()
        self.main_layout.addWidget(self.tripdistance_input, 2, 0)        

        self.fuelefficiency_input = QDoubleSpinBox()
        self.main_layout.addWidget(self.fuelefficiency_input, 3, 0)        

        #spinbox prefixes

        self.gasprice_input.setPrefix("Gas Price = ")
        self.tripdistance_input.setPrefix("Trip Distance = ")
        self.fuelefficiency_input.setPrefix("Fuel efficiency = ")

        #spinbox suffixes

        self.gasprice_input.setSuffix(" gal")
        self.tripdistance_input.setSuffix(" mi")
        self.fuelefficiency_input.setSuffix(" mpgs")

        #pushbuttons

        self.calculate_button = QPushButton("Calculate")
        self.main_layout.addWidget(self.calculate_button, 5, 0)
        
        self.reset_button = QPushButton("Reset")
        self.main_layout.addWidget(self.reset_button, 6, 0)

        #outputs

        self.tripcost_output = QLabel("tripcostlabel")
        self.main_layout.addWidget(self.tripcost_output, 8, 0)
        
        self.gallons_needed = QLabel("gallonlabel")
        self.main_layout.addWidget(self.gallons_needed, 9, 0)

        #fonts

        font = self.title.font()
        font.setPointSize(20)
        self.title.setFont(font)

        font = self.tripcost_output.font()
        font.setPointSize(15)
        self.tripcost_output.setFont(font)

        font = self.gallons_needed.font()
        font.setPointSize(15)
        self.gallons_needed.setFont(font)

        


app = QApplication(sys.argv)
app.setStyle("Fusion")
window = MainWindow()
window.show()

app.exec()