import pyttsx3  # Text-to-speech conversion library
import speech_recognition as sr  # Speech recognition library
import webbrowser  # For opening web pages
import datetime  # For getting the current time
import pyjokes  # For generating jokes
import os  # For interacting with the operating system (e.g., listing files)
import time  # For adding delays
from ttsvoice import tts  # Custom module for text-to-speech conversion

def sp_text():
    """
    This function captures audio from the microphone and converts it to text using Google's speech recognition.
    It listens for the user's speech and attempts to recognize and transcribe it.
    """
    recognizer = sr.Recognizer()  # Create a Recognizer instance
    with sr.Microphone() as source:  # Use the microphone as the audio source
        print("\nBol sun rha hu...")  # Prompt in Hindi: "Speak, I am listening..."
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise to improve recognition accuracy
        audio = recognizer.listen(source)  # Listen for the first phrase and extract it into audio data
        try:
            print("Samjhne de...")  # Prompt in Hindi: "Let me understand..."
            data = recognizer.recognize_google(audio)  # Recognize the speech using Google's speech recognition
            print(data)  # Print the recognized text
            return data  # Return the recognized text
        except sr.UnknownValueError:  # Handle unrecognized speech
            print("kuch bola bhi tune ???")  # Prompt in Hindi: "Did you even say anything?"

def tx_speech(data):
    """
    This function converts text to speech using pyttsx3.
    It takes a string of text as input and reads it aloud.
    """
    engine = pyttsx3.init()  # Initialize the pyttsx3 engine
    voices = engine.getProperty("voices")  # Get available voices
    engine.setProperty("voice", voices[0].id)  # Set the voice to the first available voice
    rate = engine.getProperty("rate")  # Get the current speaking rate
    engine.setProperty("rate", 150)  # Set the speaking rate to 150 words per minute
    engine.say(data)  # Queue the text to be spoken
    engine.runAndWait()  # Process the speech commands
    print("\n---->  Executed Successfully\n")  # Print a success message

def txt_speech(string):
    """
    This function converts text to speech using a custom tts function from the ttsvoice module.
    It takes a string of text as input and reads it aloud.
    """
    tts(string, "male")  # Call the custom tts function with the text and a specified voice
    print("\n---->  Executed Successfully\n")  # Print a success message

if __name__ == '__main__':
    data1 = sp_text()  # Capture and recognize speech input

    if data1:  # If speech was recognized
        data1 = data1.lower()  # Convert the recognized text to lowercase for easier comparison

        if "sun" in data1:  # Check if the recognized text contains the word "sun" (e.g., to start listening for commands)

            while True:
                data2 = sp_text()# Capture additional speech input

                if data2:  # If speech was recognized
                    data2 = data2.lower()  # Convert the recognized text to lowercase for easier comparison

                    if "your name" in data2:  # Respond to a query about the program's name
                        name = " My name is Bablu. "
                        print(name)
                        tx_speech(name)

                    elif "my name" in data2:  # Respond to a query about the user's name
                        m_name = " Your name is Nikhil."
                        print(m_name)
                        tx_speech(m_name)

                    elif "time" in data2:  # Provide the current time
                        time = datetime.datetime.now().strftime("%I:%M %p")  # Get the current time in a specific format
                        print(time)
                        tx_speech(time)

                    elif "youtube" in data2:  # Open YouTube in the web browser
                        print("open youtube")
                        webbrowser.open("https://www.youtube.com/")

                    elif "instagram" in data2:  # Open Instagram in the web browser
                        print("Opening Instagram")
                        webbrowser.open("https://www.instagram.com/?utm_source=pwa_homescreen&__pwa=1")

                    elif "joke" in data2:  # Tell a joke
                        joke_1 = pyjokes.get_joke(language='en', category='neutral')  # Get a neutral joke in English
                        print(joke_1)
                        tx_speech(joke_1)

                    elif "play song" in data2:  # Play a song from a specified directory
                        add = "C:\\Voiceover\\songs"  # Specify the directory path
                        listsong = os.listdir(add)  # Get a list of files in the specified directory
                        print(listsong)  # Print the list of files
                        os.startfile(os.path.join(add, listsong[0]))  # Play the first song in the list

                    elif "exit" in data2:  # Exit the program
                        tx_speech("Exiting\nThank you ")
                        break  # Exit the loop

                    else:  # Handle unrecognized commands
                        print("Samjh nhi aaya bapas bol")  # Prompt in Hindi: "Didn't understand, please repeat"
                else:
                    print("Kuch toh bol...") # Prompt in Hindi: "Say something..."
        else:
            print("Mujhe bola kya ???\nBtata toh sunna h")  # Prompt in Hindi: "Did you call me? You need to tell me if you want me to listen"
    else:
        print("Kuch toh bolta...")  # Prompt in Hindi: "Say something..."

# Uncomment the following lines to test specific functionality
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
# time.sleep(5)
