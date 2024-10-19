import pandas as pd
from collections import Counter
import re

df = pd.read_csv("tiktok_dataset.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# 1. Залежність між тривалістю відео та кількістю переглядів
duration_views = df.groupby("video_duration_sec")["video_view_count"].mean().reset_index()
print("Середня кількість переглядів за тривалістю відео:\n", duration_views)

# 2. Залежність між кількістю лайків і кількістю коментарів
likes_comments = df.groupby("video_like_count")["video_comment_count"].mean().reset_index()
print("\nСередня кількість коментарів за кількістю лайків:\n", likes_comments)

# 3. Визначення середньої кількості лайків за тривалістю відео
average_likes_duration = df.groupby("video_duration_sec")["video_like_count"].mean().reset_index()
average_likes_duration.columns = ["Video Duration (sec)", "Average Likes"]
print("\nСередня кількість лайків за тривалістю відео:\n", average_likes_duration)

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

#######  Отримання топ 10 ключових слів за кількістю лайків  ###########
top_keywords = likes_per_keyword.most_common(10)

# Створення DataFrame для результатів
results_df = pd.DataFrame(top_keywords, columns=["Keyword", "Likes"])

print(results_df)
