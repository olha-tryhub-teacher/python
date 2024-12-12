
    def save_to_file(self):
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(self.notes, file, sort_keys=True,
                      ensure_ascii=False)
