from datetime import datetime
from flask import Flask, __version__

app = Flask(__name__)


@app.route('/')
def hello():
    return f"<h1> <a href='/state'>Flask {__version__}</a></h1"


@app.route('/state')
def state():
    current_datetime = datetime.now()
    return {
        'status': 'True',
        'name': 'Flask chat',
        'time': f'{current_datetime:%H:%M:%S  %d.%m.%Y }'
    }


app.run()
