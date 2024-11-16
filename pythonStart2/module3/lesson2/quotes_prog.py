# 1
with open("quotes.txt", "r", encoding="utf-8") as file:
    data = file.read()
print(data)
# 2
author = input("Хто написав цей вірш?")
# 3
with open("quotes.txt", "a", encoding="utf-8") as file:
    file.write("\n(" + author + ")")


with open("quotes.txt", "r", encoding="utf-8") as file:
    data = file.read()
print(data)
