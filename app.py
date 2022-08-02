import asyncio
from src import app, socketio
from src._general.utils import context_initializer
import threading


# context_initializer.Initializer()
# threading.Thread(target=context_initializer.DeviceErrorThread().device_error_search).start()
if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)

