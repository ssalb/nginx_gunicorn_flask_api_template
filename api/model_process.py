from src.model import Model
import config
import time

db = redis.StrictRedis(host=config.DB_HOST, port=config.DB_PORT, db=config.DB_ID)

if __name__=="__main__":

    while True:
        time.sleep(config.SERVER_SLEEP)
