    def add_note(self):
        note_name, ok = QtWidgets.QInputDialog.getText(
            self, "Додати замітку", "Назва замітки: ")
        if ok and note_name != "":
            self.notes[note_name] = {"текст": "", "теги": []}
            self.ui.listWidget.addItem(note_name)
            self.save_to_file()
