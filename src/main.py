import time
from picamera2 import Picamera2
import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
print("[DEBUG] bot object set up")

print("[DEBUG] setting up camera...")
camera = Picamera2()
print("[DEBUG] camera set up")
print("[DEBUG] warming up the camera...")
time.sleep(2)

def take_picture():
    name = str(round(time.time())) + ".jpg"
    print("[INFO] capturing photo, say cheese!")
    camera.start_and_capture_file(name, show_preview=False)
    print("[INFO] saved photo", name)
    return name

def send_picture(path):
    print("[INFO] sending photo", path, "...")
    photo = open(path, "rb")
    bot.send_photo(config.CHAT_ID, photo)
    print("[INFO] photo sent to", config.CHAT_ID)

@bot.message_handler(commands=["photo"])
def main(message):
    picture = take_picture()
    send_picture(picture)


bot.polling() 
