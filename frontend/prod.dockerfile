FROM kiosk-czn-frontend:v2.0

#установка зависимостей
COPY kioskCZNfrontend/ .

ENTRYPOINT ["npm", "quasar", "dev"]