import speech_recognition as sr
import random
from playsound import playsound as ps
import webbrowser
import os

import pywhatkit as kit


listner = sr.Recognizer()

list1 = ['0001.mp3', '0002.mp3', '0003.mp3', '0004.mp3', '0005.mp3']
run = True


try:
    with sr.Microphone() as source:
        print("Say something!")
        audio = listner.listen(source)
        command = listner.recognize_google(audio)
        command = command.lower()
        print(len(command))
        print("You said: " + command)
        if 'cover' in command or 'gober' in command:
            ps(random.choice(list1))
            
            
        elif 'khabar' in command:
            ps(random.choice(list1))
            
        elif 'band'  in command or 'bond' in command:
            ps('001.mp3')
            run = False
            
        elif 'stop' in command:
            ps('001.mp3')
            run = False
        elif 'geet' in command or "play" in command or 'song' in command:
            kit.playonyt(command)
            
        elif 'movie' in command or 'film' in command:
            webbrowser.open('https://myflixer.pw/home')
            ps('movie.mp3')
            
        elif 'incognito' in command:
            os.system('start chrome --incognito')
            
        elif 'moco' in command or 'mock' in command or 'ho' in command or 'man ho' in command or 'who i am' in command or 'who am i' in command:
            webbrowser.open('https://www.facebook.com/crazzysaurab.baral')
            
            
        elif 'search' in command or 'who' in command:
            kit.search(command.split('search'))
            
        elif '.com' in command or 'www' in command:
            webbrowser.open(command)

except:
    pass
  
        
        
            
        
    
        
            
    
            
        
    
            
            
        
    
        


   