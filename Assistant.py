import wolframalpha
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import time
import os
import winshell
import pyjokes
import win32com.client as wincl
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
listener = sr.Recognizer()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:  
            print('listening')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            talk(command)
    except Exception as e:
        print(e)
        print('Unable to recognize your voice')
        talk('Unable to recognize your voice')
        return 0
    return command
while(1):
    talk('Heeey!Please Instruct me')
    command = take_command()
    if command==0:
        continue
    if 'stop' in command or 'exit' in command in command:
        talk('Ok bye')
        break
    if 'who are you' in command:
        talk('I am your smart voice assistant. I can listen all your instructions and provide you with better solutions quickly. Ask me for jokes, news, any information, song and many more. I will provide you with both oral and written answers. So one a plus point for you. And upgrading myself.')
        print('Most of the tasks a voice assistant should do.')
    if 'time' in command:
        time = datetime.datetime.now().strftime(' %I %M %p')
        print(time)
        talk('The current time is' + time)
    elif 'how' in command:
        command = command.replace("how","")
        webbrowser.open_new_tab(command)
    elif 'search' in command:
        command = command.replace("search","")
        webbrowser.open_new_tab(command)
    elif 'google' in command:
        webbrowser.open_new_tab("https://www.google.com")
        talk('Google is open') 
    elif 'play' in command:
        song  = command.replace('play','')
        print('playing')
        talk('playing')
        pywhatkit.playonyt(song)
    elif 'who' in command:
        person = command.replace('who','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'about' in command:
        person = command.replace('about','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'what' in command:
        person = command.replace('what','')
        info = wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'wifi' in command:
        talk('Yes, I run on wifi to provide you answers and load context for your doubts.')
        print('Yes')
    elif 'chrome' in command:
        talk('Opening Chrome')
        print('Opening')
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome')
    elif 'wordpad' in command:
        talk('Opening Wordpad')
        print('Opening')
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\WordPad')
    elif 'paint' in command:
        talk('Opening Paint')
        print('Opening')
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\Paint')
else:
        talk('Application not available')
        
