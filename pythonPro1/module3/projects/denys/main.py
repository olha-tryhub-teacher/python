import pandas as pd

full_df = pd.read_csv("steam.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# порахуємо кількість додатків для кожного жанру (екшон, інді, кежуал і т.д.) серед усього датасету
genres_split = full_df["genres"].str.split(";", expand=True)  # Розділяємо жанри по ";"
all_genres = genres_split.stack()  # Перетворюємо "розтягнутий" датафрейм у список
genres_counts = all_genres.value_counts()  # Підраховуємо частоту кожного жанру
print(genres_counts)

# середній час гри відповідно до жанру
full_df["genres_split"] = full_df["genres"].str.split(";") # Розбиваємо жанри за ";"
df_genres = full_df.explode("genres_split") # Розтягуємо жанри у окремі рядки
# Порахуємо середній та медіанний час гри і ціну по жанрам
average_playtime_by_genre = df_genres.groupby("genres_split")[["average_playtime", "median_playtime", "price"]].mean()
print(average_playtime_by_genre)

# відфільтруємо лише ті ігри, в жанрах яких є інді
df = full_df[full_df["genres"].str.contains("Indie")]

# порахуємо кількість додатків для кожної платформи (віндовс, пс, лінукс і т.д.)
app_per_platform = df.groupby(by="platforms")["name"].count().sort_values(ascending=False)
print(app_per_platform)

# порахуємо кількість додатків для кожної категорії (віндовс, пс, лінукс і т.д.)
categories_split = df["categories"].str.split(";", expand=True)  # Розділяємо категорії по ";"
all_categories = categories_split.stack()  # Перетворюємо "розтягнутий" датафрейм у список
category_counts = all_categories.value_counts()  # Підраховуємо частоту кожної категорії
print(category_counts)

# Порахуємо кількість інді ігор за кожний рік (1997-2018)
df["release_date"] = pd.to_datetime(df["release_date"])  # Перетворюємо стовпчик release_date у формат datetime
df["year"] = df["release_date"].dt.year  # Виділяємо рік
df_filtered = df[df["year"] <= 2018]  # Фільтруємо записи, починаючи з 2014 року
count_per_year = df_filtered.groupby("year")["name"].count()  # Підраховуємо кількість інді ігор за кожний рік
print(count_per_year)

# ідея для графіку: дослідити залежність ціни до кількості часу гри


