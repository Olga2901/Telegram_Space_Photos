import os
import time
import telegram


def upload_images_to_telegram(telegram_token, chat_name, update_period):
    bot = telegram.Bot(token = telegram_token)
    chat_id = bot.get_chat(chat_name, timeout = 100)["id"]
    pic_path = "directory"
    for dir_counter in os.listdir(pic_path):
        for inner_pic_path in os.listdir(f"{pic_path}/{dir_counter}"):
            photo_path = f"{pic_path}/{dir_counter}/{inner_pic_path}"
            with open(photo_path, "rb") as photo:
                bot.send_photo(
                    chat_id = chat_id,
                    photo = photo,
                    timeout = 3000
            )
            time.sleep(update_period)


def main():
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    chat_name = os.getenv("TELEGRAM_CHANNEL")
    update_period = int(os.getenv("TIMER_PERIOD", default = 15000))
    upload_images_to_telegram(telegram_token, chat_name, update_period)

if __name__ == "__main__":
    main()
