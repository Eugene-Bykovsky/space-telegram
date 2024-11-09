# Space Telegram

**Space Telegram** — это набор скриптов для скачивания и публикации фотографий о космосе. Скрипты позволяют автоматически получать фотографии запусков SpaceX, снимки EPIC и APOD от NASA, а затем публиковать их в Telegram-канале. Скрипты также поддерживают циклическую публикацию всех фотографий из заданной директории с заданным интервалом.

### Как установить

1. **Получите API-ключи**:
   - **NASA API**: Для получения фотографий от NASA (EPIC и APOD) вам понадобится API-ключ. Получить ключи можно на сайтах https://api.nasa.gov/#apod и https://api.nasa.gov/#epic.
   - **Telegram Bot Token**: Создайте бота через [BotFather](https://core.telegram.org/bots#botfather) в Telegram и получите токен.
   
2. **Склонируйте репозиторий на свой компьютер:**  
``` git clone git@github.com:Eugene-Bykovsky/devman.git ```  

3. **Перейдите в папку со скриптами:**  
``` cd devman ```

4. **Установите виртуальное окружение и активируйте его:**  
``` python3 -m venv venv ```  
``` source venv/bin/activate ```

5. **Перейдите в папку  с проектом:**  
``` cd web-api/space-telegram```  

6. **Создайте файл `.env`** в корневой директории проекта и добавьте в него следующие ключи:

   ```
   TELEGRAM_TOKEN=ваш_токен_бота
   TELEGRAM_CHAT_ID=ваш_идентификатор_канала
   APOD_NASA_API_KEY=ваш_apod_ключ_от_NASA
   EPIC_NASA_API_KEY=ваш_epic_ключ_от_NASA
   PUBLISH_DELAY_HOURS = задержка_публикации
   ```

7. **Установите зависимости:**:
   ```
   pip install -r requirements.txt
   ```
   
### Как запустить

Примеры запуска скриптов:

```
python fetch_apod_images.py

python fetch_epic_images.py

python fetch_spacex_images.py --launch_id 5eb87d47ffd86e000604b38a 

python publish_photo.py

python publish_random_photo_on_schedule.py ./apod_images --delay 1

```

### Цели проекта

Данный проект написан для образовательных целей.