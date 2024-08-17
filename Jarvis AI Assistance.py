import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from requests import get
import pywhatkit as kit
import sys
import cv2
import random
import pyautogui
import psutil
import speedtest
from pywikihow import search_wikihow
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
  
def wishMe():
    hour = int(datetime.datetime.now().hour)
    Time = datetime.datetime.now().strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"Good Morning Sir! It's {Time}")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon Sir! It's {Time}")

    else:
        speak(f"Good Evening Sir! It's {Time}")

    speak("I am Jarvis Sir! Please tell me how can I help you ?")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognition...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        return "None"
    query = query.lower()
    return query

def TaskExecution():
    wishMe()
    while True:
    #if 1:
        query = takeCommand()


        #Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            

        elif 'open google' in query:
            speak("Sir, what should I search on google")
            mvk = takeCommand()
            webbrowser.open(f"{mvk}")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open chrome' in query:
            speak("Sir, what can i search on chrome")
            pmk = takeCommand()
            webbrowser.open(f"{pmk}")

        elif 'open email' in query:
            webbrowser.open("email.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'the time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {Time}")

        elif 'open code' in query:
            VsCode = ("C:\\Users\\91770\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
            os.startfile(VsCode)

        elif 'open command prompt' in query:
            os.system('start cmd')


        elif "temperature" in query:
            search = "temperature in Kangoan"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current {search} is {temp}")       


        elif 'play music' in query or 'play songs' in query:
            music_dir = 'F:\\songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            print(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")

        elif "send message" in query:
            kit.sendwhatmsg("+919325611709", "This msg is send by Jarvis... Hello Sir" ,18,30)

        elif "play song on YouTube" in query:
            speak("Sir, Which song I should play on youtube")
            you = takeCommand()
            kit.playonyt(f"{you}")
            

        elif 'volume up' in query: 
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute' in query:
            pyautogui.press("volumemute")

        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our system have {percentage} percent battery")

        elif "how much speed we have" in query or "internet speed" in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(f"Sir we have {dl} bit per second downloding speed and {up} bit per second uploding speed")

        elif "hide all files" in query or "hide this folder" in query or "visible for everyone" in query:
            speak("Sir, please tell me you want to hide this folder or make it visible for you.")
            condition = takeCommand().lower()

            if "hide" in query:
                os.system("attrib +h +s +r")
                speak("Sir, all the files in this folder are now hidden")

            elif "visible" in query:
                os.system("attrib -h -s -r")
                speak("Sir, all the files in this folder are now visible to everyone, I wish you are talking")

            elif "leave it" in condition or "leave for now" in condition:
                speak("Ok Sir.")
 
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "activate how to do mode" in query or 'open how to do mode' in query:
            speak("How to do mode is activated")
            while True:
                speak("please tell me what you want to know?")
                how = takeCommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("okay sir, how to do mode is close")
                        break
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir, i am not able to find this")
                    
        
                    
        elif "no thanks" in query:
            speak("Thanks for using me Sir, Have a good day")
            sys.exit()

        speak("Sir, Do you need any other help ?")      


if __name__ == "__main__":  
    TaskExecution()
    
    


