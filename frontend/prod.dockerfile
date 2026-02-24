FROM kiosk-czn-frontend:v2.0

#установка зависимостей
COPY kioskCZNfrontend/ .

RUN npx quasar prepare

ENTRYPOINT ["npx", "quasar", "dev"]


EXPOSE 9000