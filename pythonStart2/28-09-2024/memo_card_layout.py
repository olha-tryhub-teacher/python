""" Вікно для картки питання """
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QTableWidget, QListWidget, QListWidgetItem,
       QLineEdit, QFormLayout,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QButtonGroup, QRadioButton, 
       QPushButton, QLabel, QSpinBox)


app = QApplication([])
app.setStyleSheet("QWidget { font-size: 30px; }")


# віджети, які треба буде розмістити:

# Панель з варіантами:

# Панель із результатом:

# Тепер займаємося розміщенням:
# Розміщуємо варіанти відповідей у два стовпці всередині групи:

# розміщуємо результат:

# розміщуємо всі віджети у вікні, вони розташовані в чотири рядки:

# Тепер створені 4 рядки розмістимо один під одним:

# Результат роботи цього модуля: віджети розміщені всередині layout_card, який можна призначити вікну.
