import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

# <-------------- Class da Tela --------------> 
class telaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv) # Criação da janela

tela = telaPrincipal() # Criação do objeto da janela 

tela.show() # Função que mostra a tela

app.exec() # Executa a janela