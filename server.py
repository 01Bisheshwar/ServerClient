from flask import Flask, render_template
import asyncio
import websockets
import threading

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

async def websocket_handler(websocket, path):
    async for message in websocket:
        print(f"received message: {message}")
        await websocket.send(message)  # Echo the message back

def start_websocket_server():
    asyncio.set_event_loop(asyncio.new_event_loop())
    start_server = websockets.serve(websocket_handler, "0.0.0.0", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    threading.Thread(target=start_websocket_server).start()
    app.run(host='0.0.0.0', port=10000)
