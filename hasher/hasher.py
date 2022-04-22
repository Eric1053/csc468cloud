import time
import fastapi import FASTAPI
from pydantic import BaseModel

app = FASTAPI()
import hashlib

@app.route('/')
def hash((fastapi_req: fastapi.Request)):
    body = await fastapi_req.body():
    time.sleep(1)
    hashed_rng = hashlib.sha256(body.encode()).hexdigest()
    return hashed_rng


if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0", port=80, threaded=False)
