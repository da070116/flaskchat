import requests


def send_to_server(user: str, password: str, text: str):
    message = {'user': user, 'password': password, 'text': text}
    response = requests.post('http://127.0.0.1:5000/send', json=message)
    return response.status_code
