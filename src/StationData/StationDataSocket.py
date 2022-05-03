from flask_socketio import send, emit, join_room
from src.Auth import auth_middleware
from src import socketio
from flask import g, request

# connected_user_ids = []
sids = []

# CONNECT
@socketio.on('connect')
def connect():
    sids.append(request.sid)
    print(request.sid, "errrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrooom")
    print('connect ****************')


# DISCONNECT
@socketio.on('disconnect')
def disconnect():
    print('disconnect ***************')


# CREATE FRIEND REQUEST
# @auth_middleware.check_authorize
def send_data(data):
    # pass
    emit('stationData', data, namespace=False, broadcast=True)


