    def add_tag(self):
        if self.ui.listWidget.currentItem():
            key = self.ui.listWidget.currentItem().text()
            tag = self.ui.lineEdit.text()
            if tag and tag not in self.notes[key]["теги"]:
                self.notes[key]["теги"].append(tag)
                self.ui.listWidget_2.addItem(tag)
                self.ui.lineEdit.clear()
                self.save_to_file()
        else:
            QtWidgets.QMessageBox.warning(self, "Помилка", "Замітка для додавання тега не обрана!")
