import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
from PyQt5.QtCore import Qt, QTimer
import random
import string  

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Carrega o layout da interface gráfica da tela splash a partir do arquivo .ui
        uic.loadUi('splash.ui', self)
        
        # Remove as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)
        
        # Define a transparência da janela (sem fundo sólido)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Define a opacidade da janela (ajuste conforme necessário)
        self.setWindowOpacity(0.9)

        # Conecta o botão de geração de senha à função 'generate_password'
        self.generateButton.clicked.connect(self.generate_password)

        # Conecta o botão de copiar senha à função 'copy_password'
        self.copyButton.clicked.connect(self.copy_password)

        # Conecta o botão de limpar campos à função 'clear_fields'
        self.clearButton.clicked.connect(self.clear_fields)
        
        # Inicializa o label de mensagem de cópia como vazio
        self.copyMessageLabel.setText("")

        # Conecta o botão de sair à função de fechar a janela
        self.exitButton.clicked.connect(self.close)

    def generate_password(self):
        # Obtém os valores de configuração da senha a partir dos inputs do usuário
        length = self.lengthSpinBox.value()  # Tamanho da senha
        include_uppercase = self.uppercaseCheckBox.isChecked()  # Incluir letras maiúsculas
        include_lowercase = self.lowercaseCheckBox.isChecked()  # Incluir letras minúsculas
        include_digits = self.digitsCheckBox.isChecked()  # Incluir números
        include_symbols = self.symbolsCheckBox.isChecked()  # Incluir símbolos

        # Verifica se pelo menos uma opção foi selecionada, caso contrário, exibe um aviso
        if not any([include_uppercase, include_lowercase, include_digits, include_symbols]):
            QMessageBox.warning(self, "Opção Inválida", "Selecione pelo menos uma opção de caractere para a senha.")
            return

        # Cria o conjunto de caracteres possíveis para a senha com base nas opções selecionadas
        characters = ""
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation
        
        # Gera a senha aleatória com o tamanho e caracteres especificados
        password = ''.join(random.choice(characters) for i in range(length))
        self.passwordLineEdit.setText(password)  # Exibe a senha gerada no campo de texto

        # Limpa a mensagem de cópia anterior
        self.copyMessageLabel.setText("")

    def copy_password(self):
        # Copia a senha gerada para a área de transferência
        clipboard = QApplication.clipboard()
        clipboard.setText(self.passwordLineEdit.text())

        # Exibe uma mensagem de que a senha foi copiada
        self.copyMessageLabel.setText("Senha copiada!")

        # Define um temporizador para limpar a mensagem de cópia após 3 segundos
        QTimer.singleShot(3000, self.clear_copy_message)
        
    def clear_copy_message(self):
        # Limpa a mensagem de cópia
        self.copyMessageLabel.setText("")
    
    def clear_fields(self):
        # Limpa todos os campos e mensagens da interface
        self.passwordLineEdit.clear()  # Limpa o campo da senha gerada
        self.copyMessageLabel.setText("")  # Limpa a mensagem de cópia
        self.uppercaseCheckBox.setChecked(False)  # Desmarca a opção de maiúsculas
        self.lowercaseCheckBox.setChecked(False)  # Desmarca a opção de minúsculas
        self.digitsCheckBox.setChecked(False)  # Desmarca a opção de números
        self.symbolsCheckBox.setChecked(False)  # Desmarca a opção de símbolos
        self.lengthSpinBox.setValue(0)  # Redefine o tamanho da senha para 0

if __name__ == '__main__':
    # Inicializa a aplicação
    app = QApplication(sys.argv)
    
    # Cria a tela splash e exibe
    splash = SplashScreen()
    splash.show()
    
    # Inicia o loop da aplicação
    sys.exit(app.exec_())
