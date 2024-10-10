import eventlet
eventlet.monkey_patch()

from flask import Flask, render_template
from flask_socketio import SocketIO
import numpy as np
import pymongo

app = Flask(__name__)
socketio = SocketIO(app)

# Set up MongoDB connection
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['array_db']
collection = db['arrays']

# HTTP Route for main page
@app.route('/')
def index():
    return render_template('index.html')

# WebSocket to generate and emit random arrays
@socketio.on('generate_array')
def generate_array(data):
    size = int(data.get('size', 10000))
    range_min = int(data.get('range_min', 0))
    range_max = int(data.get('range_max', 99999))

    # Generate random array using NumPy
    random_array = np.random.randint(range_min, range_max, size).tolist()

    # Store array in MongoDB
    collection.insert_one({'array': random_array})

    # Send the generated array to all connected clients
    socketio.emit('array_generated', {'array': random_array})

# WebSocket to get previously generated arrays
@socketio.on('get_previous_arrays')
def get_previous_arrays():
    previous_arrays = list(collection.find({}, {'_id': 0, 'array': 1}))
    socketio.emit('previous_arrays', previous_arrays)

if __name__ == '__main__':
    # Use SocketIO's eventlet server to run the app
    socketio.run(app, debug=True)
