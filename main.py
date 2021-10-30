import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QGridLayout  #, QFileDia
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QCursor

widgets = {
    "logo": [],
    "button": [],
}

choosen = {}

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Komes Software")
window.setFixedWidth(1000)
# window.move(700, 200)
window.setStyleSheet(
    "background: #161219;")  # Spróbować to zrobić w zewnętrznym pliku CSS

grid = QGridLayout()


def frame1():
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


frame1()

# def frame2():

window.setLayout(grid)

window.show()
sys.exit(app.exec())
