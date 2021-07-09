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
Программа выводит информацию по загрузке данных в redis в терминал.
Для того чтобы обратиться к redis по ключу, запустите `redis-cli`, затем введите `GET валюту_отдаю-to-валюту_получаю`. Ключ нужно забирать из ссылок.
```
https://www.bestchange.ru/bitcoin-to-sberbank.html --> bitcoin-to-sberbank
```
