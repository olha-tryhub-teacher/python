import pandas as pd
from collections import Counter
import re

df = pd.read_csv("search_statictics_game.csv", delimiter=";")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# 1. Найпопулярніші запити за обсягом пошуку
top_keywords = df[["Keyword", "Volume"]].sort_values(by="Volume", ascending=False).head(10)
print("Найпопулярніші запити:\n", top_keywords)

# 2. Складність запитів
difficulty_analysis = df[["Keyword", "Difficulty"]].groupby("Difficulty").count().reset_index()
print("\nСкладність запитів:\n", difficulty_analysis)

# 3. Тренди запитів
# Дослідження обсягу пошуку по запитах
volume_trend = df.groupby("Keyword")["Volume"].sum().reset_index().sort_values(by="Volume", ascending=False)
print("\nТренди запитів за обсягом:\n", volume_trend)

# 4. Потенціал трафіку
traffic_potential = df[["Keyword", "Traffic potential"]].sort_values(by="Traffic potential", ascending=False).head(10)
print("\nТоп запитів з потенціалом трафіку:\n", traffic_potential)

# 5. Аналіз SERP Features
serp_analysis = df["SERP Features"].value_counts()
print("\nАналіз SERP Features:\n", serp_analysis)

# 6. Порівняння мобільного та десктопного трафіку
mobile_desktop_comparison = df[["Mobile", "Desktop"]].mean()
print("\nСередній мобільний та десктопний трафік:\n", mobile_desktop_comparison)

# 7. Виявлення підрапопулярність ключових слів у запитах
# Об"єднуємо всі ключові слова в один рядок
all_keywords = " ".join(df["Keyword"].dropna())
# Витягуємо всі слова, ігноруючи регістр та символи
words = re.findall(r"\b\w+\b", all_keywords.lower())
# Список стоп-слів
stop_words = {"to", "how", "in", "a", "make", "get", "on", "4"}
# Фільтрація слів
filtered_words = [word for word in words if word not in stop_words]
# Підрахунок кількості кожного слова
word_counts = Counter(filtered_words)

# Отримуємо 10 найчастіших слів
top_10_words = word_counts.most_common(10)

# Виведення результатів
print("10 найчастіших слів у колонці `Keyword` (без стоп-слів) та їх кількість:")
for word, count in top_10_words:
    print(f"{word}: {count}")