FROM python:3.9 
ADD main.py / 
ADD html_parser.py /
ADD get_all_urls.py /
ADD connect_redis.py /
ADD browser_imitation.py /
ADD chromedriver.exe /
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]