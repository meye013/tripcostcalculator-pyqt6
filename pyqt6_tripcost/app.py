import sys
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QDoubleSpinBox, QVBoxLayout ,QWidget ,QHBoxLayout, QLabel, QLayout, QGridLayout)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
            
    #functions
    def reset(self):
        self.title.setText("Trip Cost Calculator")

        self.tripcost_output.setText("Tripcost: $ ")

        self.gallons_needed.setText("Gallons Needed: ")
    def calculate(self):
        if self.fuelefficiency_input.value() == 0.00:
                self.tripcost_output.setText("Tripcost: $Error")

                self.gallons_needed.setText("Gallons Needed: Error")
        if self.fuelefficiency_input.value() > 0.00:
                gallons_needed =  self.tripdistance_input.value()/self.fuelefficiency_input.value()

                tripcost = gallons_needed*self.gasprice_input.value()

                self.tripcost_output.setText("Tripcost: " + "$" + str(tripcost))

                self.gallons_needed.setText("Gallons Needed: " + str(gallons_needed))

    def __init__(self):
        super().__init__()

        self.setWindowTitle("pyqt6 tripcost")
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

        self.gasprice_input.setPrefix("Gas Price = $ ")
        self.tripdistance_input.setPrefix("Trip Distance = ")
        self.fuelefficiency_input.setPrefix("Fuel efficiency = ")

        #spinbox suffixes

        self.gasprice_input.setSuffix(" per gal")
        self.tripdistance_input.setSuffix(" mi")
        self.fuelefficiency_input.setSuffix(" mpgs")

        #pushbuttons
        
        self.calculate_button = QPushButton("Calculate")
        self.main_layout.addWidget(self.calculate_button, 5, 0)
        self.calculate_button.pressed.connect(self.calculate)
        
        self.reset_button = QPushButton("Reset")
        self.main_layout.addWidget(self.reset_button, 6, 0)
        self.reset_button.pressed.connect(self.reset)

        #outputs

        self.tripcost_output = QLabel("Tripcost: $")
        self.main_layout.addWidget(self.tripcost_output, 8, 0)
        
        self.gallons_needed = QLabel("Gallons Needed: ")
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