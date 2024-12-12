    def save_note(self):
        if self.ui.listWidget.currentItem():
            key = self.ui.listWidget.currentItem().text()
            self.notes[key]["текст"] = self.ui.textEdit.toPlainText()
            self.save_to_file()
        else:
            QtWidgets.QMessageBox.warning(self, "Помилка", "Замітка для збереження не вибрана!")
