    def search_tag(self):
        tag = self.ui.lineEdit.text()
        if self.ui.pushButton_7.text() == "Шукати замітки по тегу" and tag:
            notes_filtered = {k: v for k, v in self.notes.items() if tag in v["теги"]}
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(notes_filtered)
            self.ui.pushButton_7.setText("Скинути пошук")
        elif self.ui.pushButton_7.text() == "Скинути пошук":
            self.ui.listWidget.clear()
            self.ui.listWidget.addItems(self.notes)
            self.ui.lineEdit.clear()
            self.ui.pushButton_7.setText("Шукати замітки по тегу")
