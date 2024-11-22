import pandas as pd
from sklearn.model_selection import train_test_split  # Імпортуємо функцію для розділення даних на тренувальну і тестову вибірки
from sklearn.preprocessing import StandardScaler  # Імпортуємо StandardScaler для нормалізації даних
from sklearn.neighbors import KNeighborsClassifier  # Імпортуємо K-Nearest Neighbors Classifier
from sklearn.metrics import confusion_matrix, accuracy_score  # Імпортуємо метрики оцінки моделі

df = pd.read_csv("train.csv")
print(df.info())


# Заповнюємо пропущені дати народження медіанним роком
df["bdate"] = pd.to_datetime(df["bdate"], errors="coerce")
df["bdate_year"] = df["bdate"].dt.year.fillna(df["bdate"].dt.year.median())

# Створюємо ознаку віку
current_year = 2024
df["age"] = current_year - df["bdate_year"]

# Чи працює користувач
df["is_employed"] = df["career_end"] > df["career_start"]

df.drop(["id", "last_seen", "langs", "bdate", "career_end", "career_start"], axis=1, inplace=True)

def remove_False_life_main(row):
    if row["life_main"] == "False":
        return -1
    return int(row["life_main"])
def remove_False_people_main(row):
    if row["people_main"] == "False":
        return -1
    return int(row["people_main"])

df["life_main"] = df.apply(remove_False_life_main, axis=1)
df["people_main"] = df.apply(remove_False_people_main, axis=1)

print(df.info())

# One-hot encoding для категоріальних змінних
df = pd.get_dummies(df, columns=["education_form", "education_status", "occupation_type"], drop_first=True)


# Вибір цільової змінної та ознак

# Розділення даних

# Навчання моделі

