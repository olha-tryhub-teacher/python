import pandas as pd
import matplotlib.pyplot as plt

# Завантаження даних
df = pd.read_csv("CourseraDataset-Clean.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# Залежність оцінки від розкладу (гнучкість графіку навчання)
rating_by_schedule = df.groupby("Schedule")["Rating"].mean()
print(rating_by_schedule)

plt.figure(figsize=(10, 5))
rating_by_schedule.plot(kind='bar', color='skyblue')
plt.title("Середня оцінка за графіком навчання")
plt.xlabel("Графік навчання")
plt.ylabel("Середня оцінка")
plt.xticks(rotation=45)
plt.show()

# Топ 10 найбільш розповсюджених скілів для навчання
df["Skill gain"] = df["Skill gain"].fillna("")
skills_series = df["Skill gain"].str.split(",").explode()
most_common_skills = skills_series.value_counts().head(10)

print(most_common_skills)

plt.figure(figsize=(10, 5))
most_common_skills.plot(kind='bar', color='orange')
plt.title("Топ 10 найбільш розповсюджених скілів")
plt.xlabel("Скіли")
plt.ylabel("Частота")
plt.xticks(rotation=45)
plt.show()

# Топ 10 найбільш частих тематик (Keyword) для курсу
most_common_keyword = df["Keyword"].value_counts().head(10)
print(most_common_keyword)

plt.figure(figsize=(10, 5))
most_common_keyword.plot(kind='bar', color='green')
plt.title("Топ 10 найбільш частих тематик")
plt.xlabel("Тематики")
plt.ylabel("Частота")
plt.xticks(rotation=45)
plt.show()

# Залежність між рівнем складності курсу (Beginner, Intermediate) та його оцінкою
rating_by_level = df.groupby("Level")["Rating"].mean()
print(rating_by_level)

plt.figure(figsize=(8, 5))
rating_by_level.plot(kind='bar', color='purple')
plt.title("Середня оцінка за рівнем складності курсу")
plt.xlabel("Рівень складності")
plt.ylabel("Середня оцінка")
plt.xticks(rotation=0)
plt.show()

# Чи впливає тривалість курсу на його рейтинг
df["Duration to complete (Approx.)"] = pd.to_numeric(df["Duration to complete (Approx.)"], errors='coerce')
rating_by_duration = df.groupby(pd.cut(df["Duration to complete (Approx.)"], bins=10))["Rating"].mean()

print(rating_by_duration)

plt.figure(figsize=(10, 5))
rating_by_duration.plot(kind='line', marker='o', color='blue')
plt.title("Середня оцінка за тривалістю курсу")
plt.xlabel("Тривалість курсу (біновані)")
plt.ylabel("Середня оцінка")
plt.xticks(rotation=45)
plt.show()
