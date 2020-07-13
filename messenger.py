import time
from datetime import datetime

from PyQt5 import QtWidgets, QtCore
from clientui import UiMainWindow
import requests


def send_to_server(user: str, password: str, text: str):
    message = {'user': user, 'password': password, 'text': text}
    response = requests.post('http://127.0.0.1:5000/send', json=message)
    return response.status_code


def format_message(msg: dict):
    _user = msg['user']
    _dt = datetime.fromtimestamp(msg['time'])
    _show_time = _dt.strftime('%H:%M:%S %d.%m.%Y')
    _txt = msg['text']
    fmt_msg_string = f'<strong>{_user} says at {_show_time}</strong>: <br/> {_txt} <br/><br/>'
    return fmt_msg_string


class MessengerApp(QtWidgets.QMainWindow, UiMainWindow):

    def __init__(self):
        super().__init__()
        self.setup_ui(self)
        self.after = time.time() - 24 * 60 * 60
        self.sendButton.pressed.connect(self._btn_pressed)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.upload_messages)
        self.timer.start(1000)

    def write_text(self, message):
        self.textBrowser.append(format_message(message))
        self.textBrowser.repaint()

    def upload_messages(self):
        response = requests.get('http://127.0.0.1:5000/messages', params={'after': self.after})
        obtained_messages = response.json()['messages']
        for message in obtained_messages:
            self.write_text(message)
            self.after = message['time']

    def _btn_pressed(self):
        user = self.login_field.text().strip()
        password = self.password_field.text()
        text = self.textEdit.toPlainText().strip()
        if len(text) > 0 and len(user) > 0 and len(password) > 0:
            try:
                reply = send_to_server(user, password, text)
                if reply == 200:
                    self.textEdit.clear()
                    self.statusbar.showMessage("")
                elif reply == 401:
                    self.statusbar.showMessage("Unauthorized access")
                else:
                    self.statusbar.showMessage(f"Error: server returns {reply}")
            except (ConnectionRefusedError, Exception):
                self.statusbar.showMessage(f"Server unavailable :(")


app = QtWidgets.QApplication([])
window = MessengerApp()
window.show()
app.exec_()
