import sys, ast
from PyQt5.QtWidgets import QApplication, QCheckBox, QLabel, QPushButton, QRadioButton, QVBoxLayout, QWidget, QGridLayout  #, QFileDia
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import pyqtSlot

widgets = {
    "price": [],
    "logo": [],
    "buttonCAE": [],
}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Komes Software")
window.setFixedWidth(1000)
# window.move(700, 200)
window.setStyleSheet(
    "background: #fff;")  # Spróbować to zrobić w zewnętrznym pliku CSS

grid = QGridLayout()


def clear_widgets():
    ''' hide all existing widgets and erase
        them from the global dictionary'''
    for widget in widgets:
        if widgets[widget] != []:
            widgets[widget][-1].hide()
        for i in range(0, len(widgets[widget])):
            widgets[widget].pop()


def show_frame1():
    '''display welcome frame'''
    clear_widgets()
    welcome_frame()


@pyqtSlot()
def print_allert():
    print('dziala')


def start_choosing():
    '''display choosing frame'''
    clear_widgets()
    choosing_frame()


def create_button(label):
    """ Function that handle creating buttons with styling """
    button = QPushButton(label)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet("*{border: 4px solid '#BC006C';" +
                         "border-radius: 15px;" + "font-size: 25px;" +
                         "color: 'black';" + "padding: 5px 0;" +
                         "margin: 5px 10px;}" +
                         "*:hover{background: '#BC006C';" + "color: white;}")
    return button


def get_button_text(button):
    return button.text()


def welcome_frame():
    """Function that is responsible for the welcome screen. The frame consists of buttons responsible for navigating to another frame and for displaying choosen modules to offer"""

    # Display Logo
    image = QPixmap("logo.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 20px;")

    # Headers
    leftHeader = QLabel("Wybierz program")
    rightHeader = QLabel("Wybrane")
    headers = [leftHeader, rightHeader]
    for header in headers:
        header.setStyleSheet("font-size: 30px;" + "color: #02119B;" +
                             "margin: auto;")

    # Button widget
    buttonNFX = create_button("Midas NFX")
    buttonMF = create_button("Midas MeshFree")
    buttonCAE = create_button("CAE LIMIT")
    buttonSDC = create_button("SDC Verifier")
    buttonMW = create_button("DEP MeshWorks")

    # buttons callback
    # buttonCAE.clicked.connect(choosing_frame("CAE LIMIT"))
    buttonCAE.clicked.connect(print_allert)
    widgets["buttonCAE"].append(buttonCAE)

    grid.addWidget(logo, 0, 2)
    grid.addWidget(leftHeader, 1, 0)
    grid.addWidget(rightHeader, 1, 3)
    grid.addWidget(buttonNFX, 2, 0)
    grid.addWidget(buttonMF, 3, 0)
    grid.addWidget(widgets["buttonCAE"][-1], 4, 0)
    grid.addWidget(buttonSDC, 5, 0)
    grid.addWidget(buttonMW, 6, 0)


def choosing_frame(choosen):
    """ Funcion that handle displaying detail module choosing tool for the particular software """

    # clearance
    clear_widgets()

    # Stored pricelists
    with open('prices/versions/{}.txt'.format(choosen), 'r') as v_prices:
        contents = v_prices.read()
        V_pricing = ast.literal_eval(contents)

    with open('prices/modules/{}.txt'.format(choosen), 'r') as v_prices:
        contents = v_prices.read()
        M_pricing = ast.literal_eval(contents)

    # Display Logo
    image = QPixmap("logo.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 20px;")

    # Radio butons that enable user to choose between perpetual and one-year license
    perpetual_license = QRadioButton("licencja wieczysta")
    yearly_license = QRadioButton("licencja roczna")

    # Headers
    leftHeader = QLabel("Wersja")
    mediumHeader = QLabel("Moduł")
    rightHeader = QLabel("Cena")

    # Exception - CAE LIMIT doesn't have versions and modules but has modules and interfaces
    if choosen == "CAE":
        mediumHeader = QLabel("Interfejs")
        leftHeader = QLabel("Moduł")

    headers = [
        leftHeader, mediumHeader, rightHeader, perpetual_license,
        yearly_license
    ]
    for header in headers:
        header.setStyleSheet("font-size: 30px;" + "color: #02119B;" +
                             "margin: 10px 25px;")

    # print(versions)

    grid.addWidget(logo, 0, 1)
    grid.addWidget(perpetual_license, 1, 0)
    grid.addWidget(yearly_license, 1, 2)
    grid.addWidget(leftHeader, 2, 0)
    grid.addWidget(mediumHeader, 2, 1)
    grid.addWidget(rightHeader, 2, 2)

    # Versions;
    versions = []
    for version in V_pricing:
        versions.append(QCheckBox(version))
        iterator = list(V_pricing.keys()).index(version)
        versions[iterator].setStyleSheet("font-size: 22px;" +
                                         "margin: 10px 35px;")
        grid.addWidget(versions[iterator], iterator + 3, 0)

    # Modules;
    modules = []

    for module in M_pricing:
        modules.append(QCheckBox(module))
        iterator = list(M_pricing.keys()).index(module)
        modules[iterator].setStyleSheet("font-size: 22px;" +
                                        "margin: 10px 35px;")
        grid.addWidget(modules[iterator], iterator + 3, 1)

    sum_price = 0
    price_label = logo = QLabel(str(sum_price) + "€")
    price_label.setStyleSheet("font-size: 30px;" + "margin: 10px 35px;" +
                              "text-decoration: bold;")
    grid.addWidget(price_label, 3, 2)

    # Buttons
    calculate_button = QPushButton("Oblicz")
    add_to_offer_button = QPushButton("Dodaj")
    buttons = [calculate_button, add_to_offer_button]
    for button in buttons:

        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet("*{border: 4px solid '#BC006C';" +
                             "border-radius: 15px;" + "font-size: 25px;" +
                             "color: 'black';" + "padding: 5px 0;" +
                             "margin: 5px 10px;}" +
                             "*:hover{background: '#BC006C';" +
                             "color: 'white'}")

    grid.addWidget(calculate_button, 4, 2)
    grid.addWidget(add_to_offer_button, 5, 2)


welcome_frame()

# choosing_frame()

window.setLayout(grid)

window.show()
sys.exit(app.exec())
