# Executes by executing "env FLASK_APP=flask-server.py python3 -m flask run"
# first define the file in an environment variable and then flask run
# do flask run --host=0.0.0.0 for executing available in the network
from flask import Flask, escape, request, render_template, send_from_directory
from flask_socketio import SocketIO
from gpiozero import Motor
import time

motor1 = Motor(27, 17)
motor2 = Motor(24, 23)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    return send_from_directory('statics', 'index.html')

@socketio.on('move_motors')
def handle_message(data):
    left = data['data']['left']
    right = data['data']['right']

    print('left: ' + str(left))
    print('right: ' + str(right))

    if left > 0:
        motor1.forward(left)
    elif left < 0:
        motor1.backward(abs(left))
    else:
        motor1.stop()

    if right > 0:
        motor2.forward(right)
    elif right < 0:
        motor2.backward(abs(right))
    else:
        motor2.stop()
    
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=49152)
    #running in localhost:5000 default


