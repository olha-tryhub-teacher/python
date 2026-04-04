while True:
    password = input("Введіть пароль:")
    if len(password) <= 8:
        print("Пароль надто короткий.")
        continue
    print("Пароль прийнятий.")
    break
