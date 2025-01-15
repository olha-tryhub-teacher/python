QSS = '''
QWidget#mainWindow {
    background-color: #f7ff95;  /* Задаємо фон для головного вікна */
}

QWidget {
    font: 20px "Montserrat";  /* Встановлюємо шрифт для всіх віджетів */
}

QPushButton { 
    background-color: #ffb788;  /* Задаємо фон для кнопки */
    color: black;  /* Колір тексту на кнопці */
}

QPushButton:pressed {
    background-color: #a7694c;  /* Задаємо фон кнопки, коли вона натиснута */
    color: white;
}

QListWidget {
    background-color: #ffffa8;  /* Задаємо фон для списку */
}

QListWidget::item:selected {
    background-color: #e9ea95;  /* Задаємо фон для вибраного елемента списку */
    color: black;
}
'''
