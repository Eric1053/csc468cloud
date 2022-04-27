# import requests
# import time
# import logging
# import mysql.connector

# try:
#     connection = mysql.connector.connect(host='localhost',database='coinminer', user='3306', password='IloveCloud '
#     )
#     cursor = connection.cursor()
# except mysql.connector.Error as error:
#     print("Failed to update".format(error))
# finally:
#     if connection.is_connect():
#         connection.close()
#         print("Mysql is closed")

        
# def get_bitcoin_bytes():
#     r = requests.get("http://rng/randomNumber")
#     return r.content
   
# def hash_bytes(data):
#     r = requests.post("http://hasher/", data=data)
#     hex_hash = r.text
#     return hex_hash

# def work_once():
#     logging.debug("Doing one unit of work")
#     time.sleep(0.1)
#     random_bytes = get_bitcoin_bytes()
#     hex_hash = hash_bytes(random_bytes)
#     if not hex_hash.startswith('0'):
#         logging.debug("No coin found")
#         return
#     logging.info("Coin found: {}...".format(hex_hash[:8]))
#     created  = """INSERT INTO MyPortfolio (CoinType,Quantity) Values("Bitcoin", 6)"""
#     # created = redis.hset("wallet", hex_hash, random_bytes)
#     if not created:
#         logging.info("We already had that coin")


# if __name__ == "__main__":
#     while True:
#         try:
#             work_once()
#         except:
#             logging.exception("In work loop:")
#             logging.error("Waiting 10s and restarting.")
#             time.sleep(10)


import requests
import time
import logging
import mysql.connector
from flask import Flask, Response
app = Flask(__name__)
# try:
#     connection = mysql.connector.connect(host='localhost',database='coinminer',user= ' ', password=' '
#     )
#     cursor = connection.cursor()
# except mysql.connector.Error as error:
#     print("Failed to update".format(error))
# finally:
#     if connection.is_connect():
#         connection.close()
#         print("Mysql is closed")

        
def get_bitcoin_bytes():
    r = requests.get("http://rng/randomNumber")
    return r.content
   
def hash_bytes(data):
    r = requests.post("http://hasher/", data=data)
    hex_hash = r.text
    return hex_hash

# def work_loop(interval=1):
#     deadline = 0
#     loops_done = 0
#     while True:
#         if time.time() > deadline:
#             logging.info("{} units of work done, updating hash counter"
#                      .format(loops_done))
#             loops_done = 0
#             deadline = time.time() + interval
#         work_once()
#         loops_done += 1


# def work_once():
#     logging.debug("Doing one unit of work")
#     time.sleep(0.1)
#     random_bytes = get_bitcoin_bytes()
#     hex_hash = hash_bytes(random_bytes)
#     if not hex_hash.startswith('0'):
#         logging.debug("No coin found")
#         return
#     logging.info("Coin found: {}...".format(hex_hash[:8]))
#     n = 0
#     print("Hashes done {}".format(n+1))
    # created  = """INSERT INTO MyPortfolio (CoinType,Quantity) Values("Bitcoin", "{}")""".format(10)
    # created = redis.hset("wallet", hex_hash, random_bytes)
    # if not created:
    #     logging.info("We already had that coin")

@app.route('/raa')
def work_loop(interval=1):
    deadline = 0
    loops_done = 0
    while True:
        if time.time() > deadline:
            logging.info("{} units of work done, updating hash counter"
                     .format(loops_done))
            loops_done = 0
            deadline = time.time() + interval
        work_once()
        loops_done += 1


def work_once():
    logging.debug("Doing one unit of work")
    time.sleep(0.1)
    random_bytes = get_bitcoin_bytes()
    hex_hash = hash_bytes(random_bytes)
    if not hex_hash.startswith('0'):
        logging.debug("No coin found")
        return
    logging.info("Coin found: {}...".format(hex_hash[:8]))
    n = 0
    print("Hashes done {}".format(n+1))

if __name__ == "__main__":
    while True:
        try:
            work_loop()
        except:
            logging.exception("In work loop:")
            logging.error("Waiting 10s and restarting.")
            time.sleep(10)
