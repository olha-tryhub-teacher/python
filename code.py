# Створення класу "Ресторан"
class Restaurant:
    def __init__(self, name, cuisine, rating, address):
        self.name = name
        self.cuisine = cuisine
        self.rating = rating
        self.address = address

    def __str__(self):
        return f"{self.name} ({self.cuisine}) - Рейтинг: {self.rating}, Адреса: {self.address}"


# Створення списку об'єктів "Ресторан"
restaurants = [
    Restaurant("Il Piatto", "Італійська", 4.2, "вул. Італійська, 12"),
    Restaurant("Bella Napoli", "Італійська", 4.5, "вул. Піца, 5"),
    Restaurant("Sushi King", "Японська", 4.0, "вул. Суші, 8"),
    Restaurant("Spice Garden", "Індійська", 3.8, "вул. Каррі, 14"),
    Restaurant("Mamma Mia", "Італійська", 4.3, "вул. Піца, 20"),
]

# Створення ітератора для перебору об'єктів "Ресторан"
iterator = iter(restaurants)

# Визначення критеріїв для відбору ресторанів
desired_cuisine = "Італійська"
min_rating = 4.0

# Ініціалізація списку для відібраних ресторанів
selected_restaurants = []

# Перебір ресторанів та відбір та виведення на екран відповідних ресторанів
for restaurant in iterator:
    if restaurant.cuisine == desired_cuisine and restaurant.rating >= min_rating:
        selected_restaurants.append(restaurant)

# Виведення результату на екран
print(f"Список ресторанів з кухнею '{desired_cuisine}' і рейтингом не менше {min_rating}:")
for idx, selected_restaurant in enumerate(selected_restaurants, 1):
    print(f"{idx}. {selected_restaurant}")
