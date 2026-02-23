FROM node:lts-alpine3.22


RUN mkdir -p /home/frontend

WORKDIR /home/frontend

# Копируем директорию kioskCZNfrontend в контейнер
COPY kioskCZNfrontend/ .

# Устанавливаем зависимости
RUN npm install

# Проверяем версию Node.js при запуске контейнера
CMD ["node", "--version"]