## AI ASSISTANT IN BEGINNER LEVEL

#Install libraries
!pip install speechrecognition pyttsx3 pyaudio

# Check if SpeechRecognition is installed
try:
    import speech_recognition as sr
    print("SpeechRecognition is installed.")
except ImportError:
    print("SpeechRecognition is not installed.")

# Check if pyttsx3 is installed
try:
    import pyttsx3
    print("pyttsx3 is installed.")
except ImportError:
    print("pyttsx3 is not installed.")

# Check if PyAudio is installed
try:
    import pyaudio
    print("PyAudio is installed.")
except ImportError:
    print("PyAudio is not installed.")

#Check
import speech_recognition as sr
import pyttsx3
import pyaudio
print("Libraries are installed successfully!")

#Program
import speech_recognition as sr
import pyttsx3
# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
# Function to listen to user's command
def listen():
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
        command = ""
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except Exception as e:
            print("Sorry, I didn't catch that.")
        return command

# Function to respond
def respond(response):
    engine.say(response)
    engine.runAndWait()
# Test the functionality
if __name__ == "__main__":
    print("Say 'hello' or 'exit' to test.")
    command = listen()
    if "hello" in command.lower():
        respond("Hello! How can I assist you?")
    elif "exit" in command.lower():
        respond("Goodbye!")


## AI ASSISTANT IN ADVANCED LEVEL

import sys
print(sys.version)

#Install 3 libraries
!pip install speechrecognition pyttsx3 pyaudio

#Check
import speech_recognition as sr
import pyttsx3
import pyaudio
print("Libraries are installed successfully!")

#Import speech recognition 
import speech_recognition as sr
# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()
# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source)
# Recognize the speech using Google's speech recognition
try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, I did not understand the speech.")
except sr.RequestError:
    print("Could not request results from Google Speech Recognition service.")

#Check for voice assistant
import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
# Test the function
speak("Hello, I am your voice assistant.")

#Program 
import speech_recognition as sr
import pyttsx3
import webbrowser

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand the speech.")
        return None
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def open_browser_and_search(query):
    search_url = f"https://www.google.com/search?q={query}"
    webbrowser.open(search_url)
    speak(f"Here are the results for {query}.")

# Main loop
while True:
    command = listen()
    if command:
        if "stop" in command or "exit" in command:
            speak("Goodbye!")
            print("Exiting...")
            break
        elif "open browser" in command or "search" in command:
            speak("What would you like to search for?")
            search_query = listen()
            if search_query:
                open_browser_and_search(search_query)
        else:
            speak(f"You said: {command}")
    else:
        speak("Please repeat your command.")

























