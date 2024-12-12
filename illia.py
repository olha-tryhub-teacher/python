    def del_tag(self):
        if self.ui.listWidget_2.currentItem():
            key = self.ui.listWidget.currentItem().text()
            tag = self.ui.listWidget_2.currentItem().text()
            self.notes[key]["теги"].remove(tag)
            self.ui.listWidget_2.clear()
            self.ui.listWidget_2.addItems(self.notes[key]["теги"])
            self.save_to_file()
        else:
            QtWidgets.QMessageBox.warning(
                self, "Помилка", "Тег для видалення не обраний!")
