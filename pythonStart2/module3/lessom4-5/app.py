from PyQt5 import QtCore, QtGui, QtWidgets
import json

# Підключення створеного UI
from ui import Ui_MainWindow

class NotesWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.notes = {}

        # Підключення обробників
        self.ui.pushButton.clicked.connect(self.add_note)
        self.ui.listWidget.itemClicked.connect(self.show_note)
        self.ui.pushButton_3.clicked.connect(self.save_note)
        self.ui.pushButton_2.clicked.connect(self.del_note)
        self.ui.pushButton_4.clicked.connect(self.add_tag)
        self.ui.pushButton_5.clicked.connect(self.del_tag)
        self.ui.pushButton_6.clicked.connect(self.search_tag)

        # Завантаження заміток
        self.load_notes()

    def load_notes(self):
        try:
            with open("notes_data.json", "r", encoding="utf-8") as file:
                self.notes = json.load(file)
            self.ui.listWidget.addItems(self.notes)
        except FileNotFoundError:
            self.notes = {}

    def save_to_file(self):
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(self.notes, file, sort_keys=True,
                      ensure_ascii=False)

    def add_note(self):
        note_name, ok = QtWidgets.QInputDialog.getText(
            self, "Додати замітку", "Назва замітки: ")
        if ok and note_name != "":
            self.notes[note_name] = {"текст": "", "теги": []}
            self.ui.listWidget.addItem(note_name)
            self.save_to_file()

    def show_note(self):
        key = self.ui.listWidget.currentItem().text()
        self.ui.textEdit.setText(self.notes[key]["текст"])
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes[key]["теги"])

    def save_note(self):
        if self.ui.listWidget.currentItem():
            key = self.ui.listWidget.currentItem().text()
            self.notes[key]["текст"] = self.ui.textEdit.toPlainText()
            self.save_to_file()
        else:
            QtWidgets.QMessageBox.warning(self, "Помилка", "Замітка для збереження не вибрана!")

    def del_note(self):
        if self.ui.listWidget.currentItem():
            key = self.ui.listWidget.currentItem().text()
            del self.notes[key]
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            self.ui.textEdit.clear()
            self.ui.listWidget.addItems(self.notes)
            self.save_to_file()
        else:
            QtWidgets.QMessageBox.warning(self, "Помилка", "Замітка для видалення не обрана!")

    def add_tag(self):
        if self.ui.listWidget.currentItem():
            key = self.ui.listWidget.currentItem().text()
            tag = self.ui.lineEdit.text()
            if tag and tag not in self.notes[key]["теги"]:
                self.notes[key]["теги"].append(tag)
                self.ui.listWidget_2.addItem(tag)
                self.ui.lineEdit.clear()
                self.save_to_file()
        else:
            QtWidgets.QMessageBox.warning(self, "Помилка", "Замітка для додавання тега не обрана!")
