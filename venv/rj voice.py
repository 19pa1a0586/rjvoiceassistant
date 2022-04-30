# Upgrade/ Update pip library by 'py -m pip install --upgrade pip'
# Check the current version of pip by using the following command 'pip --version'

# This module helps python/voice assistant to speak with us
# If you need to install then use 'pip install pyttsx3'
import pyttsx3

# This module helps python/voice assistant to understand/listed what we said
# If you need to install then use 'pip install SpeechRecognition'
import speech_recognition as sr

# This module helps us to open the content in the new web browser
import webbrowser

# This module helps us to get the exact date and time
# If you need to install then use 'pip install DateTime'
import datetime

# This module helps us to search and open YouTube
# If you need to install then use 'pip install pywhatkit'
import pywhatkit
from flask import Flask, request

# This module helps us to shut down/restart the system/computer
import os

# This module helps us to know the current stock prices for specific stocks
# If you need to install then use 'pip install yfinance'
import yfinance as yf

# This module contains pre-defined jokes such that we can use. Whenever we ask to tell me a joke then it will answer
# from this module.
# If you need to install then use 'pip install pyjokes'
import pyjokes

import wikipedia

# This function helps us to speak loud whatever we wish to pass as context
def speaking(message):
    # We have to instantiate the object of pyttsx3
    engine = pyttsx3.init()
    # engine.say("Hi dear, My name is robert.")
    # print(engine.getProperty('voices'))
    # This property helps us to know what are the voices that are present in out system
    voices = engine.getProperty('voices')
    # by default we have male voice. I want change the voice to female by using setProperty method
    engine.setProperty('voice', voices[1].id)
    # print(engine.getProperty('rate'))
    # This helps to set the speed of the voice assistant, by default 200
    engine.setProperty('rate',180)
    # say(context) method helps us to speak the message/context loud with our desired voice
    engine.say(message)
    # computer/system needs to wait untill the engine completes its speaking process, this can be done by the runAndWait() method
    engine.runAndWait()


def getTheNoon():
    hr = int(datetime.datetime.today().hour)
    if hr > 0 and hr < 12:
        return "Morning"
    if hr >= 12 and hr < 16:
        return "Afternoon"
    return "Evening"

# welcome message
def greetings():
    speaking(f"Hi good {getTheNoon()}, My name is Riya. I am your personal assistant. How do you do?")


# First instantiate Recognizer() class from speech_recognition library
r = sr.Recognizer()

# This function listen to our microphone and converts the audio into text using google and return it
def audioToText():
    # Now we use context manager(using with keyword in python) and instantiate Microphone() class from
    # speech_recognition library and use it as a source
    with sr.Microphone() as source:
        # Now lets try to grab the audio from the user and convert the audio to text.
        # But sometimes we may run into some troubles. So, it's better to handle with try except blocks
        try:
            # This helps us to grab our voice without any noise by removing all the uneccessary background noise
            r.energy_threshold = 10000
            # We need to listen to the user by waiting for sometime
            r.adjust_for_ambient_noise(source, 0.8)
            print("listening")
            # Now after pausing for some time, we need to listen to the user and grab the voice message and store it into
            # the variable
            audio = r.listen(source)
            # Now by using the recognizer_google() method from Recognizer() class we can convert the audio to text
            # along with our desired language
            text = r.recognize_google(audio, language="en")
            # print(text)
            # speaking(text)
            return text
        # we may get UnknownValueError then it will directly handle the error by using this except block
        except sr.UnknownValueError:
            # speaking("Sorry I didn't understand, I am waiting to listen")
            # return "I am waiting to listen"
            return "Sorry I didn't understand, I am waiting to listen"
        # we may get RequestError then it will directly handle the error by using this except block
        except sr.RequestError:
            # speaking("Sorry I didn't understand, I am waiting to listen")
            # return "I am waiting to listen"
            return "Sorry I didn't understand, I am waiting to listen"
        # If other than the above-mentioned errors occurred then this except block will execute
        except:
            # speaking("Sorry I didn't understand")
            # return "I am waiting to listen"
            return "Sorry I didn't understand, I am waiting to listen"


# audioToText()


# This function helps us to get the date along with the weekday
def getDateAndDay():
    weekdays = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thrusday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    try:
        speaking(f"Today is {datetime.date.today()}, {weekdays[datetime.date.today().weekday()]}")
    except:
        pass

# This function helps us to get the exact current time
def getTime():
    try:
        speaking(datetime.datetime.now().strftime("%I:%M:%S"))
    except:
        pass


def searchInYoutube():
    speaking("What do you want to search in youtube?")
    query = audioToText()
    speaking(f"opening {query} in youtube")
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def openWebbrowser():
    speaking("What do you want to search in Webbrowser?")
    query = audioToText()
    speaking(f"opening {query} in Webbrowser")
    webbrowser.open(f"https://www.google.com/search?q={query}")

# def searchInWikipedia():
#     speaking("What do you want to search in wikipedia?")
#     query = audioToText()
#     speaking(f"opening {query} in wikipedia")
#     webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")

def startRiya():
    greetings()
    start = True
    while(start):
        query = audioToText().lower()
        print(query)
        if 'what about you' in query:
            speaking("I'm fine, You're very kind to ask. Let me know if I can help you?")
        elif 'how do you do' in query:
            speaking("I'm fine, You're very kind to ask. Let me know if I can help you?")
        elif 'quit' in query:
            speaking("Ok, I'm shutting down.")
            break
        elif 'shut' and 'down' in query:
            speaking("Ok, I'm shutting down.")
            break
        elif 'bye' in query:
            speaking("Ok, I'm shutting down.")
            break
        elif 'what' and 'time' in query:
            getTime()
        elif 'what' and 'day' in query:
            getDateAndDay()
        elif 'what' and 'date' in query:
            getDateAndDay()
        elif "play" in query:
            pywhatkit.playonyt(query)
        elif 'open' and 'youtube' in query:
            searchInYoutube()
        elif 'start' and 'youtube' in query:
            searchInYoutube()
        elif 'open' and 'web' and 'browser' in query:
            # openWebbrowser()
            speaking("This is what I found")
            pywhatkit.search(query)
        elif 'open' and 'google' in query:
            openWebbrowser()
        elif 'search' and 'from' and 'wikipedia' in query:
            # searchInWikipedia()
            query = query.replace("wikipedia","")
            q = wikipedia.summary(query, sentences=2)
            speaking(q)
        elif 'your name' in query:
            speaking("My name is Riya. What's you good name?")
        elif 'my name' in query:
            speaking("your name is too cool. Let me know if I can help you?")
        elif 'my self' in query:
            speaking("your name is too cool. Let me know if I can help you?")
        elif "tell" and "joke" in query:
            speaking(pyjokes.get_joke())
        else:
            speaking("sorry i didn't understand, i am waiting to listen")
startRiya()