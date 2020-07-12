import time
from datetime import datetime
import requests


def chat_cleaner(text: str):
    bad_words_list = ['spam']  # extend this
    for bad_w in bad_words_list:
        if bad_w in text.split():
            text = text.replace(bad_w, '####')
    return text


def format_message(msg: dict):
    _user = msg['user']
    _dt = datetime.fromtimestamp(msg['time'])
    _show_time = _dt.strftime('%H:%M:%S %d.%m.%Y')
    _txt = chat_cleaner(msg['text'])
    fmt_msg_string = f'{_user} says at {_show_time}: \n {_txt}'
    return fmt_msg_string


after = time.time() - 24 * 60 * 60

while True:
    response = requests.get('http://127.0.0.1:5000/messages', params={'after': after})
    obtained_messages = response.json()['messages']
    for message in obtained_messages:
        print(format_message(message))
        after = message['time']
    time.sleep(1)
