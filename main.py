# Library to import

import datetime  # This module import the date and time module
import webbrowser  # This module import the web-browser module
import urllib
import json
import pyautogui
# import pywhatkit
# from Jarvis.config import config
import wolframalpha
import playsound
import os
import time
from tkinter import *
import pyttsx3  # module imported for speech and voice recognition
import requests
from gtts import gTTS
import speech_recognition as sr  # Module imported from pyAudio through pip
import wikipedia  # This module import the wikipedia module
# from django.contrib.sites import requests
# Setting the properties for the AI bot/ One may change the settings accordingly
engine = pyttsx3.init('sapi5')  # Speech API for taking voice input in Windows(in-built fxn)
voices = engine.getProperty('voices')  # getting details of current voice
# voices[0] for male voice(David) and voices[1], voices[2] for female voice(Hazel & Zira)
engine.setProperty('voice', voices[2].id)  # Setting the voice property for the engine(input processor)
engine.setProperty('rate', 210)  # Words per minute Ideal range ~ 200 words/min
engine.setProperty('volume', 0.8)  # Volume of the bot Ideal range ~ 0.75
a = 0
email = "<your_email>"
email_password = "<your_email_password>"
wolframalpha_id = "<your_wolframalpha_id>"
app_id = wolframalpha_id
def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
def speak(audio):  # This fxn is responsible for speaking! of our AI bot
    # engine.say(audio)
    # engine.runAndWait()
    tts = gTTS(text=audio, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
def wishMe():  # This fxn gives a greeting acc. to the auto time settings
    hour = int(datetime.datetime.now().hour)
    welcome = 0
    if 0 <= hour < 12:
        welcome = "Good Morning! Namaste"
    elif 12 < hour < 18:
        welcome = "Good Afternoon! Namaste"
    else:
        welcome = "Good Evening! Namaste"
    # greetings = "My Name is Harmony, I am an A.I. assistant, my speed is 1042344.234 bits per second!\n"
    print(welcome)
    speak(welcome)
    # print(greetings)
    # speak(greetings)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.50
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # For list of supported languages visit <http://stackoverflow.com/a/14302134>
        print("User said:", query)
    except Exception as e:
        # print(e)
        print("Say that again, Please!")
        return "None"
    return query
def users():
    i = 0
    user_list = []
    user_input = ""
    while user_input != "quit":
        a1 = "Are you a new user?"
        print(a1)
        speak(a1)
        o1 = takeCommand()
        if "yes" in o1:
            a2 = "Okay new user, How may I call you?"
            print(a2)
            speak(a2)
            o2 = takeCommand()
            user_list.append(o2)
            o3 = "Do you want to add more users?"
            print(o3)
            speak(o3)
            o4 = takeCommand().lower()
            if "no" in o4:
                return user_list
        else:
            return user_list
        i += 1
    return user_list
def harmony(name, query):
    if "wikipedia" in query:
        speak('Searching on Wikipedia')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif "open youtube" in query:
        speak("Ok! I'll be opening youtube for you")
        webbrowser.open("youtube.com")
    elif "calculate" in query:
        question = query
        answer = computational_intelligence(question)
        speak(answer)
    elif "open google" in query:
        speak("Ok! I'll be opening Google for you")
        webbrowser.open("google.com")
    elif "open facebook" in query:
        speak("Ok! I'll be opening Facebook for you")
        webbrowser.open("facebook.com")
    elif "play song" in query:
        speak("Ok! I'll be playing songs from your favourite playlist")
        webbrowser.open("https://www.youtube.com/watch?v=73ubdCX1fMM&list=PLnK3RksNU3qXv9ZeXaB9TswYXllPIirtz")
    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("Sir!, the time is " + strTime)
    elif "search" in query:
        query = query.replace("search", "")
        results = webbrowser.open(query)
    # elif "what" in query:
    #     query = query.replace("what", "")
    #     results = webbrowser.open(query)
    #     webbrowser.open("google.com")
    # elif "calculate" in query:
    #     query = query.replace("calculate", "")
    #     speak("Ok! I'll calculate Google for you")
    #     webbrowser.open("query")
    elif "whatsapp" in query:
        query = query.replace("whatsapp", "")
        ie3 = "Okay! " + name + " , I'll open whatsapp for you"
        print(ie3)
        speak(ie3)
        results = webbrowser.open("web.whatsapp.com")
    elif "open zoom" in query:
        results = webbrowser.open("https://utoronto.zoom.us/j/82987936354")
    elif "quit" in query:
        exit_output = 'Thank you for using Bernard! An AI bot built by Divyansh Kachchhava'
        print(exit_output)
        speak(exit_output)
    elif "What's my name?" in query:
        output = "Sir, You asked me to call you" + name
        print(output)
        speak(output)
    elif "change my name" in query:
        output = "Sir, by what name should I call you"
        print(output)
        speak(output)
        i3 = takeCommand().lower()
        name = i3
        q9 = "Okay! So from now on, I'll call you " + name
        print(q9 + " :)")
        speak(q9)
    elif "where is" in query:
        query = query.split(" ")
        location_url = "https://www.google.com/maps/place/" + str(query[2])
        ure3 = "Hold on " + name + ", I will show you where " + query[2] + " is."
        print(ure3)
        speak(ure3)
        webbrowser.open(location_url)
    # elif "what is the weather in" in query:
    # api_key = "Your_API_key"
    # weather_url = "http://api.openweathermap.org/data/2.5/weather?"
    # query = query.split(" ")
    # location = str(query[5])
    # url = weather_url + "appid=" + api_key + "&q=" + location
    # js = requests.get(url).json()
    # print(js)
    # if js["cod"] != "404":
    #     weather = js["main"]
    #     temp = weather["temp"]
    #     hum = weather["humidity"]
    #     desc = js["weather"][0]["description"]
    #     resp_string = " The temperature in Kelvin is " + str(temp) + " The humidity is " + str(hum) + " and The weather description is "+ str(desc)
    #     print(resp_string)
    #     speak(resp_string)
    # else:
    #     ui3 = "City Not Found"
    #     print(ui3)
    #     speak(ui3)
    elif "tell me about yourself" in query:
        for i in harmony_info:
            print(i)
            speak(i)
        w3 = "Do you want to know more about me?"
        print(w3)
        speak(w3)
        u89 = takeCommand().lower()
        if "yes" in u89:
            print(harmony_more_info)
            speak(harmony_more_info)
        "Sorry if you're bored...It was my life story... :)"
# def fxn_to_start(a):
#     a = 1
if __name__ == "__main__":
    playsound.playsound('C:\\Users\\Divyansh\\Downloads\\mixkit-sci-fi-loading-operative-system-2529.wav')
    # new_window = Tk()
    # a = 0
    # Button(new_window, text="Start",command=fxn_to_start(1)).pack()
    #
    # new_window.mainloop()
    # if a == 1:
    a = 0
    ig1 = "Sir, do you want to run without a user?"
    print(ig1)
    speak(ig1)
    r5 = takeCommand()
    if r5 == "no":
        a = 1
    wishMe()
    name = "Sir"
    user_list = [name]
    if a == 1:
        user_list = users()
        for j9 in user_list:
            if j9 != "":
                name = j9
    harmony_info = ["My name is Harmony", "I am older than the universe", "I am a Female", "My inspiration is Shah Rukh Khan",
                    "My favourite song Rasputin by Booney. M"]
    harmony_more_info = "First of Thank you ver much " + name + " because no-one ever cared about me" + " but you did :)" \
    "\nI was made by Divyansh who is famous as Zuckerbergh among his friends, I was the first Project which Divynsh ever made " \
    "\nSince then he left me :( ...\nBut now I would like to Thank God for sending you to me :)\nWe will spend a good time!" + name
    # k = ["\nStarting Program......\n", "Full Power......\n", "We are good to go......\n", "Launching in......",
    #      "\n3......",
    #      "\n2......", "\n1......", "\nProgram Started successfully! Enjoy:)"]
    i = 0
    # for i in k:
    #     print(i)
    #     speak(i)
    checker = 0
    w = "\nPlease, Ask your query " + user_list[0]
    print(w)
    speak(w)
    while True:
        st = time.time()
        query = takeCommand().lower()
        et = time.time()
        elapsed_time = et - st
        if checker == 0 or elapsed_time < 5:
            if "hey harmony" in query:
                query.replace("hey harmony", "")
                speak("Hey!" + name)
            harmony(name, query)
            checker = checker + 1

