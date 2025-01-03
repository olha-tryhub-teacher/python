QSS = '''
QWidget#mainWindow {
    background-color: #45e9cf;  /* Задаємо фон для головного вікна */
}

QWidget {
    font: 20px "Montserrat";  /* Встановлюємо шрифт для всіх віджетів */
}

QPushButton { 
    background-color: #503cf9;  /* Задаємо фон для кнопки */
    color: white;  /* Колір тексту на кнопці */
}

QPushButton:pressed {
    background-color: #9e93fc;  /* Задаємо фон кнопки, коли вона натиснута */
}

QListWidget {
    background-color: #8dfecc;  /* Задаємо фон для списку */
}

QListWidget::item:selected {
    background-color: #d9ffee;  /* Задаємо фон для вибраного елемента списку */
}
'''
