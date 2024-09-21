import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# Скільки коштує (Price) найдешевший платний додаток (Type == 'Paid)?
print("✨Найдешевший додаток коштує✨")
print(df[df["Type"] == "Paid"]["Price"].min())

# Чому дорівнює медіанна (median) кількість установок (Installs)
# додатків із категорії (Category) "ART_AND_DESIGN"?
print("✨Медіана встановлень додатків категорії ART_AND_DESIGN✨")
print(df[df["Category"] == "ART_AND_DESIGN"]["Installs"].median())

# На скільки максимальна кількість відгуків (Reviews) для безкоштовних програм (Type == 'Free')
# більше максимальної кількості відгуків для платних програм (Type == 'Paid')?
print("✨Різниця максимальної кількості відгуків✨")
print(df[df["Type"] == "Free"]["Reviews"].max() - df[df["Type"] == "Paid"]["Reviews"].max())

# Який мінімальний розмір (Size) програми для тинейджерів (Content Rating == 'Teen')?
print("✨Мінімальний розмір програми для тинейджерів✨")
print(df[df["Content Rating"] == "Teen"]["Size"].min())

# *До якої категорії (Category) відноситься додаток із найбільшою кількістю відгуків (Reviews)?
max_rew = df["Reviews"].max()
print("✨Категорія додатку із найбільшою кількістю відгуків✨")
print(df[df["Reviews"] == max_rew]["Category"])

# *Який середній (mean) рейтинг (Rating) додатків вартістю (Price) понад 20 доларів
# з кількістю установок (Installs) понад 10000?
print("✨Середній рейтинг додатків партістю понад 20 доларів, встановлених понад 10 000 разів✨")
print(df[(df["Price"]>20) & (df["Installs"] > 10000)]["Rating"].mean())
