import pandas as pd
df = pd.read_csv("CourseraDataset-Clean.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# Залежність оцінки від розкладу (гнучкість графіку навчання)
# Групуємо курси за графіком і обчислюємо середню оцінку для кожного розкладу
rating_by_schedule = df.groupby("Schedule")["Rating"].mean()
print(rating_by_schedule)


# топ 10 найбільш розповсюджених скілів для навчання
# Розділяємо скіли за комами
df["Skill gain"] = df["Skill gain"].fillna("")
skills_series = df["Skill gain"].str.split(",").explode()
# Рахуємо частоту кожного скілу
most_common_skills = skills_series.value_counts().head(11)

print(most_common_skills)


# топ 10 найбільш частих тематик (Keyword) для курсу
most_common_keyword = df["Keyword"].value_counts().head(10)

print(most_common_keyword)

# чи є залежність між рівнем складності курсу (Beginner, Intermediate) та його оцінкою
rating_by_level = df.groupby("Level")["Rating"].mean()
print(rating_by_level)

# Чи впливає тривалість курсу на його рейтинг
df["Duration to complete (Approx.)"] = pd.to_numeric(df["Duration to complete (Approx.)"], errors='coerce')
rating_by_duration = df.groupby(pd.cut(df["Duration to complete (Approx.)"], bins=10))["Rating"].mean()

print(rating_by_duration)
