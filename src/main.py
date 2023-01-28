import time
from picamera import PiCamera
import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
print("[DEBUG] bot object set up")

camera = PiCamera()
camera.resolution(720, 720)
print("[DEBUG] camera set up")
print("[DEBUG] camera resolution: " + str(camera.resolution))
print("[DEBUG] camera zoom: " + str(camera.zoom))

print("[DEBUG] warming up the camera...")
time.sleep(2)

def take_picture():
    name = str(round(time.time())) + ".jpg"
    print("[INFO] capturing photo, say cheese!")
    camera.capture(name)
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


    
