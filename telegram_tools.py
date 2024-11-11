def publish_photo(bot, chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)
    print(f'Фото опубликовано: {photo_path}')
