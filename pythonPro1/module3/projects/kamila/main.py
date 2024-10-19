import pandas as pd
df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
pd.set_option("display.max_columns", 20)
pd.set_option("display.width", 1000)

# Найгірша якість сну за професією
worst_sleep_by_occupation = df.groupby("Occupation")["Quality of Sleep"].min()
print(worst_sleep_by_occupation)

# Найкраща якість сну за професією
best_sleep_by_occupation = df.groupby("Occupation")["Quality of Sleep"].max()
print(best_sleep_by_occupation)

# Найгірша якість сну за віком
worst_sleep_by_age = df.groupby("Age")["Quality of Sleep"].min()
print(worst_sleep_by_age)

# Найкраща якість сну за віком
best_sleep_by_age = df.groupby("Age")["Quality of Sleep"].max()
print(best_sleep_by_age)

# Найгірша якість сну за статтю
worst_sleep_by_gender = df.groupby("Gender")["Quality of Sleep"].min()
print(worst_sleep_by_gender)

# Найкраща якість сну за статтю
best_sleep_by_gender = df.groupby("Gender")["Quality of Sleep"].max()
print(best_sleep_by_gender)

# Відповідь на залежність від фізичної активності
activity_sleep_correlation = df["Physical Activity Level"].corr(df["Quality of Sleep"])
print(activity_sleep_correlation)

# Відповідь на залежність від індексу ваги тіла (BMI Category)
bmi_sleep_relationship = df.groupby("BMI Category")["Quality of Sleep"].mean()
print(bmi_sleep_relationship)

# Обчислюємо середню тривалість сну за віком
avg_sleep_duration_by_age = df.groupby("Age")["Sleep Duration"].mean()
print(avg_sleep_duration_by_age)

# Обчислюємо середню якість сну за віком
avg_quality_of_sleep_by_age = df.groupby("Age")["Quality of Sleep"].mean()
print(avg_quality_of_sleep_by_age)
