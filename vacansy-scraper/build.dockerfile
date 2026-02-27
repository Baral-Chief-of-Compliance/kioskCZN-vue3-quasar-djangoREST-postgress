FROM python:3.13-slim

RUN mkdir -p /home/vacansy-scraper

WORKDIR /home/vacansy-scraper

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["python3", "--version"]