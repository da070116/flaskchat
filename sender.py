import requests

name = input('Name: ').strip()
password = input('Password: ')
print(f"Welcome to chat, {name}! Input \\q to quit")
while True:
    text = input('> ').strip()
    if text == '\\q':
        print(f'Bye, {name}!')
        break
    if 0 < len(text.strip()) < 1024 and len(password) > 0:
        message = {'user': name, 'password': password, 'text': text}
        response = requests.post('http://127.0.0.1:5000/send', json=message)
