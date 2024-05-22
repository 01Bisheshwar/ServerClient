from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(_name_)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    emit('message', message, broadcast=True)

if _name_ == '_main_':
    socketio.run(app, host='0.0.0.0', port=8765)