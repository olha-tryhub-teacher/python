from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
import json


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Завантаження даних із JSON
        self.notes = {
            "Ласкаво просимо!": {
                "текст": "Це найкращий додаток для заміток у світі!",
                "теги": ["добро", "інструкція"]
            },
            "Оля": {
                "текст": "Це найкращий додаток для заміток у світі!",
                "теги": ["добро", "інструкція"]
            },
            "Коля": {
                "текст": "Це найкращий додаток для заміток у світі!",
                "теги": ["добро", "інструкція"]
            }
        }
        self.load_notes()

        # Підключення подій
        self.ui.listWidget.itemClicked.connect(self.show_note)

    def load_notes(self):
        """Завантажує замітки у список."""
        try:
            with open("notes_data.json", "r", encoding="utf-8") as file:
                if file.read().strip():  # Перевіряємо, чи файл не порожній
                    file.seek(0)  # Повертаємося на початок файлу
                    self.notes = json.load(file)
                else:
                    raise ValueError("Файл порожній")
        except (FileNotFoundError, ValueError):  # Якщо файл не знайдено або він порожній
            with open("notes_data.json", "w", encoding="utf-8") as file:
                json.dump(self.notes, file, ensure_ascii=False, indent=4)

        # Оновлюємо список заміток у віджеті
        self.ui.listWidget.clear()
        self.ui.listWidget.addItems(self.notes.keys())

    def show_note(self):
        """Відображає вибрану замітку та оновлює список тегів."""
        current_item = self.ui.listWidget.currentItem()
        if current_item:
            key = current_item.text()
            self.ui.textEdit.setText(self.notes[key]["текст"])
            self.ui.listWidget_2.clear()
            self.ui.listWidget_2.addItems(self.notes[key]["теги"])



app = QApplication([])

# Ініціалізація та запуск вікна
window = Widget()
window.show()

app.exec_()
