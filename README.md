# Telegram_Space_Photos
Sends photos of space to the channel telegram from 3 sources

# Что делает
Cкрипты для скачивания в папку directory фото из сервисов NASA и SpaceX и отправки фотографий в телеграмм канал через бота.

# Как запустить
Для запуска требуется установленный Python версии 3.6 и выше.

- Скачайте код
- Установите зависимости из requirements.txt
```
pip install -r requirements.txt
```
# Скачивание фото SpaceX

- Запустите скрипт вставив ID нужного вам запуска:
```
python fetch_spacex_images.py -l [id]
```
- Если не указан ID, то скрипт скачает фото с последнего запуска, указан.
```
python fetch_spacex_images.py
```

# Скачивание фото APOD-фото NASA

- Получить API токен <a href="https://api.nasa.gov/#signUp%D1%8F" target="_blank">тут</a>
- Создать переменную окружения `NASA_TOKEN` и поместить в нее полученный токен
- Запустить скрипт, указав желаемое кол-во фото для скачивания 
```
python get_nasa_days_pictures.py -c 50
```
- Если кол-во не указано, то устанавливается кол-во по умолчанию равное 50
```
python get_nasa_days_pictures.py
```
# Скачивание фото EPIC-фото NASA

- Получить API токен <a href="https://api.nasa.gov/#signUp%D1%8F" target="_blank">тут</a>
- Создать переменную окружения `NASA_TOKEN` и поместить в нее полученный токен
- Запустить скрипт
```
python download_epic_photo_earth.py
```

# Отправка фото в ТГ бота
- Через телеграм бота @BotFather создать бота
- Получить API-токен созданного бота
- Создать телеграмм канал и бота сделать администратором
- Создайте переменные окружения для бота API-токена `TELEGRAM_TOKEN`=5922771341:AAH95oxSSJV36WveqOjgTzOCUDq1mTXIIeo
и чат-ID для канала `TELEGRAM_CHANNEL`= @spacephotosnasa
- Запустить скрипт указав желаемый интервал публикации фото
```
python upload_images_to_telegram.py -t время
```
- Если время не указано, то устанавливается время по умолчанию равное 4 часам
```
python upload_images_to_telegram.py
```
# Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
