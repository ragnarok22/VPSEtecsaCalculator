from PyQt5.QtWidgets import *

from helpers import *
from setup import __appname__


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle(__appname__)
        self.setFixedSize(640, 480)
        calculator = CalculatorWidget()
        self.setCentralWidget(calculator)


class CalculatorWidget(QWidget):
    def __init__(self):
        super(CalculatorWidget, self).__init__()
        self.main_layout = QGridLayout(self)
        self.setLayout(self.main_layout)

        self.cpu_label = QLabel('Cantidad de CPU')
        self.cpu_text = QSpinBox()
        self.cpu_text.setMinimum(CPU_MIN)
        self.cpu_text.setMaximum(CPU_MAX)
        self.cpu_text.valueChanged.connect(self.calculate)
        self.main_layout.addWidget(self.cpu_label, 0, 0)
        self.main_layout.addWidget(self.cpu_text, 0, 1)

        self.ram_label = QLabel('Cantidad de RAM (MB)')
        self.ram_text = QSpinBox()
        self.ram_text.setMinimum(RAM_MIN)
        self.ram_text.setMaximum(RAM_MAX)
        self.ram_text.valueChanged.connect(self.calculate)
        self.main_layout.addWidget(self.ram_label, 1, 0)
        self.main_layout.addWidget(self.ram_text, 1, 1)

        self.storage_label = QLabel('Espacio en disco (GB)')
        self.storage_text = QSpinBox()
        self.storage_text.setMinimum(STORAGE_MIN)
        self.storage_text.setMaximum(STORAGE_MAX)
        self.storage_text.valueChanged.connect(self.calculate)
        self.main_layout.addWidget(self.storage_label, 2, 0)
        self.main_layout.addWidget(self.storage_text, 2, 1)

        self.price_in_hours = QLabel('Precio en horas')
        self.price_in_days = QLabel('Precio en un día')
        self.price_in_months = QLabel('Precio en un mes (30 días)')

        self.main_layout.addWidget(self.price_in_hours, 3, 0)
        self.main_layout.addWidget(self.price_in_days, 4, 0)
        self.main_layout.addWidget(self.price_in_months, 5, 0)

    def calculate(self):
        cpu = self.cpu_text.value()
        ram = self.ram_text.value()
        storage = self.storage_text.value()
        self.price_in_hours.setText('Precio en horas: $' + str(price_per_hours(cpu, ram, storage)))
        self.price_in_days.setText('Precio en un día: $' + str(price_per_day(cpu, ram, storage)))
        self.price_in_months.setText('Precio en un mes (30 días): $' + str(price_per_month(cpu, ram, storage)))