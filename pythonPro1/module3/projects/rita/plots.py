import pandas as pd
import matplotlib.pyplot as plt

# Завантаження датасету
df = pd.read_csv("all_combined.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# 1. Загальна інформація про додатки
# Середня оцінка для кожного додатку
app_average_score = df.groupby('app')['score'].mean().sort_values()

# Загальна кількість позитивних відгуків (score > 3) для кожного додатка
positive_reviews_count = df[df['score'] > 3].groupby('app')['reviewId'].count().sort_values()

# Загальна кількість негативних відгуків (score <= 3) для кожного додатка
negative_reviews_count = df[df['score'] <= 3].groupby('app')['reviewId'].count().sort_values()

# 2. Аналіз інформації про додатки-месенджери
# Створення підмножини для додатків-месенджерів
messenger_apps = ['Facebook Messenger', 'WhatsApp', 'Viber', 'LINE', 'Instagram', 'Skype', 'Snapchat', 'TikTok']
messengers_df = df[df['app'].isin(messenger_apps)]

# Середня оцінка для кожного месенджера
messenger_average_score = messengers_df.groupby('app')['score'].mean().sort_values()

# Кількість позитивних та негативних відгуків для месенджерів
positive_reviews_messengers = messengers_df[messengers_df['score'] > 3].groupby('app')['reviewId'].count().sort_values()
negative_reviews_messengers = messengers_df[messengers_df['score'] <= 3].groupby('app')['reviewId'].count().sort_values()

# Виведення результатів
print("Загальна інформація про додатки")
print("Середня оцінка для кожного додатку:\n", app_average_score)
print("Кількість позитивних відгуків для кожного додатка:\n", positive_reviews_count)
print("Кількість негативних відгуків для кожного додатка:\n", negative_reviews_count)

print("\nАналіз інформації про додатки-месенджери")
print("Середня оцінка для кожного месенджера:\n", messenger_average_score)
print("Кількість позитивних відгуків для кожного месенджера:\n", positive_reviews_messengers)
print("Кількість негативних відгуків для кожного месенджера:\n", negative_reviews_messengers)

# Візуалізація

# 1. Середня оцінка для кожного додатку
plt.figure(figsize=(10, 6))
app_average_score.plot(kind='bar', color='skyblue')
plt.title('Середня оцінка для кожного додатку')
plt.xlabel('Додаток')
plt.ylabel('Середня оцінка')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 2. Кількість позитивних відгуків для кожного додатку
plt.figure(figsize=(10, 6))
positive_reviews_count.plot(kind='bar', color='lightgreen')
plt.title('Кількість позитивних відгуків для кожного додатку')
plt.xlabel('Додаток')
plt.ylabel('Кількість позитивних відгуків')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 3. Кількість негативних відгуків для кожного додатку
plt.figure(figsize=(10, 6))
negative_reviews_count.plot(kind='bar', color='salmon')
plt.title('Кількість негативних відгуків для кожного додатку')
plt.xlabel('Додаток')
plt.ylabel('Кількість негативних відгуків')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 4. Середня оцінка для кожного месенджера
plt.figure(figsize=(10, 6))
messenger_average_score.plot(kind='bar', color='lightblue')
plt.title('Середня оцінка для кожного месенджера')
plt.xlabel('Месенджер')
plt.ylabel('Середня оцінка')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 5. Кількість позитивних відгуків для кожного месенджера
plt.figure(figsize=(10, 6))
positive_reviews_messengers.plot(kind='bar', color='lightgreen')
plt.title('Кількість позитивних відгуків для кожного месенджера')
plt.xlabel('Месенджер')
plt.ylabel('Кількість позитивних відгуків')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# 6. Кількість негативних відгуків для кожного месенджера
plt.figure(figsize=(10, 6))
negative_reviews_messengers.plot(kind='bar', color='salmon')
plt.title('Кількість негативних відгуків для кожного месенджера')
plt.xlabel('Месенджер')
plt.ylabel('Кількість негативних відгуків')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()