
from text_detection_video import text_video
import threading
from flask import Flask


app = Flask(__name__)



@app.route('/')
def hello():

    return "Hello world!"


if __name__ == '__main__':
    t1 = threading.Thread(target=text_video)
    t1.daemon = True
    t1.start()

    app.run(host='0.0.0.0', port=5000, debug=True)