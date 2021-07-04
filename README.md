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
Скрипт будет ждать от вас ссылку формата:
```
https://www.bestchange.ru/bitcoin-to-sberbank.html
```
Программа выводит данные из redis в терминал.
Для того чтобы обратиться к redis по ключу, запустите `redis-cli`, затем введите `GET *валюту_отдаю-to-валюту_получаю*`. Ключ нужно забирать из ссылок, для этого можно воспользоваться html_parser.fetch_exchange_course, либо скопировать вручную:
```
https://www.bestchange.ru/bitcoin-to-sberbank.html --> bitcoin-to-sberbank
```