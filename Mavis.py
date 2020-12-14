import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from PyDictionary import PyDictionary
webbrowser.register('chrome', None)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.setProperty("rate", 170)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Abdul")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Abdul")
    else:
        speak("Good Evening Abdul")
    speak("Tell me how may I assist you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You: {query}\n")

    except Exception as e:
        print("Sorry, Say that again please...")
        return "None"
    return query


if __name__ == '__main__':

    # speak("Hello Abdul.")
    wishme()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak(results)

        elif 'search' in query:
            query = query.replace("search", "")
            try:

                myDict = PyDictionary(query)
                speak(myDict.getMeanings())
            except:
                speak("Sorry, I could not fetch the meaning ")

        elif 'open moodle' in query:

            webbrowser.open("https://moodle.nitdgp.ac.in/my/")

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open gmail' in query:
            webbrowser.open("https://www.gmail.com")

        elif 'open college gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ABDUL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open whatsapp' in query:
            Path = "C:\\Users\\ABDUL\\AppData\\Local\\WhatsApp\\WhatsApp.exe"

            os.startfile(Path)

        elif 'speed test' in query:
            webbrowser.open("https://fast.com/")

        elif 'date' in query:
            strdate = datetime.date.today()
            speak(f"Today is {strdate}")

        elif 'open among us' in query:
            among_us_path = "C:\\Users\\ABDUL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Among Us.lnk"
            os.startfile(among_us_path)

        elif 'open fifa' in query:
            fifa_path = "E:\\games\\Games\\FIFA 18\\FIFA18.exe"
            os.startfile(fifa_path)


        elif 'open vpn' in query:
            vpn_path = "C:\\Users\\ABDUL\\Downloads\\vpngate-client-2020.10.13-build-9745.148387\\vpncmgr_x64.exe"
            os.startfile(vpn_path)

        elif 'open discord' in query:
            discord_path = "C:\\Users\\ABDUL\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
            os.startfile(discord_path)

        elif 'open git' in query:
            webbrowser.open("https://github.com/Abdulrashif/")


        elif 'stop' in query:
            speak("OK. I will take my leave now. Have a nice day Abdul.")
            break


        # conversation programming


        elif 'who are you' in query:
            speak("I am Mavis. An artificial Intelligence created to serve you")

        elif 'who created you' in query:
            speak("I was created by Master Abdul Rashif on 24th of november 2020")

