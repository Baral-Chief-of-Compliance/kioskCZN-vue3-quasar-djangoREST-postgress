## Парсер старниц телефонного справочника
Каким то образом парсить через request библу python не получается 
Выдает страницу vipnet координатора, поэтому было принято решение 
написать на go модуль для скачивания страниц с телефоного справочника 
под каждый кц

#### Подготовка

он лежит в корне под названием go-parser-from-phone-book
ему нужен env файл .env так же в корне проекта

```
URL=http://localhost/phones2 
```

так как проект запускается на сервре, на котором и есть телефонный справочник

```bash
chmod 777 ./go-parser-from-phone-book

chmod -R 777 logs # если папка logs уже есть
```

#### Добавляем его исполнение в cron

```bash
crontab -e
Добавляем 0 * * * * cd  /var/www/kioskCZN-vue3-quasar-djangoREST-postgress-main/kioskCZN-vue3-quasar-djangoREST-postgress-main && ./go-parser-from-phone-book

grep CRON /var/log/syslog - работает ли
```

И теперь страницы с телефонных справочников находятся в phones_book_page