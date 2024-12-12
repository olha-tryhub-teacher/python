import sys
app = QtWidgets.QApplication(sys.argv)
mainWindow = NotesWindow()
mainWindow.show()
sys.exit(app.exec_())
