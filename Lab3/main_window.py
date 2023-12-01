import sys
import csv
from PyQt5 import QtWidgets, QtGui, QtCore

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App for Lab3")
        self.folderpath = None
        self.dataset = None

        '''Widgets'''
        self.label = QtWidgets.QLabel("Выберите папку с исходным датасетом:")
        self.select_folder_button = QtWidgets.QPushButton("Выбрать папку")
        self.select_folder_button.clicked.connect(self.select_folder)

        self.create_annotation_button = QtWidgets.QPushButton("Создать аннотацию")
        self.create_annotation_button.clicked.connect(self.create_annotation)

        self.create_dataset_button = QtWidgets.QPushButton("Создать датасет")
        self.create_dataset_button.clicked.connect(self.create_dataset)

        self.date_input = QtWidgets.QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QtCore.QDate.currentDate())

        self.get_data_button = QtWidgets.QPushButton("Получить данные")
        self.get_data_button.clicked.connect(self.get_data)

        '''Layout'''
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.select_folder_button)
        layout.addWidget(self.create_annotation_button)
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

    def create_annotation(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите папку с исходным датасетом')
            return

        destination_file, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Выберите место для сохранения аннотации', '', 'CSV Files (*.csv);;All Files (*)')
        if destination_file:
            annotation_data = [["Дата", "Курс доллара (рубли)"]]

            with open(destination_file, 'w', newline='', encoding='utf-8') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(annotation_data)

            QtWidgets.QMessageBox.information(self, 'Аннотация создана', f'Аннотация создана и сохранена в {destination_file}')

    def create_dataset(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите папку с исходным датасетом')
            return

        destination_folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку для нового датасета')
        if destination_folder:
            # Здесь нужно добавить логику создания нового датасета и его аннотации
            QtWidgets.QMessageBox.information(self, 'Датасет создан', f'Датасет создан и сохранен в {destination_folder}')

    def get_data(self):
        if not self.folderpath:
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Выберите папку с исходным датасетом')
            return

        selected_date = self.date_input.date().toString(QtCore.Qt.ISODate)
        # Здесь нужно добавить логику получения данных для выбранной даты и их отображения в интерфейсе
        QtWidgets.QMessageBox.information(self, 'Данные получены', f'Данные для {selected_date} получены и отображены в интерфейсе')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())