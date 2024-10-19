import pandas as pd
from collections import Counter
import re

pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)


df = pd.read_csv("pinterest_finalised.csv")


# Визначення стоп-слів
stop_words = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
    "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
    "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
    "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
    "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
    "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
    "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
}

# Функція для підрахунку слів
def count_words(text):
    if pd.isna(text):  # Перевірка на NaN
        return []
    words = re.findall(r"\w+", text.lower())  # Знаходимо всі слова в тексті
    filtered_words = [word for word in words if word not in stop_words]  # Видаляємо стоп-слова
    return filtered_words

# Підрахунок ключових слів для кожної картинки
keyword_counts = []
for index, text in df["title"].items():  # Зміна iteritems на items
    words = count_words(text)
    most_common = Counter(words).most_common(3)  # Отримуємо 3 найпоширеніших слова
    keyword_counts.append((index, [keyword for keyword, _ in most_common]))

# Підрахунок репінів для кожного ключового слова
repin_per_keyword = Counter()

for index, keywords in keyword_counts:
    repins = df["repin_count"].iloc[index]
    for keyword in keywords:
        repin_per_keyword[keyword] += repins

#######  Отримання топ 10 ключових слів за кількістю лайків  ###########
top_keywords = repin_per_keyword.most_common(10)

# Створення DataFrame для результатів
results_df = pd.DataFrame(top_keywords, columns=["Keyword", "Likes"])
print(results_df)


# Завантажуємо дані з файлу
df_social = pd.read_csv('socialmedia.csv')

# 1. Кількість публікацій на різних платформах
# Рахуємо кількість публікацій для кожної платформи
platform_post_counts = df_social['Platform'].value_counts()

# 2. Середня кількість взаємодій для кожної платформи
# Рахуємо середню кількість лайків, коментарів та шейрів на кожній платформі
average_engagement = df_social.groupby('Platform')[['Likes/Reactions', 'Comments', 'Shares/Retweets']].mean()

# 3. Кількість верифікованих та не верифікованих користувачів
# Рахуємо скільки є верифікованих та не верифікованих акаунтів
verification_counts = df_social['Account Verification'].value_counts()

# 4. Публікації з найбільшою кількістю коментарів
# Знаходимо топ-5 публікацій, які мають найбільшу кількість коментарів
top_commented_posts = df_social[['Post ID', 'Username', 'Comments']].sort_values(by='Comments', ascending=False).head(5)

# 5. Середня кількість підписників для верифікованих і не верифікованих користувачів
# Обчислюємо середню кількість підписників залежно від статусу верифікації акаунтів
average_followers_by_verification = df_social.groupby('Account Verification')['User Followers'].mean()

# Виведемо результати
print("Кількість публікацій на платформах:")
print(platform_post_counts)
print("\nСередня кількість взаємодій на платформах:")
print(average_engagement)
print("\nКількість верифікованих та не верифікованих користувачів:")
print(verification_counts)
print("\nТоп 5 публікацій з найбільшою кількістю коментарів:")
print(top_commented_posts)
print("\nСередня кількість підписників для верифікованих та не верифікованих користувачів:")
print(average_followers_by_verification)