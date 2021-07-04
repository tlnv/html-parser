import redis
import json
from pprint import pprint


redis_host = 'localhost'
redis_port = 6379


def redis_set_hash(exchange_course, exchange_course_data):
    try:
        rates_base = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        rates_base.set(exchange_course, json.dumps(exchange_course_data, ensure_ascii=False))
        print(rates_base.get(exchange_course))
    except Exception as e:
        print(e)
