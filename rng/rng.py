# from flask import Flask, Response
# import socket
# import time
# from faker import Faker
# from urllib.request import urlopen
# app = Flask(__name__)
# hostname = socket.gethostname()
# fake = Faker()

# @app.route('/')
# def index():
#     return "RNG running on {}\n".format(hostname)

# @app.route('/randomNumber')
# def number():
#     time.sleep(1)
#     rng = str(fake.random_int(min=100, max=100000))
#     return Response(rng, 
#     content_type= "text/octet-stream")
# if __name__ == '__main__':
#     app.run(debug = True, host="0.0.0.0", port=80, threaded=False)
    
    
from flask import Flask, Response
import os
import socket
import time

app = Flask(__name__)

# Enable debugging if the DEBUG environment variable is set and starts with Y
app.debug = os.environ.get("DEBUG", "").lower().startswith('y')

hostname = socket.gethostname()

urandom = os.open("/dev/urandom", os.O_RDONLY)


@app.route("/")
def index():
    return "RNG running on {}\n".format(hostname)


@app.route("/<int:how_many_bytes>")
def rng(how_many_bytes):
    # Simulate a little bit of delay
    time.sleep(0.1)
    return Response(
        os.read(urandom, how_many_bytes),
        content_type="application/octet-stream")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=False)
