import pandas as pd
df = pd.read_csv('GoogleApps.csv')
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)


# 1 Виведи на екран мінімальний, середній та максимальний рейтинг ('Rating') платних та безкоштовних програм ('Type') з точністю до десятих.
print("💅🏻Завдання 1💅🏻")
res = df.groupby(by="Type")["Rating"].agg(["min", "mean", "max"])
print(round(res, 1))

# 2 Виведи на екран мінімальну, медіанну (median) та максимальну ціну ('Price') платних додатків (Type == 'Paid') для
# різних цільових аудиторій ('Content Rating')
print("💅🏻Завдання 2💅🏻")
res = df[df["Type"] == "Paid"].groupby(by="Content Rating")["Price"].agg(["min", "median", "max"])
print(res)

# 3 Згрупуй дані за категорією ('Category') та цільовою аудиторією ('Content Rating') будь-яким зручним для тебе способом
# Порахуй максимальну кількість відгуків ('Reviews') у кожній групі.
# Порівняй результати для категорій 'EDUCATION', 'FAMILY' та 'GAME':
# У якій віковій групі найбільше відгуків отримала програма з категорії 'EDUCATION'? 'FAMILY'? 'GAME'?
# Підказка: ти можеш вибрати з DataFrame кілька стовпців одночасно за допомогою такого синтаксису:
# df [[<стовпець 1>, <стовпець 2>, <стовпець 3>]]
print("💅🏻Завдання 3💅🏻")
res = df.pivot_table(index='Content Rating', columns='Category', values='Reviews', aggfunc='max')
print(res[['EDUCATION', 'FAMILY', 'GAME']])


# 4 Згрупуй платні (Type == 'Paid') програми за категорією ('Category') та цільовою аудиторією ('Content Rating')
# Порахуй середню кількість відгуків ('Reviews') у кожній групі
# Зверніть увагу, що в деяких клітинках отриманої таблиці відображається не число, а значення "NaN" - Not a Number
# Цей запис означає, що в цій групі немає жодної програми.
# Вибери назви категорій, в яких є платні програми для всіх вікових груп і розташуй їх в алфавітному порядку.
print("💅🏻Завдання 4💅🏻")
res = df[df["Type"] == "Paid"].pivot_table(index="Category", columns="Content Rating", values="Reviews", aggfunc="mean")
print(res)

# Бонусне завдання. Знайди категорії безкоштовних (Type == 'Free') додатків,
# у яких програми розроблені не для всіх вікових груп ('Content Rating')
print("💅🏻Бонусне завдання💅🏻")
res = df[df["Type"] == "Free"].pivot_table(index="Category", columns="Content Rating", values="Reviews", aggfunc="mean")
print(res)
