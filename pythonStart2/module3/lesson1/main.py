import random

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate_password)

    def example(self):
        print(1)

    def generate_password(self):
        signs = ''
        if self.ui.checkBox.isChecked():
            signs = "qwertyuiopsdfghjklzxcvbnm"
        if self.ui.checkBox_2.isChecked():
            signs += "1234567890"

        pass_len = random.randint(8, 16)
        password = ""
        for i in range(pass_len):
            password += random.choice(signs)

        self.ui.label_2.setText(password)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
