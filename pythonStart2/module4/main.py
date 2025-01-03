import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from python2.module4.lesson1.ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configure()
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.video) # де ми його будемо показувати
        self.get_date()

    def configure(self):
        self.ui.start.clicked.connect(self.media_play)
        self.ui.stop.clicked.connect(self.media_stop)
        self.ui.calendar.selectionChanged.connect(self.get_date)

    def get_date(self):
        self.media_stop()
        print(self.ui.calendar.selectedDate())
        day = str(self.ui.calendar.selectedDate().day())

        self.media.setMedia(QMediaContent(QUrl.fromLocalFile(f'Video\\{day}.avi')))
        if self.ui.autostart.isChecked():
            self.media_play()

    def media_play(self):
        self.media.play()

    def media_stop(self):
        self.media.stop()



app = QApplication([])
ex = Widget()
ex.show()
app.exec()