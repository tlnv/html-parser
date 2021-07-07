import html_parser
import get_all_urls
from connect_redis import redis_set_hash


urls = get_all_urls.get_all_exchange_urls()
print(len(urls))
for url in urls:
    exchange_course, rates_required_data = html_parser.parse(url)
    redis_set_hash(exchange_course, rates_required_data)
    print(f'{exchange_course} course is done')
