import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

speak("Hello sir. I am Jarvis. How can I help you?")

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except:
        speak("Sorry, I didn't understand that.")
        return ""

speak("I am listening.")

while True:
    command = listen()

    if "hello" in command:
        speak("Hello. How are you?")

    elif "time" in command:
        import datetime
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "stop" in command or "exit" in command:
        speak("Goodbye.")
        break


    import webbrowser
import subprocess

if "open youtube" in command:
    webbrowser.open("https://youtube.com")
    speak("Opening YouTube.")

elif "open calculator" in command:
    subprocess.Popen("calc.exe")
    speak("Opening calculator.")

if "..." in command:
    "jarvis"
    