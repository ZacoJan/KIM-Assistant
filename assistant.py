import speech_recognition as sr
import pyttsx3
import pywhatkit
import openai
import datetime
import wikipedia

from config import OPENAIKEY, FREEMODE

openai.api_key = OPENAIKEY
FREEQUERYMODE = FREEMODE


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
    return command


def run_kim():
    command = take_command()
    print(command)
    if command != '':

        if 'change voice' in command:
            result = voiceChanger(command)
            talk(result)

        elif 'your name' in command:
            talk("My Name is Kim, K. I. M")

        else:
            print('Listening')


    if FREEQUERYMODE:

        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'who is' in command or ('what is' in command and "your name" not in command):
            try:
                person = command.replace('who is', '')
                person = command.replace('what is', '')
                info = wikipedia.summary(person, 3)
                print(info)
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                talk(e)

        elif 'date' in command:
            date = datetime.date.today()
            talk(str(date))

    else:
        response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=command,
        temperature=0.5,
        max_tokens=20,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )

        # Print the generated text
        talk(response["choices"][0]["text"])

while True:
    run_kim()