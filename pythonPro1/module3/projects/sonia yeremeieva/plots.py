import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# Завантажуємо дані
df = pd.read_csv("pinterest_finalised.csv")

# Визначення стоп-слів
stop_words = { "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
    "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
    "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}

# Функція для підрахунку слів
def count_words(text):
    if pd.isna(text):  # Перевірка на NaN
        return []
    words = re.findall(r"\w+", text.lower())  # Знаходимо всі слова в тексті
    filtered_words = [word for word in words if word not in stop_words]  # Видаляємо стоп-слова
    return filtered_words

# Підрахунок ключових слів для кожної картинки
keyword_counts = []
for index, text in df["title"].items():
    words = count_words(text)
    most_common = Counter(words).most_common(3)  # Отримуємо 3 найпоширеніших слова
    keyword_counts.append((index, [keyword for keyword, _ in most_common]))

# Підрахунок репінів для кожного ключового слова
repin_per_keyword = Counter()

for index, keywords in keyword_counts:
    repins = df["repin_count"].iloc[index]
    for keyword in keywords:
        repin_per_keyword[keyword] += repins

# Отримання топ 10 ключових слів за кількістю лайків
top_keywords = repin_per_keyword.most_common(10)

# Створення DataFrame для результатів
results_df = pd.DataFrame(top_keywords, columns=["Keyword", "Likes"])
print(results_df)

# Графік топ 10 ключових слів
plt.figure(figsize=(10, 6))
plt.barh(results_df["Keyword"], results_df["Likes"], color='lightblue')
plt.xlabel('Кількість репінів')
plt.title('Топ 10 ключових слів за кількістю репінів')
plt.gca().invert_yaxis()
plt.show()

# Завантажуємо дані з файлу
df_social = pd.read_csv('socialmedia.csv')

# 1. Кількість публікацій на різних платформах
platform_post_counts = df_social['Platform'].value_counts()

# Графік кількості публікацій на платформах
plt.figure(figsize=(10, 6))
platform_post_counts.plot(kind='bar', color='coral')
plt.xlabel('Платформа')
plt.ylabel('Кількість публікацій')
plt.title('Кількість публікацій на різних платформах')
plt.xticks(rotation=45)
plt.show()

# 2. Середня кількість взаємодій для кожної платформи
average_engagement = df_social.groupby('Platform')[['Likes/Reactions', 'Comments', 'Shares/Retweets']].mean()

# Графік середньої кількості взаємодій
average_engagement.plot(kind='bar', figsize=(10, 6), color=['lightgreen', 'lightblue', 'salmon'])
plt.ylabel('Середня кількість')
plt.title('Середня кількість взаємодій для кожної платформи')
plt.xticks(rotation=45)
plt.legend(title='Взаємодії', loc='upper right')
plt.show()

# 3. Кількість верифікованих та не верифікованих користувачів
verification_counts = df_social['Account Verification'].value_counts()

# Графік верифікації користувачів
plt.figure(figsize=(6, 6))
verification_counts.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'salmon'])
plt.title('Кількість верифікованих та не верифікованих користувачів')
plt.ylabel('')
plt.show()

# 4. Публікації з найбільшою кількістю коментарів
top_commented_posts = df_social[['Post ID', 'Username', 'Comments']].sort_values(by='Comments', ascending=False).head(5)

# Виводимо топ 5 публікацій
print("\nТоп 5 публікацій з найбільшою кількістю коментарів:")
print(top_commented_posts)

# 5. Середня кількість підписників для верифікованих і не верифікованих користувачів
average_followers_by_verification = df_social.groupby('Account Verification')['User Followers'].mean()

# Графік середньої кількості підписників
plt.figure(figsize=(8, 5))
average_followers_by_verification.plot(kind='bar', color='lightblue')
plt.ylabel('Середня кількість підписників')
plt.title('Середня кількість підписників для верифікованих та не верифікованих користувачів')
plt.xticks(rotation=0)
plt.show()

# Виводимо результати
print("\nСередня кількість підписників для верифікованих та не верифікованих користувачів:")
print(average_followers_by_verification)
