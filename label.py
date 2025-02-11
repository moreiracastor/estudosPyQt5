import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, Pixma

from PyQt5.QtCore import Qt 

class telaLabel(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Teste label")

        # <-------------- Definição de tamanho Fixo da tela -------------->
        self.setFixedWidth(400)
        self.setFixedHeight(600)

        texto = QLabel("Hello Word!")
        fonte = texto.font()

        fonte.setPointSize(30) # Tamanho da fonte do label
        texto.setFont(fonte) # Não entendi essa parte
        texto.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Alinha no eixo x no meio e no meio y no meio, logo alinha ao centro da tela

        self.setCentralWidget(texto) # Não entendi essa

app = QApplication(sys.argv)

tela = telaLabel()

tela.show()
app.exec()