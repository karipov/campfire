import time
import RPi.GPIO as GPIO
from picamera2 import Picamera2
from libcamera import Transform
import telebot

import config

bot = telebot.TeleBot(config.BOT_TOKEN)
print("[INFO] bot object set up")

print("[INFO] setting up camera...")
camera = Picamera2()
cam_config = camera.create_still_configuration(transform=Transform())
camera.set_controls({"ExposureTime": 100000, "Sharpness": 2.0,
                     "Brightness": 0.1})
camera.configure(cam_config)
camera.start()
print("[INFO] camera set up")
print("[INFO] warming up the camera...")
time.sleep(2)
print("[INFO] camera warmed up, ready for pictures")

def take_picture():
    name = "images/" + str(round(time.time())) + ".jpg"
    print("[INFO] capturing photo, say cheese!")
    camera.capture_file(name)
    print("[INFO] saved photo", name)
    return name

def process_picture(path):
    print("[INFO] processing photo", path, "...")
    photo = open(path, "rb")

    bot.send_photo(config.CHAT_ID, photo)
    print("[INFO] photo sent to", config.CHAT_ID)

if __name__ == "__main__":
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    while True:
        if GPIO.input(10) == GPIO.HIGH:
            print("[INFO] detected a press!")
            picture = take_picture()
            process_picture(picture)

    GPIO.cleanup()
