import pandas as pd

# Завантаження даних
df_cs = pd.read_csv('csgo_steam_reviews.csv')

# Перевірка наявності пропущених значень в колонці review
df_cs['review'] = df_cs['review'].fillna('')  # Заміна NaN на пусті рядки
df_cs['review_length'] = df_cs['review'].apply(len)  # Обчислення довжини відгуку

# Конвертація стовпця created у формат дати та часу
df_cs['created'] = pd.to_datetime(df_cs['created'])

# Витягуємо години з дати та часу
df_cs['hour'] = df_cs['created'].dt.hour

# 1. Чи є залежність між часом написання відгуку та його середньою довжиною?
# Витягуємо години з дати та часу
average_length_by_hour = df_cs.groupby('hour')['review_length'].mean().reset_index()

# 2. Чи впливає підтримку коментаря кількість ігор, що належать автору?
games_owned_vs_voted = df_cs[['author.num_games_owned', 'voted_up']].groupby(by="voted_up")['author.num_games_owned'].mean()

# 3. Чи є різниця в кількості коментарів для позитивних і негативних відгуків?
comment_count = df_cs.groupby('voted_up')['comment_count'].sum().reset_index()

# 4. Яка середня кількість часу, проведеного автором у грі, для позитивних та негативних відгуків?
average_playtime = df_cs.groupby('voted_up')['author_playtime_forever'].mean().reset_index()

# 5. Чи є різниця у кількості відгуків між авторами, які отримали гру безкоштовно та тими, хто її купив?
purchase_vs_reviews = df_cs.groupby('steam_purchase')['id'].count().reset_index()

# Результати
results = {
    'и є залежність між часом написання відгуку та його середньою довжиною?': average_length_by_hour,
    'Чи впливає підтримку коментаря кількість ігор, що належать автору?': games_owned_vs_voted,
    'Чи є різниця в кількості коментарів для позитивних і негативних відгуків?': comment_count,
    'Яка середня кількість часу, проведеного автором у грі, для позитивних та негативних відгуків?': average_playtime,
    'Чи є різниця у кількості відгуків між авторами, які отримали гру безкоштовно та тими, хто її купив?': purchase_vs_reviews
}

# Вивід результатів
for title, result in results.items():
    print(f"\n{title}:\n{result}\n")
