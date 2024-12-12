    def show_note(self):
        key = self.ui.listWidget.currentItem().text()
        self.ui.textEdit.setText(self.notes[key]["текст"])
        self.ui.listWidget_2.clear()
        self.ui.listWidget_2.addItems(self.notes[key]["теги"])
