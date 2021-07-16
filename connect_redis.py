import redis
import json


redis_host = 'localhost'
redis_port = 6379


def redis_set_string(exchange_course, exchange_course_data):
    try:
        rates_base = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        rates_base.set(exchange_course, json.dumps(exchange_course_data, ensure_ascii=False))
    except Exception as e:
        print(e)


def redis_set_hash(exchange_course, city, city_exchange_course_data):
    try:
        rates_base = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        rates_base.hset(exchange_course, city, json.dumps(city_exchange_course_data, ensure_ascii=False))
    except Exception as e:
        print(e)