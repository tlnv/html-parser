import html_parser
import get_all_urls
from datetime import datetime
from connect_redis import redis_set_hash

starttime = datetime.now()
exchange_adresses = get_all_urls.get_all_exchange_adresses()
for exchange_adress in exchange_adresses.items():
    starttime = datetime.now()
    exchange_course, rates_required_data = html_parser.parse(exchange_adress)
    redis_set_hash(exchange_course, rates_required_data)
    print(f'{exchange_course} course is done. ')
print(f'Time {datetime.now() - starttime}')
