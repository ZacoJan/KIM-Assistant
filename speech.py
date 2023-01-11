import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia


from AISource import *
from speech import *
from analysis import *

COMMONPHRASES = ['play','time','who is','what is','date','change voice','your name']

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[28].id)


def voiceChanger(person):
    if "one" in person or '1' in person:
        engine.setProperty('voice', voices[8].id)
        return "Voice changed to Voice 1"

    elif "two" in person or '2' in person:
        engine.setProperty('voice', voices[28].id)
        return "Voice changed to Voice 2"

    elif "three" in person or '3' in person:
        engine.setProperty('voice', voices[30].id)
        return "Voice changed to Voice 3"

    elif "four" in person or '4' in person:
        engine.setProperty('voice', voices[40].id)
        return "Voice changed to Voice 4"

    return "Voice id not indexed"


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'kim' in command:
                command = command.replace('kim', '')
    except:
        pass
    return command.lower()


def commonPhrases(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        return 'Current time is ' + time

    elif 'date' in command:
        date = datetime.date.today()
        return str(date)

    if 'change voice' in command:
        result = voiceChanger(command)
        return result

    elif 'your name' in command:
        return "My Name is Kim, K. I. M"


def wikiQuery(command):
    if 'who is' in command or ('what is' in command and "your name" not in command):
        request = command.replace('who is', '')
        request = command.replace('what is', '')
    else: 
        request = command
    
    try:
        info = wikipedia.summary(request, 3)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e)
        info = "NO-SOURCE-DATA-FOUND"
    except wikipedia.exceptions.PageError as e:
        print(e)
        info = "NO-SOURCE-DATA-FOUND"
    
    return info