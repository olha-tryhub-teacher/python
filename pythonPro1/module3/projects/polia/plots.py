import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt

df = pd.read_csv("tiktok_dataset.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# 1. Залежність між тривалістю відео та кількістю переглядів
duration_views = df.groupby("video_duration_sec")["video_view_count"].mean().reset_index()

# 2. Залежність між кількістю лайків і кількістю коментарів
likes_comments = df.groupby("video_like_count")["video_comment_count"].mean().reset_index()

# 3. Визначення середньої кількості лайків за тривалістю відео
average_likes_duration = df.groupby("video_duration_sec")["video_like_count"].mean().reset_index()
average_likes_duration.columns = ["Video Duration (sec)", "Average Likes"]

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

# Підрахунок ключових слів для кожного відео
keyword_counts = []
for index, text in df["video_transcription_text"].items():  # Зміна iteritems на items
    words = count_words(text)
    most_common = Counter(words).most_common(3)  # Отримуємо 3 найпоширеніших слова
    keyword_counts.append((index, [keyword for keyword, _ in most_common]))

# Підрахунок лайків для кожного ключового слова
likes_per_keyword = Counter()

for index, keywords in keyword_counts:
    likes = df["video_like_count"].iloc[index]
    for keyword in keywords:
        likes_per_keyword[keyword] += likes

# Отримання топ 10 ключових слів за кількістю лайків
top_keywords = likes_per_keyword.most_common(10)

# Створення DataFrame для результатів
results_df = pd.DataFrame(top_keywords, columns=["Keyword", "Likes"])

# Візуалізація

# 1. Залежність між тривалістю відео та кількістю переглядів
plt.figure(figsize=(10, 6))
plt.bar(duration_views["video_duration_sec"], duration_views["video_view_count"], color='skyblue')
plt.title('Середня кількість переглядів за тривалістю відео')
plt.xlabel('Тривалість відео (сек)')
plt.ylabel('Середня кількість переглядів')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 2. Залежність між кількістю лайків і кількістю коментарів
plt.figure(figsize=(10, 6))
plt.scatter(likes_comments["video_like_count"], likes_comments["video_comment_count"], color='orange')
plt.title('Середня кількість коментарів за кількістю лайків')
plt.xlabel('Кількість лайків')
plt.ylabel('Середня кількість коментарів')
plt.grid()
plt.show()

# 3. Середня кількість лайків за тривалістю відео
plt.figure(figsize=(10, 6))
plt.bar(average_likes_duration['Video Duration (sec)'], average_likes_duration['Average Likes'], color='lightgreen')
plt.title('Середня кількість лайків за тривалістю відео')
plt.xlabel('Тривалість відео (сек)')
plt.ylabel('Середня кількість лайків')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 4. Топ 10 ключових слів за кількістю лайків
results_df.plot(kind='bar', x='Keyword', y='Likes', color='purple', legend=False, figsize=(10, 6))
plt.title('Топ 10 ключових слів за кількістю лайків')
plt.xlabel('Ключові слова')
plt.ylabel('Кількість лайків')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

print(results_df)
