
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import pywhatkit
import cv2
from requests import get
import sys
import pyautogui
import time
import PyPDF2
import operator
from bs4 import BeautifulSoup
# from  pywikihow



engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    tt =time.strftime("%I,%M,%p")
    if hour>=0 and hour<12:
        speak(f"good mornig!{tt}")
    elif hour>=12 and hour<18:
        speak(f"good afternoon Raja !{tt}")
    else:
        speak(f"good evening raja !{tt}")

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

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=5fe42268bb374030b24d3d759525a682'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head =[]
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"todat's{day[i]} news is: {head[i]}")

def pdf_reader():
    book = open('Constitution of India.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"totel number of pages of this book is{pages}")
    speak("Raja , please tell me the page number from where i have to read")
    # pg = int(input("please enter the page number"))
    # pg = takeCommand().lower()
    
    page = pdfReader.getPage(0)
    text = page.extractText()
    speak(text)

if __name__ =="__main__":
    wishMe()
    
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'wikipedia ' in query:
            speak('searching wikipedia')
            quary = query.replace('wikipedia' , " ")
            results = wikipedia.summary(query , sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif 'news' in  query:
            speak("please wait raja, featching the latest news")
            news()
        
        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open command prompt' in query:
            os.system("start cmd")

        elif "temperature " in query:
            search = "temperature in ghaziayabad"
            url = f"https//www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current{search} is {temp}")

        elif 'open camera' in query:
            speak("opining camera")
            cam = cv2.VideoCapture(0)
            while True:
              ret , img = cam.read()
              cv2.imshow('webcam',img)
              k= cv2.waitKey(50)
              if k==27:
                  break
            cam.release()
            cv2.destroyAllWindows() 

        # elif 'open notepad' in query:
        #     npath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.exe"
        #     os.startfile(npath) 
        
        elif "calculations" in query :
            r =sr.Recognizer()
            with sr.Microphone()as source:
                speak("tell me what you wnat to calculate , example: 3 plus 3")
                print("listening.....")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+':operator.add,
                        '-':operator.sub,
                        '*':operator.mul,
                        'divided': operator.__truediv__,

                    }[op]

                def eval_binary_expr(op1 , oper , op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1,op2)
                speak("your result is")
                speak(eval_binary_expr(*(my_string.split())))    

        elif "ip address" in query:
            ip= get('https://api.ipify.org').text
            speak(f"your ip address is{ip}")

        elif 'open google' in query:
            speak("str , what should i search on google")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "temperature " in query:
            search = "temperature in ghaziayabad"
            url = f"https//www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current{search} is {temp}")

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
        
        elif 'nappu ' in query:
            speak ('yes raja you are right, pravesh is a lund boy bsdk hai')

        elif 'switch the window' in query:
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.keyUp('alt')

        elif 'location' in query or 'where am i' in query:
            speak('wait raja, let me check')
            try:
                ipadd = requests.get('https://api.ipify.org').text
                print(ipadd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                geo_requests= requests.get(url)
                geo_data = geo_requests.json()
                # city = geo_data['city']
                state = geo_data['state']
                country = geo_data['country']
                speak(f'Raja, your current location is{state} city of {country} country')
            except Exception as e:
                speak("sorry Raja, i did not get the location")
                pass

        elif 'screenshort' in query or 'ss' in query:
            speak('raja, please tell me the name for this screenshort file')
            name = takeCommand().lower()
            speak("Raja ,please hold the screen , i am taking the ss")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done Raja , screenshort is saved in our main folder")

        elif "read pdf" in query:
            pdf_reader()

        elif "activate how to do mode " in query:
            speak("activated Raja , please tell what you want to know.")
            how = takeCommand()
            max_result = 1
            how_to = search_wikihow(how , max_result)
            assert len(how_to)==1
            how_to[0].print()
            speak(how_to[0].summary)

        elif "you can sleep now" in query:
            speak("thanks for using me raja")
            sys.exit()

        speak("raja , do you have any other work for me")


