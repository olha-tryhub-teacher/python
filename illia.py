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
