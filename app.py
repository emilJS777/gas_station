from src import app
from src._general.utils import context_initializer
import threading


# context_initializer.Initializer()
# threading.Thread(target=context_initializer.DeviceErrorThread).start()
if __name__ == '__main__':
    app.run(debug=True, port=5000)
