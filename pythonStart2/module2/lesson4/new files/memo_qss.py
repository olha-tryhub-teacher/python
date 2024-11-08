# Оформлення
QSS = '''
QPushButton { 
    background-color: rgb(210, 210, 210); 
    border-width: 1px;
    border-radius: 10px;
    border-color: gray;
    font: 11px "Montserrat";
    min-width: 10em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: gray;
    border-style: inset;
}
QGroupBox {
    color: gray;
    font: 14px;
    border-radius: 7px;
    border: 2px solid gray;
    margin-top: 2ex;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 3px;
}

QRadioButton {
    font: bold 14px;
}
QRadioButton::indicator {
    width: 14px;
    height: 14px;
    border-radius: 7px;
}
QRadioButton::indicator::unchecked {
    border: 2px solid; 
    border-color: gray;
    background-color: white;
    border-radius: 7px;
}

QRadioButton::indicator:unchecked:hover {
    border-color: black;
    background-color: white;
    border-radius: 7px;
}

QRadioButton::indicator::checked {
    border: 1px; 
    border-color: green;
    background-color: green;
    border-radius: 7px;
}

QLabel { 
    font: 11px "Montserrat";
}
'''

QSS_OK = '''
QPushButton { background-color: rgb(70, 150, 70); 
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: bold 18px "Montserrat";
    min-width: 10em;
    padding: 6px;
}
QPushButton:pressed {
    background-color: gray;
    border-style: inset;
}
'''

QSS_TextCardQuestion = '''QLabel { 
    font: bold 26px "Montserrat";
}'''

QSS_TextResult = '''QLabel {
    font: italic 22px "Montserrat";
}'''

QSS_TextHeader = '''QLabel {
    font: 18px ;
}'''
