# Real-Time Random Array Generator with Flask and MongoDB

## Project Overview

This project is a real-time web application that generates random arrays using NumPy and sends them to connected clients in real-time via WebSockets, implemented using Flask and Flask-SocketIO. The application also stores the generated arrays in a MongoDB database for future reference.

### Key Features
- **Random Array Generation**: 
  - Generate random arrays with a configurable size (minimum 10,000) and number range (default: 0-99,999).
  - Allow users to specify the size of the array and the range of random numbers.
- **Real-Time Updates**:
  - Send the generated random arrays to all connected clients in real-time using WebSockets (via Flask-SocketIO).
  - Dynamically update the front-end display as new arrays are generated.
- **Array Storage**:
  - Store each generated array in MongoDB for future reference.
  - Allow users to view previously generated arrays from the database.

## Installation and Setup Instructions

### Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- Flask
- Flask-SocketIO
- NumPy
- MongoDB
- pymongo
- eventlet (for WebSocket support)
- Socket.IO

### Setting Up the Environment

1. **Clone the Repository**:

   ```bash
   git clone <repository-link>
   cd <project-folder>