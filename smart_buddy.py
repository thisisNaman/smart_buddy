import pyttsx3
import speech_recognition as sr
import datetime
from time import sleep
import wikipedia
import os
import webbrowser
import pyjokes
import random
import psutil
import subprocess
import os



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

hr=int(datetime.datetime.now().hour)
m = int(datetime.datetime.now().minute)
#random lists---------------------------------------------------------------------
think = ["Thinking...","Recognizing..."]
sorry = ["Apologies...I could not get that","Sorry..Will you please repeat that","Please try one more time..","Sorry..","Didn't get that"]
greetings = ["Hi there! ", "Hello?","What\'s up","Hey Sir","Pleased to meet you!","Namaste"]
farewell = ["See you soon","Great talking with you...See you soon","Bye Bye","Nice talking with you","Take Care!"]




#---------------------------------------------------------------------------------

def speak(audio):
    engine.say(audio)
    engine.runAndWait()   #without this the audio is not audible

def wishme():
    hr=int(datetime.datetime.now().hour)
    if hr>=0 and hr<12:
        speak("Good Morning Sir, How can I help you?")
    elif hr>=12 and hr<=15:
        speak("Good Afternoon Sir, How can I help you?")
    else:
        speak("Good Evening Sir, How can I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold=1          #time to pause after listening
        r.energy_threshold = 600     #so that the assistant don't pay attention to disturbing voices
        audio=r.listen(source)
    try:
        print(random.choice(think)
        query = r.recognize_google(audio, language='en-in')
        print(f"{query}\n")
    except Exception as e:
        sorry_temp = random.choice(sorry)
        print(sorry_temp)
        speak(sorry_temp)
        return "None"
    return query


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()   #converting query to lower case
        if 'wikipedia' in query:
            query = query.replace("wikipedia","")
            if query==" ":
                speak("I didn't get that! ")
            else:
                speak("hmmmmm.....OK..Let's see..")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
        elif 'on youtube' in query or 'open youtube' in query or 'youtube' in query:
            query = query.replace("on youtube","")
            speak("Opening youtube...")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("Opening google...")
            webbrowser.Chrome()
            webbrowser.open("google.in")
    
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Currently, its {strTime}")
        elif 'stop listening' in query or 'bye' in query:
            speak(random.choice(farewell))
            exit(0)
        elif 'joke' in query or 'jokes' in query or 'laugh' in query:
            speak(pyjokes.get_joke())
            speak("Ha Ha Ha Ha")
        elif 'hello' in query or 'hi' in query or 'hey' in query:
            speak(random.choice(greetings))
        elif 'good morning buddy' in query:
            if hr>=0 and hr<12:
                speak("Good Morning to you too...")
                print("Good Morning to you too...")
            else:
                speak(f"Really...? Its {hr} {m}.Anyways..Good Morning!")
                print(f"Really...? Its {hr} {m}.Anyways..Good Morning!")
        elif 'battery status' in query:
            battery = psutil.sensors_battery()
            percent= str(battery.percent)
            speak(f"Your device is at {percent} %")
            print(percent+"%")
            if int(percent)<15:
                speak("I suggest you put your device on charging!")  
        elif 'open calculator' in query or 'start calulator' in query or 'calculate' in query or 'calculator' in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
        elif 'open wordpad' in query or 'start wordpad' in query or 'wordpad' in query:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
        elif 'make notes' in query or 'open notes' in query or 'notes' in query or 'note' in query:
            speak("Which one would you like to open ? Notepad or OneNote")
            ask = takeCommand().lower()
            if 'onenote' in query:
                speak("Which one?")
                os.system('start OneNote:')
            elif 'notepad' in query:
                speak("Opening Notepad")
                subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            else:
                speak("Sorry.....Please try again")
                print("Sorry.....Please try again")
            

        
        
