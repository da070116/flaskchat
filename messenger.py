from PyQt5 import QtWidgets
from clientui import Ui_MainWindow
from sender import send_to_server


class MessengerApp(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sendButton.pressed.connect(self._btn_pressed)

    def _btn_pressed(self):
        user = self.login_field.text().strip()
        password = self.password_field.text()
        text = self.textEdit.toPlainText().strip()
        if len(text) > 0:
            send_to_server(user, password, text)
        self.textEdit.clear()


app = QtWidgets.QApplication([])
window = MessengerApp()
window.show()
app.exec_()
