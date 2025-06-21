class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.author}) - {self.pages} сторінок"

books = [
    Book("Колонія", "Макс Кідрук", 600),
    Book("Ворошиловград", "Сергій Жадан", 200),
    Book("Я бачу, вас цікавить пітьма", "Ілларіон Павлюк", 400),
    Book("Я (Романтика)", "Микола Хвильовий", 200)
]

pages_sum = sum(book.pages for book in books)
