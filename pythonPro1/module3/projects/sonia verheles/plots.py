import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt

df = pd.read_csv("search_statictics_game.csv", delimiter=";")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# 1. Найпопулярніші запити за обсягом пошуку
top_keywords = df[["Keyword", "Volume"]].sort_values(by="Volume", ascending=False).head(10)
print("Найпопулярніші запити:\n", top_keywords)

# Графік найпопулярніших запитів
plt.figure(figsize=(10, 5))
plt.barh(top_keywords["Keyword"], top_keywords["Volume"], color='skyblue')
plt.xlabel('Обсяг пошуку')
plt.title('Найпопулярніші запити за обсягом пошуку')
plt.gca().invert_yaxis()  # Інвертувати вісь y для кращого вигляду
plt.show()

# 2. Складність запитів
difficulty_analysis = df[["Keyword", "Difficulty"]].groupby("Difficulty").count().reset_index()
print("\nСкладність запитів:\n", difficulty_analysis)

# Графік складності запитів
plt.figure(figsize=(8, 5))
plt.bar(difficulty_analysis["Difficulty"], difficulty_analysis["Keyword"], color='lightcoral')
plt.xlabel('Складність')
plt.ylabel('Кількість запитів')
plt.title('Аналіз складності запитів')
plt.xticks(rotation=45)
plt.show()

# 4. Потенціал трафіку
traffic_potential = df[["Keyword", "Traffic potential"]].sort_values(by="Traffic potential", ascending=False).head(10)
print("\nТоп запитів з потенціалом трафіку:\n", traffic_potential)

# Графік потенціалу трафіку
plt.figure(figsize=(10, 5))
plt.barh(traffic_potential["Keyword"], traffic_potential["Traffic potential"], color='lightgreen')
plt.xlabel('Потенціал трафіку')
plt.title('Топ запитів з потенціалом трафіку')
plt.gca().invert_yaxis()
plt.show()

# 5. Аналіз SERP Features
serp_analysis = df["SERP Features"].value_counts()
print("\nАналіз SERP Features:\n", serp_analysis)

# Графік аналізу SERP Features
plt.figure(figsize=(10, 5))
serp_analysis.plot(kind='bar', color='purple')
plt.xlabel('SERP Features')
plt.ylabel('Кількість')
plt.title('Аналіз SERP Features')
plt.xticks(rotation=45)
plt.show()

# 6. Порівняння мобільного та десктопного трафіку
mobile_desktop_comparison = df[["Mobile", "Desktop"]].mean()
print("\nСередній мобільний та десктопний трафік:\n", mobile_desktop_comparison)

# Графік порівняння мобільного та десктопного трафіку
plt.figure(figsize=(8, 5))
mobile_desktop_comparison.plot(kind='bar', color=['cyan', 'orange'])
plt.ylabel('Середнє значення')
plt.title('Порівняння мобільного та десктопного трафіку')
plt.xticks(rotation=0)
plt.show()

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

# Графік 10 найчастіших слів
plt.figure(figsize=(10, 5))
words, counts = zip(*top_10_words)  # Розділення слів та їх кількості
plt.bar(words, counts, color='lightblue')
plt.xlabel('Слова')
plt.ylabel('Кількість')
plt.title('10 найчастіших слів у колонці `Keyword`')
plt.xticks(rotation=45)
plt.show()
