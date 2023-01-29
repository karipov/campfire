from gtts import gTTS
import os

def speak(mytext):
    language = 'en'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("guide.mp3")
    os.system("mpg321 guide.mp3")
    os.remove("guide.mp3")

if __name__ == "__main__":
    speak("rehaan is a fucking idiot")
