# [ЗМІНА] Створено інтерфейс кнопок керування внизу екрана
            BoxLayout:
                size_hint: 1, None
                height: dp(100)
                padding: dp(20)
                spacing: dp(20)

                # Кнопка ВЛІВО
                MDIconButton:
                    icon: "arrow-left-bold"
                    icon_size: "50dp"
                    # При натисканні змінюємо стан у словнику на True, при відпусканні - на False
                    on_press: root.keys["left"] = True
                    on_release: root.keys["left"] = False

                # Кнопка ВПРАВО
                MDIconButton:
                    icon: "arrow-right-bold"
                    icon_size: "50dp"
                    on_press: root.keys["right"] = True
                    on_release: root.keys["right"] = False

                # Пустий віджет, щоб розділити стрілки і кнопку пострілу
                Widget:

                # Кнопка ВОГОНЬ
                MDIconButton:
                    icon: "fire"
                    icon_size: "50dp"
                    # Використовуємо червоний колір для кнопки пострілу, що відповідає темі
                    theme_icon_color: "Custom"
                    icon_color: 1, 0, 0, 1
                    # Одразу викликаємо метод стрільби
                    on_press: root.fire()
