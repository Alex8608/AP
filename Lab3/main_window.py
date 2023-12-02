import sys
import csv
from functools import partial
from PyQt5 import QtWidgets, QtGui, QtCore
from Script_1 import split_by_columns
from Script_2 import split_by_years
from Script_3 import split_by_weeks
from Script_4 import find_in_dataset

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App for Lab3")
        self.folderpath = None
        self.dataset = None
        self.menu=None
        self.destination_folder=None

        '''Widgets'''
        self.label = QtWidgets.QLabel("Выберите папку с исходным датасетом:")
        self.select_folder_button = QtWidgets.QPushButton("Выбрать папку")
        self.select_folder_button.clicked.connect(self.select_folder)

        self.create_dataset_button = QtWidgets.QPushButton("Создать датасет")
        self.create_dataset_button.clicked.connect(self.create_dataset)

        self.date_input = QtWidgets.QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QtCore.QDate.currentDate())

        self.get_data_button = QtWidgets.QPushButton("Получить данные")
        self.get_data_button.clicked.connect(self.get_date)

        '''Layout'''
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_folder_button)
        layout.addWidget(self.create_dataset_button)
        layout.addWidget(self.date_input)
        layout.addWidget(self.get_data_button)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def select_folder(self):
        self.folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку')
        if self.folderpath:
            QtWidgets.QMessageBox.information(self, 'Папка выбрана', f'Выбрана папка: {self.folderpath}')
        self.folderpath += "/dataset.csv"

    def create_dataset(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите папку с исходным датасетом')
            return

        self.destination_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для нового датасета')
        if self.destination_folder:
            self.menu=SubWindow(self)
            self.menu.show()
            

    def get_date(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите папку с исходным датасетом')
            return

        selected_date = self.date_input.date().toString(QtCore.Qt.ISODate)
        self.find_date(selected_date)
        
    
    def find_date(self, selected_date):
        course=find_in_dataset(selected_date, self.folderpath)
        if course==None:
            QtWidgets.QMessageBox.information(self, 'Данные не получены', f'Курса доллара на {selected_date} нет')
        else:
            QtWidgets.QMessageBox.information(self, 'Данные получены', f'Курс доллара на {selected_date} равен {course} руб')


class SubWindow(QtWidgets.QDialog):
    def __init__(self, Main:MainWindow=None):
        super(SubWindow,self).__init__(Main)
        self.setModal(True)

        if Main is not None:
            self.Main = Main

        layout = QtWidgets.QVBoxLayout()

        self.button1 = QtWidgets.QPushButton("Разделить на X и Y")
        self.button1.clicked.connect(self.but1)
        self.button2 = QtWidgets.QPushButton("Разделить по годам")
        self.button2.clicked.connect(self.but2)
        self.button3 = QtWidgets.QPushButton("Разделить по неделям")
        self.button3.clicked.connect(self.but3)

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.setLayout(layout)

    def but1(self):
        split_by_columns(self.Main.folderpath, self.Main.destination_folder)
        QtWidgets.QMessageBox.information(self, 'Датасет создан', f'Датасет создан и сохранен в {self.Main.destination_folder}')
        self.close()
    def but2(self):
        split_by_years(self.Main.folderpath, self.Main.destination_folder)
        QtWidgets.QMessageBox.information(self, 'Датасет создан', f'Датасет создан и сохранен в {self.Main.destination_folder}')
        self.close()
    def but3(self):
        split_by_weeks(self.Main.folderpath, self.Main.destination_folder)
        QtWidgets.QMessageBox.information(self, 'Датасет создан', f'Датасет создан и сохранен в {self.Main.destination_folder}')
        self.close()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())