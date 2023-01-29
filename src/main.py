import plants
import time
from picamera2 import Picamera2
from libcamera import Transform
import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN)
print("[DEBUG] bot object set up")

print("[DEBUG] setting up camera...")
camera = Picamera2()
cam_config = camera.create_still_configuration(transform=Transform(180))
camera.set_controls({"ExposureTime": 100000, "Sharpness": 2.0,
                     "Brightness": 0.1})
camera.configure(cam_config)
camera.start()
print("[DEBUG] camera set up")
print("[DEBUG] warming up the camera...")
time.sleep(2)

def take_picture():
    name = "images/" + str(round(time.time())) + ".jpg"
    print("[INFO] capturing photo, say cheese!")
    camera.capture_file(name)
    print("[INFO] saved photo", name)
    return name

def send_picture(path):
    print("[INFO] sending photo", path, "...")
    photo = open(path, "rb")
    # identification = plants.identify_plant(path)
    bot.send_photo(config.CHAT_ID, photo)
    # bot.send_message(config.CHAT_ID, identification)
    print("[INFO] photo sent to", config.CHAT_ID)

@bot.message_handler(commands=["photo"])
def main(message):
    picture = take_picture()
    send_picture(picture)


bot.polling() 
