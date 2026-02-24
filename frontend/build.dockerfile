FROM node:24-bullseye-slim


RUN mkdir -p /home/frontend

WORKDIR /home/frontend

# Копируем package-lock.jsonв контейнер
COPY kioskCZNfrontend/package-lock.json .

# Копируем package.json контейнер
COPY kioskCZNfrontend/package.json .


# Устанавливаем зависимости
RUN npm ci --ignore-scripts || npm install --force


# Проверяем версию Node.js при запуске контейнера
CMD ["node", "--version"]