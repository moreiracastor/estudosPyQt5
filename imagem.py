import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap

from time import sleep

class telaImagem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Teste de Imagem")
        self.setFixedWidth(400) # eixo x
        self.setFixedHeight(600) # eixo y

        global imagem

        imagem = QLabel("Gato", self)

        imagem.setPixmap(QPixmap('gatao.jpeg'))
        imagem.setScaledContents(True) # Estica a imagem pra caber no tamanho definido da tela

        imagem.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Define as posições onde a imagem irá aparecer

        self.setCentralWidget(imagem) # Não sei pra que serve

    # def teste(self):
    #     sleep(5)
    #     imagem = QLabel("Funcionou?", self) depois eu testo



app = QApplication(sys.argv)

tela = telaImagem()
tela.show()


app.exec()