current_year = 2024
df2["age"] = current_year - df2["bdate_year"]

# Чи працює користувач
df2["is_employed"] = df2["career_end"] > df2["career_start"]

df2.drop(["id", "last_seen", "langs", "bdate",
          "career_end", "career_start"], axis=1, inplace=True)

df2["life_main"] = df2.apply(remove_False_life_main, axis=1)
df2["people_main"] = df2.apply(remove_False_people_main, axis=1)

# One-hot encoding для категоріальних змінних
df2 = pd.get_dummies(df2, columns=["education_form", "education_status", "occupation_type"], drop_first=True)


# класифікуємо ці данні
y_pred2 = classifier.predict(df2)

# формуємо датафрейм із двох стовпчиків
result = pd.DataFrame({'id': ID, 'result': y_pred2})

# зберігаємо в окреми CSV файл наш  результат із лише двома стовпчиками
result.to_csv("result.csv", index=False)
