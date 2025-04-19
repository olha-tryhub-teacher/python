import pandas as pd
import numpy as np

data = pd.read_csv("data.csv")

name = data[data["category"] == "name"]["text"].values
position = data[data["category"] == "position"]["text"].values
contacts = data[data["category"] == "contacts"][["text", "link"]].replace({np.nan: None}).values
skills = data[data["category"] == "skills"]["text"].values
projects = data[data["category"] == "projects"][["text", "link"]].replace({np.nan: None}).values
education = data[data["category"] == "education"]["text"].values
achievements = data[data["category"] == "achievements"]["text"].values
facts = data[data["category"] == "facts"]["text"].values

print(name)
print(position)
print(contacts)
print(skills)
print(projects)
print(education)
print(achievements)
print(facts)
