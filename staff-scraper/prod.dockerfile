FROM kiosk-czn-staff-scraper:v2.0

COPY . .

CMD ["python3", "main.py"]