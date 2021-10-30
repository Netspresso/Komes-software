import sys, ast
from PyQt5.QtWidgets import QApplication, QCheckBox, QLabel, QPushButton, QRadioButton, QVBoxLayout, QWidget, QGridLayout  #, QFileDia
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QCursor

widgets = {
    "logo": [],
    "button": [],
}

# Stored pricelists
with open('NFX_V.txt', 'r') as NFX_prices:
    contents = NFX_prices.read()
    NFX_V_pricing = ast.literal_eval(contents)

with open('NFX_M.txt', 'r') as NFX_prices:
    contents = NFX_prices.read()
    NFX_M_pricing = ast.literal_eval(contents)

# for line in lines:
#     NFX_V_pricing[]

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Komes Software")
window.setFixedWidth(1000)
# window.move(700, 200)
window.setStyleSheet(
    "background: #fff;")  # Spróbować to zrobić w zewnętrznym pliku CSS

grid = QGridLayout()


def welcome_frame():
    """Function that is responsible for the welcome screen. The frame consists of buttons responsible for navigating to another frame and for displaying choosen modules to offer"""

    # Display Logo
    image = QPixmap("logo.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 20px;")
    widgets["logo"].append(logo)

    # Headers
    leftHeader = QLabel("Wybierz program")
    rightHeader = QLabel("Wybrane")
    headers = [leftHeader, rightHeader]
    for header in headers:
        header.setStyleSheet("font-size: 30px;" + "color: #02119B;" +
                             "margin: auto;")

    # Button widget
    buttonNFX = QPushButton("Midas NFX")
    buttonMF = QPushButton("Midas MeshFree")
    buttonCAE = QPushButton("CAE LIMIT")
    buttonSDC = QPushButton("SDC Verifier")
    buttonMW = QPushButton("DEP MeshWorks")
    buttons = [buttonNFX, buttonMF, buttonCAE, buttonSDC, buttonMW]

    for button in buttons:

        button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        button.setStyleSheet("*{border: 4px solid '#BC006C';" +
                             "border-radius: 15px;" + "font-size: 25px;" +
                             "color: 'white';" + "padding: 5px 0;" +
                             "margin: 5px 10px;}" +
                             "*:hover{background: '#BC006C';}")
        widgets["button"].append(button)

    grid.addWidget(widgets["logo"][-1], 0, 2)
    grid.addWidget(leftHeader, 1, 0)
    grid.addWidget(rightHeader, 1, 3)
    grid.addWidget(buttonNFX, 2, 0)
    grid.addWidget(buttonMF, 3, 0)
    grid.addWidget(buttonCAE, 4, 0)
    grid.addWidget(buttonSDC, 5, 0)
    grid.addWidget(buttonMW, 6, 0)


# welcome_frame1()


def choosing_frame():
    """ Funcion that handle displaying detail module choosing tool for the particular software """

    # Display Logo
    image = QPixmap("logo.jpg")
    logo = QLabel()
    logo.setPixmap(image)
    logo.setAlignment(QtCore.Qt.AlignCenter)
    logo.setStyleSheet("margin-top: 20px;")
    widgets["logo"].append(logo)

    # Radio butons that enable user to choose between perpetual and one-year license
    perpetual_license = QRadioButton("licencja wieczysta")
    yearly_license = QRadioButton("licencja roczna")

    # Headers
    leftHeader = QLabel("Wersja")
    mediumHeader = QLabel("Moduł")
    rightHeader = QLabel("Cena")
    headers = [
        leftHeader, mediumHeader, rightHeader, perpetual_license,
        yearly_license
    ]
    for header in headers:
        header.setStyleSheet("font-size: 30px;" + "color: #02119B;" +
                             "margin: 10px 25px;")

    # print(versions)

    grid.addWidget(widgets["logo"][-1], 0, 1)
    grid.addWidget(perpetual_license, 1, 0)
    grid.addWidget(yearly_license, 1, 2)
    grid.addWidget(leftHeader, 2, 0)
    grid.addWidget(mediumHeader, 2, 1)
    grid.addWidget(rightHeader, 2, 2)

    # Versions;
    versions = []
    for version in NFX_V_pricing:
        versions.append(QCheckBox(version))
        iterator = list(NFX_V_pricing.keys()).index(version)
        versions[iterator].setStyleSheet("font-size: 22px;" +
                                         "margin: 10px 35px;")
        grid.addWidget(versions[iterator], iterator + 3, 0)

    # Modules;
    modules = []

    for module in NFX_M_pricing:
        modules.append(QCheckBox(module))
        iterator = list(NFX_M_pricing.keys()).index(module)
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


choosing_frame()

window.setLayout(grid)

window.show()
sys.exit(app.exec())
