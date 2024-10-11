import pandas as pd
df = pd.read_csv('GoogleApps.csv')
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)


# 1 Скільки всього програм з категорією ('Category') 'BUSINESS'?
print("💅🏻Завдання 1💅🏻")
res = ...
print(res)


# 2 Чому дорівнює співвідношення кількості додатків для підлітків ('Teen') і для дітей старше 10 ('Everyone 10+')?
# Відповідь запиши з точністю до сотих.
print("💅🏻Завдання 2💅🏻")
res1 = ...
res2 = ...
print(round(res1 / res2, 2))

# 3.1 Чому дорівнює середній рейтинг ('Rating') платних ('Type' == 'Paid') додатків?
# Відповідь запиши з точністю до сотих.
print("💅🏻Завдання 3.1💅🏻")
res1 = ...
print(round(res1, 2))

# 3.2 На скільки середній рейтинг ('Rating') безкоштовних ('Free') додатків менший за середній рейтинг платних ('Type' == 'Paid')?
# Відповідь запиши з точністю до сотих.
print("💅🏻Завдання 3.2💅🏻")
res2 = ...
print(round(res1 - res2, 2))

# 4 Чому дорівнює мінімальний та максимальний розмір ('Size') додатків у категорії ('Category') 'COMICS'?
# Запиши відповіді з точністю до сотих.
print("💅🏻Завдання 4💅🏻")
min_size = ...
max_size = ...
print("Min size", round(min_size, 2))
print("Max size", max_size)

# Бонус 1. Скільки додатків з рейтингом ('Rating') більше 4.5 у категорії ('Category') 'FINANCE'?
print("💅🏻Бонусне завдання 1💅🏻")
res = ...
print(res)

# Бонус 2. Чому дорівнює співвідношення безкоштовних ('Free') і платних ('Paid') ігор з рейтингом ('Rating') більше 4.9?
print("💅🏻Бонусне завдання 2💅🏻")
free_apps = ...
paid_apps = ...
print(free_apps/paid_apps)
