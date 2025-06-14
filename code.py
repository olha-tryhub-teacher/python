class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def generate_product_list(self):
        for product in self.products:
            yield product


def generate_product_page(product_generator, limit):
    count = 0
    for product in product_generator:
        if count < limit:
            print(product)
            count += 1
        if count == limit:
            break


# Створення магазину і додавання товарів
store = Store()

store.add_product(Product("Ліжко", 500, 5))
store.add_product(Product("Стіл", 250, 3))
store.add_product(Product("Стілець", 50, 10))
store.add_product(Product("Шафа", 350, 4))
store.add_product(Product("Диван", 800, 2))
store.add_product(Product("Комод", 150, 6))
store.add_product(Product("Столик", 100, 8))
store.add_product(Product("Крісло", 75, 12))
store.add_product(Product("Тумба", 55, 5))
store.add_product(Product("Полиця", 200, 7))


# Генератор для виведення товарів на сторінку сайту
products_generated = store.generate_product_list()

while input() == 'c':
    generate_product_page(products_generated, limit=3)
