
from PyQt5.QtWidgets import (
        QApplication, QWidget, QListWidget,
        QHBoxLayout, QVBoxLayout,
        QPushButton, QLabel, QFileDialog  # Діалог відкриття файлів (і папок)
)

from qss import QSS
import os

from PyQt5.QtCore import Qt # потрібна константа Qt.KeepAspectRatio для зміни розмірів із збереженням пропорцій
from PyQt5.QtGui import QPixmap # оптимізована для показу на екрані картинка
from PIL import Image


app = QApplication([])
win = QWidget()

win.resize(1000, 800)
win.setObjectName("mainWindow")
win.setWindowTitle("Easy Editor")
win.setStyleSheet(QSS)

lb_image = QLabel("Картинка")
btn_dir = QPushButton("Папка")
lw_files = QListWidget()


btn_left = QPushButton("Уліво")
btn_right = QPushButton("Управо")
btn_flip = QPushButton("Дзеркало")
btn_sharp = QPushButton("Різкість")
btn_bw = QPushButton("Ч/Б")


row = QHBoxLayout()          # Основний рядок
col1 = QVBoxLayout()         # ділиться на два стовпці
col2 = QVBoxLayout()
col1.addWidget(btn_dir)      # у першому – кнопка вибору директорії
col1.addWidget(lw_files)     # та список файлів
col2.addWidget(lb_image, 95) # у другому - картинка
row_tools = QHBoxLayout()    # та рядок кнопок
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
col2.addLayout(row_tools)


row.addLayout(col1, 30)
row.addLayout(col2, 70)
win.setLayout(row)


win.show()

workdir = ""

def filter(files, extensions):
   result = []
   for filename in files:
       for ext in extensions:
           if filename.endswith(ext):
               result.append(filename)
   return result


def chooseWorkdir():
   global workdir
   workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
   extensions = [".jpg",".jpeg", ".png", ".gif", ".bmp"]
   chooseWorkdir()
   filenames = filter(os.listdir(workdir), extensions)
   lw_files.clear()
   for filename in filenames:
       lw_files.addItem(filename)


class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        ''' під час завантаження запам'ятовуємо шлях та ім'я файлу '''
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    def saveImage(self):
        ''' зберігає копію файлу у підпапці '''
        path = os.path.join(self.dir, self.save_dir)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def showImage(self, path):
        lb_image.hide()  # Ховає елемент `lb_image`, щоб під час зміни зображення користувач не бачив проміжного стану.
        pixmapimage = QPixmap(path)  # Завантажує зображення з вказаного шляху (`path`) у об'єкт `QPixmap`.
        w, h = lb_image.width(), lb_image.height()  # Зберігає поточну ширину (`w`) і висоту (`h`) віджета `lb_image`.
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)  # Масштабує зображення, щоб воно відповідало розмірам `lb_image`, зберігаючи пропорції.
        lb_image.setPixmap(pixmapimage)  # Встановлює масштабоване зображення в якості вмісту для віджета `lb_image`.
        lb_image.show()  # Показує елемент `lb_image` з новим зображенням.

    def do_bw(self):
        self.image = self.image.convert("L")
        self.saveImage()
        image_path = os.path.join(
            self.dir, self.save_dir, self.filename)
        self.showImage(image_path)


def showChosenImage():  # Оголошення функції `showChosenImage`, яка відображає вибране зображення з переліку файлів.
    if lw_files.currentRow() >= 0:  # Перевіряє, чи обраний будь-який елемент у списку `lw_files` (чи є активний рядок).
        filename = lw_files.currentItem().text()  # Отримує текст вибраного елемента списку (ім'я файлу).
        workimage.loadImage(workdir, filename)  # Завантажує вибране зображення, передаючи робочу директорію та ім'я файлу.
        image_path = os.path.join(workimage.dir, workimage.filename)  # Створює повний шлях до зображення, поєднуючи директорію та ім'я файлу.
        workimage.showImage(image_path)  # Викликає метод `showImage`, щоб відобразити зображення за вказаним шляхом.


btn_dir.clicked.connect(showFilenamesList)

workimage = ImageProcessor() #поточне робоче зображення для роботи

lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)

app.exec()


