import pandas as pd
import numpy as np
from flask import Flask, render_template
import os


def index():
    data = pd.read_csv("data.csv")
    photo = "photo.jpg" #######
    name = data[data["category"] == "name"]["text"].values[0]
    position = data[data["category"] == "position"]["text"].values[0]
    contacts = data[data["category"] == "contacts"][["text", "link"]].replace({np.nan: None}).values
    summary = data[data["category"] == "summary"]["text"].values[0] # ⬅️⬅️⬅️⬅️⬅️
    skills = data[data["category"] == "skills"]["text"].values
    projects = data[data["category"] == "projects"][["text", "link"]].replace({np.nan: None}).values
    education = data[data["category"] == "education"]["text"].values
    achievements = data[data["category"] == "achievements"]["text"].values
    facts = data[data["category"] == "facts"]["text"].values

    return render_template("index.html", name=name, photo=photo,#########
                           position=position, summary=summary,
                           contacts=contacts, skills=skills,
                           projects=projects,
                           education=education, achievements=achievements,
                           facts=facts)


folder = os.getcwd() # запам'ятали поточну робочу папку
app = Flask(__name__, template_folder=folder, static_folder=folder)
app.add_url_rule("/", "index", index)

app.run()
