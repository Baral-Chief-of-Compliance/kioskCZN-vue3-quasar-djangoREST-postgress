FROM python:3.13-slim

RUN mkdir -p /home/staff-scraper

WORKDIR /home/staff-scraper

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["python3", "--version"]