FROM kiosk-czn-vacansy-scraper:v2.0

COPY . .

CMD ["python3", "main.py"]