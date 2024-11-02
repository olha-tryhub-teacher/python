import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df_cs = pd.read_csv('csgo_steam_reviews.csv')

# Перевірка наявності пропущених значень в колонці review
df_cs['review'] = df_cs['review'].fillna('')  # Заміна NaN на пусті рядки
df_cs['review_length'] = df_cs['review'].apply(len)  # Обчислення довжини відгуку

# Конвертація стовпця created у формат дати та часу
df_cs['created'] = pd.to_datetime(df_cs['created'])

# Витягуємо години з дати та часу
df_cs['hour'] = df_cs['created'].dt.hour

# 1. Середня довжина відгуку за годинами
average_length_by_hour = df_cs.groupby('hour')['review_length'].mean().reset_index()

plt.figure(figsize=(12, 6))
plt.plot(average_length_by_hour['hour'], average_length_by_hour['review_length'], marker='o')
plt.title('Середня довжина відгуку за годинами')
plt.xlabel('Година')
plt.ylabel('Середня довжина відгуку')
plt.grid()
plt.xticks(range(24))
plt.show()

# 2. Вплив підтримки коментаря на кількість ігор, що належать автору
games_owned_vs_voted = df_cs.groupby('voted_up')['author.num_games_owned'].mean()

plt.figure(figsize=(8, 5))
games_owned_vs_voted.plot(kind='bar', color='orange')
plt.title('Середня кількість ігор, що належать авторам, за підтримкою коментаря')
plt.xlabel('Підтримка коментаря')
plt.ylabel('Середня кількість ігор')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# 3. Різниця в кількості коментарів для позитивних та негативних відгуків
comment_count = df_cs.groupby('voted_up')['comment_count'].sum().reset_index()

plt.figure(figsize=(8, 5))
plt.pie(comment_count['comment_count'], labels=comment_count['voted_up'], autopct='%1.1f%%', colors=['green', 'red'])
plt.title('Кількість коментарів для позитивних та негативних відгуків')
plt.show()

# 4. Середній час, проведений автором у грі, для позитивних та негативних відгуків
average_playtime = df_cs.groupby('voted_up')['author_playtime_forever'].mean().reset_index()

plt.figure(figsize=(8, 5))
plt.bar(average_playtime['voted_up'], average_playtime['author_playtime_forever'], color=['blue', 'orange'])
plt.title('Середній час, проведений у грі, за підтримкою коментаря')
plt.xlabel('Підтримка коментаря')
plt.ylabel('Середній час (години)')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

# 5. Різниця у кількості відгуків між авторами, які отримали гру безкоштовно та тими, хто її купив
purchase_vs_reviews = df_cs.groupby('steam_purchase')['id'].count().reset_index()

plt.figure(figsize=(8, 5))
plt.pie(purchase_vs_reviews['id'], labels=purchase_vs_reviews['steam_purchase'], autopct='%1.1f%%', colors=['purple', 'yellow'])
plt.title('Кількість відгуків за типом покупки')
plt.show()
