import time
from flask import Flask
import hashlib
app = Flask(__name__)
@app.route('/')
def hash(int):
    time.sleep(1)
    hashed_rng = hashlib.sha256(int.encode()).hexdigest()
    return hashed_rng


if __name__ == '__main__':
    from waitress import serve
    app.run(debug = True, host="0.0.0.0", port=80, threaded=False)
