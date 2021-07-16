# HTML Parser для Bestchange

### Как установить

Для установки используйте:
```
pip install -r requirements.txt
```

### Как запустить
```
$ python main.py 
```
После запуска скрипт пишет данные по обмену кэша в разных городах, выводит в терминал `валюту-отдаю-to-валютe-получаю in код-города is done` после успешной записи. Периодически программа будет оттормаживаться и запускать Chrome, чтобы обойти блокировку парсинга. 
Запись в базу идет в виде хеш-таблиц, следующего вида:
```
{exchange_course: {city_code: { exchanger_name: {pay: pay_value, get: get_value, reserve: reserve_value}}}}
```
Например:
```
{bitcoin-to-dollar-cash: {beij: { BestObmen {pay: 1 BTC, get: 12 USD, reserve: 900}}}
```
Так как в redis вложенные хеш-таблицы недоступны, напрямую вытащить можно либо все обменники во всех городах по направлению: `HGETALL bitcoin-to-dollar-cash`, либо все обменники в одном городе: `HGET bitcoin-to-dollar-cash beij`.
