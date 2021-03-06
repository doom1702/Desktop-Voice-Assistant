import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyaudio
import smtplib
import pyjokes
from bs4 import BeautifulSoup
import json
import requests
import win32com.client as wincl
from urllib.request import urlopen


# dictionary containing email ids
mail_id = {"Recevier's Name":"Receiver's Email id"}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


# speak audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Greet According to time
def greet():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        speak("Good Morning")

    elif 12 <= hour < 17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    print("I am your assistant. How,may I help you ?")
    speak("I am your assistant. How,may I help you ?")


# Taking Commands from User
def takeCommand():
    # Return String Output Of class
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        # Print User Commands
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :{query}\n")
    except :
        # print(e)
        speak("Can't recognize Please say that again")
        print("Please,say that again")
        return "None"
        takeCommand()
    return query

def sendEmail(receiver,messsage):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Your Email id','Your Password')
    server.sendmail('Your Email id',receiver,message)
    server.close()


if __name__ == '__main__':
    greet()
    while True:
    # if 1 :
        query = takeCommand().lower()

        # Commands for query based response
        if "wikipedia" in query:
            
            speak("Searching for Wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query :
            speak("Opening Youtube...")
            webbrowser.open("www.youtube.com")

        elif 'open stack overflow' in query:
            speak("Opening Stackoverflow")
            webbrowser.open("www.stackoverflow.com")    
        
        elif 'play music' in query:
            speak("Playing Music..")
            music_dir ="Location"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randrange(0,int(len(songs))-1)]))
        
        elif 'geeks for geeks' in query:
            # webbrowser.open("www.google.com")
            r = sr.Recognizer()
            with sr.Microphone() as source :
                speak("Search Your Query")
                print("Search Your Query")
                audio = r.listen(source)
                r.pause_threshold = 1
                try:
                  query = r.recognize_google(audio, language='en-in')
  
                  print(query)
                  webbrowser.open("https://www.geeksforgeeks.org/"+ query)
                except Exception() as e :
                  print("Sorry Operation Failed")
        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")     

        elif 'google search' in query :
         try:
             from googlesearch import search
         except ImportError: 
           print("No module named 'google' found")
  
         # to search
         speak("What do you want to search")
         query = takeCommand()
         print("Output:")   
         for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            print(j)

        elif 'the time' in query :
            str_Time = datetime.datetime.now().strftime("%H:%M:%S")
            print("The Time is : "+ str_Time)
            speak(f'The Time is {str_Time}')
        
        elif 'open vs code'in query :
            vs_code_location = "Location"
            os.startfile(vs_code_location)
        
        elif 'open vlc'in query :
            vlc_location = "Location"
            os.startfile(vlc_location)

        elif 'movies folder' in query :
            mvf_location = "Location"
            os.startfile(mvf_location)     

        elif 'send email' in query :
           try:
            # Taking Subject context and receiver from user
            print("Whom To Send Email?") 
            speak("Whom To Send Email")
            receiver = takeCommand()
            receiver = mail_id[receiver]
            speak("Tell your message")
            print("Tell your message")
            message = takeCommand()
            sendEmail(receiver,message)


           except Exception as e:
            #    print(e)
               speak("Sorry your mail cannot be send")
               print("Sorry your mail cannot be send")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            print("I am fine, Thank you")
            speak("How are you, Sir")
            print("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        
        elif 'what is your name' in query :
            speak("My name is Saturday")
            print("My name is Saturday")
        elif 'joke' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        
        # Reading News
        elif 'news' in query:
             
            try:
                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?country=in&apiKey=Your Api Key ")
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news of india')
                print('''===============NEWS FROM INDIA ============'''+ '\n')
                
                for item in data['articles'] :
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1

            except Exception as e:
                 
                print("This is the news.")
        
    # to read a file 
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                str_Time = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(str_Time)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)        
        
    # to read a file
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'exit'or 'quit' or 'stop' in query :
            exit()
