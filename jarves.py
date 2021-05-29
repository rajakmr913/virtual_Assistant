
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit


engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good mornig!")
    elif hour>=12 and hour<18:
        speak("good afternoon Raja !")
    else:
        speak("good evening raja !")

    speak("I am your AI  . How may i help you ")

def takeCommand():
    # it takes microphone input from user and return string
    r = sr.Recognizer()
    with sr.Microphone()as sourse:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(sourse)


    try:
         print( "Recognizing...")
         qurey = r.recognize_google(audio , language = 'en-in')
         print("user said:" , qurey)

    except Exception as e:
        print(e)
        print(" sorry i did not capture please say that again...")
        return "none"
    return qurey



if __name__ =="__main__":
    wishMe()
    
    # while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia ' in query:
            speak('searching wikipedia')
            quary = query.replace('wikipedia' , " ")
            results = wikipedia.summary(query , sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif ' the time ' in query:
            timestr = datetime.datetime.now().strftime("%H:%M:%S")
            print(timestr)
            speak(f"Raja , the time is {timestr}")
        
        elif ' play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\favoriote song'
            songs =os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[0]))

        elif ' open  code' in query:
            codepath = "C:\\Users\\rajak\AppData\\Loca\l\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'play' in query:
           music = query.replace('play', '')
          
           result = pywhatkit.playonyt(music)
           speak( 'playing' + result)
         

        elif 'joke' in query:
            speak (pyjokes.get_joke())

        elif 'single' in query:
            speak ('sorry i am connected with internet but i willbe here always for you')

        elif 'love' in query:
            speak ('love is a feelings and i love to talk with you')

        elif 'boring' in query:
            speak ('what can i do for you that you feel better')

        else:
            speak ("go to hell")


