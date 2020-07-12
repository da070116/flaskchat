import time
from datetime import datetime
from flask import Flask, __version__, request, abort
from source import filter_dict

app = Flask(__name__)

messages_list = [
    dict(user="Guido", time=4000, text="I've created a new program language"),
    dict(user="Tim", time=7000, text="Hmm...  Beautiful is better than ugly. Guido, add something?"),
    dict(user="Guido", time=4000, text="No, 19 is a good number"),
    dict(user="John Doe", time=datetime.now().timestamp() - 4000, text="Spam? " * 3),
    dict(user="Jane Doe", time=datetime.now().timestamp() - 2000, text="Eggs! " * 3),
]

users_dict = {
    'Guido': 'HetWilgelmus',
    'Tim': '1920Zen',
    'John': 'Doe',
    'Jane': 'Doe'
}



@app.route('/users')
def users():
    usernames = list(users_dict.keys())
    return {'users': usernames}


@app.route('/')
def hello():
    return f"<h1> <a href='/state'>Flask {__version__}</a></h1"


@app.route('/state')
def state():
    date_now = datetime.now()
    return {
        'status': True,
        'name': 'Flask chat',
        'total_messages': len(messages_list),
        'total_users': len(users_dict),
        'server_time': f'{date_now:%H:%M:%S  %d.%m.%Y }'
    }


@app.route("/send", methods=['POST'])
def send():
    user = request.json['user']
    password = request.json['password']
    text = request.json['text']
    if user in users_dict:
        if users_dict[user] != password:
            abort(401)
    else:
        users_dict[user] = password
    messages_list.append(dict(user=user, time=time.time(), text=text))
    return {'ok': True}


@app.route('/messages')
def messages_view():
    after = float(request.args['after'])
    filtered = filter_dict(messages_list, 'time', after)
    return {'messages': filtered}


app.run()
