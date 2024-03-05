import os
import shutil
from datetime import datetime
import requests

if __name__ == "__main__":

    def backup(): 
        # src folder
        src = "D:/Desktop/copy/src/12"

        # dst folder
        dst = "D:/Desktop/copy/dst"

        # Date Format
        date_format = "Date_%Y-%m-%d_Time_%H-%M-%S_Name"   

        # today
        today = datetime.today().strftime(date_format)

        # New folder name
        new_name = f"{today}_{os.path.basename(src)}"

        # folder existance check
        if not os.path.exists(dst):
            os.makedirs(dst)

        # copy folder
        shutil.copytree(src, os.path.join(dst, new_name))

        print(f"Папка успешно скопирована в {os.path.join(dst, new_name)}")

        # Telegram bot token
        bot_token = "**********:************_**********************"

        # Telegram chat id
        chat_id = "-*********"

        # Telegram Message text
        text = f"Папка успешно скопирована в {os.path.join(dst, new_name)}"

        
        # URL-adress API Telegram
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"

        # sending request
        requests.get(url)

    
    backup()
