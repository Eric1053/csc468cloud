# import time
# import hashlib
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hash(int):
#     time.sleep(1)
#     hashed_rng = hashlib.sha256(int.encode()).hexdigest()
#     return hashed_rng


# if __name__ == '__main__':
#     app.run(debug = True, host="0.0.0.0", port=80, threaded=False)
require 'digest'
require 'sinatra'
require 'socket'

set :bind, '0.0.0.0'
set :port, 80

post '/' do
    # Simulate a bit of delay
    sleep 0.1
    content_type 'text/plain'
    "#{Digest::SHA2.new().update(request.body.read)}"
end

get '/' do
    "HASHER running on #{Socket.gethostname}\n"
end
