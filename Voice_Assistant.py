import pyttsx3  # text to speech converter
import speech_recognition as sr
import webbrowser  # for web search
import datetime
import pyjokes
import os
import time
from ttsvoice import tts


def sp_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nBol sun rha hu...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Samjhne de...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("kuch bola bhi tune ???")


def tx_speech(data):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 150)
    engine.say(data)
    engine.runAndWait()
    print("\n---->  Executed Successfully\n")


def txt_speech(string):
    tts(string, "male")
    print("\n---->  Executed Successfully\n")


if __name__ == '__main__':
    data1 = sp_text()
    if data1:
        data1 = data1.lower()
        if "sun" in data1:
            while True:
                data2= sp_text()
                if "your name" in data2:
                    name = " My name is Bablu. "
                    print(name)
                    tx_speech(name)

                elif "my name" in data2:
                    m_name = " Your name is Nikhil."
                    print(m_name)
                    tx_speech(m_name)

                elif "time" in data2:
                    time = datetime.datetime.now().strftime("%I:%M %p")
                    print(time)
                    tx_speech(time)

                elif "youtube" in data2:
                    print("open youtube")
                    webbrowser.open("https://www.youtube.com/")

                elif "instagram" in data2:
                    print("Opening Instagram")
                    webbrowser.open("https://www.instagram.com/?utm_source=pwa_homescreen&__pwa=1")

                elif "joke" in data2:
                    joke_1 = pyjokes.get_joke(language='en', category='neutral')
                    print(joke_1)
                    tx_speech(joke_1)

                elif "play song" in data2:
                    add = "C:\\Voiceover\\songs"
                    listsong = os.listdir(add)
                    print(list)
                    os.startfile(os.path.join(add, listsong[0]))

                elif "exit" in data2:
                    tx_speech("Exiting\nThank you ")
                    break

                else:
                    print("Samjh nhi aaya bapas bol")
        else:
            print("Mujhe bola kya ???\nBtata toh sunna h")
    else:
        print("Kuch toh bolta...")

# time = datetime.datetime.now().strftime("%I:%M %p")
# print(time)
# txt_speech(time)
# txt_speech("Rakshita paagal ")
# joke_1 = pyjokes.get_joke(language= 'en', category= 'neutral')
# print(joke_1)
# txt_speech(joke_1)
# add = "C:\\Voiceover\\songs"
# listsong = os.listdir(add)
# print(listsong)
# os.startfile(os.path.join(add,listsong[0]))
#time.sleep(5)