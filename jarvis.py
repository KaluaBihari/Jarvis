import pyttsx3 # pip install pyttsx3 # text to speech
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import sys #using sys.exit() to exit the program
import random
import speech_recognition as sr # pip install speechRecognition # speech to text

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''
    This functions takes a argument and speak that
    '''
    engine.say(audio) 
    engine.runAndWait()#audible

# speak("Hello")

def WishMe():
    x = datetime.datetime.now()
    hours = int(x.strftime("%H"))
    if hours>=0 and hours<12:
        print("Jarvis : Good Morning")
        speak("Good Morning")
    elif hours>12 and hours<6:
        print("Jarvis : Good Afternoon")
        speak("Good Afternoon")
    else:
        print("Jarvis : Good Evening")
        speak("Good Evening")
    print("Jarvis : Hello sir I am Jarvis. Please tell me how may I help you?")
    speak("Hello sir I am Jarvis. Please tell me how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
     print("Recognizing....")
     query = r.recognize_google(audio, language='en-in')
     print(f"User : {query}\n")
    except Exception as e:
      print(e)
      return "None"
    return query

def generate_pass():
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','p','q','o','r','s','t','u','v','x','y','z','@','&','*','#']
    password = ''
    for i in range(random.randint(8,15)):
        a = random.choice(alpha)
        password = password+a
    return password
# a = generate_pass()
# print(a)
def tell_time():
    return datetime.datetime.now()

def search_youtube(search):
    search = search.replace("search youtube","")
    webbrowser.open("https://www.youtube.com/results?search_query="+search)

def search_google(search):
    search = search.replace("search google","")
    webbrowser.open("https://www.google.com/search?q="+search)


def wiki(search):
    try:
        results = wikipedia.summary(search,sentences = 2) 
    except:
        results = "Wikipedia Not Found!"
    return results

def Download(link):
    from pytube import YouTube
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download("D:\Python Practice\X - PYTHON PROJECTS\Jarvis-AI\Videos")
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def quit():
    print("Jarvis : Ok sir thanks for your time and have a nice day")
    speak("Ok sir thanks for your time and have a nice day")
    sys.exit()

if __name__ == "__main__":
    WishMe()
    while True:
        user = takeCommand()
        user = user.lower()
        if "hello" in user:
            print("Jarvis : Hello sir I am jarvis please tell me how may I help you?")
            speak("Hello sir I am jarvis please tell me how may I help you?")
            
        elif "wikipedia" in user:
            print(f"User : {user}")
            results = wiki(user)
            print("According to the wikipedia...")
            speak("According to the wikipedia...")
            print(f"Jarvis : {results}")
            speak(results)
        elif 'open chrome' in user:
            print(f"User : {user}")
            os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\chrome.exe")
            print(f"Jarvis : Done sir!")
            speak("Done Sir!")

        elif 'open code' in user:
            print(f"User : {user}")
            os.startfile(r"C:\Users\Anjali Kumari\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            print(f"Jarvis : Done sir!")
            speak("Done Sir!")

        elif 'open edge' in user:
            print(f"User : {user}")
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            print(f"Jarvis : Done sir!")
            speak("Done Sir!")

        elif 'open pycharm' in user:
            print(f"User : {user}")
            os.startfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2023.2.1\bin\pycharm64.exe")
            print(f"Jarvis : Done sir!")
            speak("Done Sir!")

        elif 'open discord' in user:
            print(f"User : {user}")
            os.startfile(r"C:\Users\Anjali Kumari\AppData\Local\Discord\app-1.0.9018\Discord.exe")
            print(f"Jarvis : Done sir!")
            speak("Done Sir!")

        elif 'open stackoverflow' in user:
            print(f"User : {user}")
            webbrowser.open("stackoverflow.com")

        elif 'open google' in user:
            print(f"User : {user}")
            webbrowser.open("google.com")

        elif 'open youtube' in user:
            print(f"User : {user}")
            webbrowser.open("youtube.com")

        elif 'open insta' in user:
            print(f"User : {user}")
            webbrowser.open("instagram.com")

        elif 'open facebook' in user:
            print(f"User : {user}")
            webbrowser.open("facebook.com")

        elif 'play a music' in user:
            print(f"User : {user}")
            os.open("song.mp3")

        elif 'download youtube video' in user:
            print(f"User : {user}")
            print(f"Jarvis : Enter the link sir!")
            link = input()
            Download(link)

        elif 'search youtube' in user:
            print(f"User : {user}")
            user = user.replace("search youtube","")
            search_youtube(user)

        elif 'search google' in user:
            print(f"User : {user}")
            user = user.replace("search google","")
            search_google(user)

        elif 'tell me the time' in user:
            print(f"User : {user}")
            print(f"Jarvis : The current time is {tell_time()}")
            speak(f"The current time is {tell_time()}")

        elif 'shutdown' in user:
            print(f"User : {user}")
            speak("ok sir i'll shutdown the computer")
            os.system("shutdown /s /t 1")

        elif 'restart' in user:
            print(f"User : {user}")
            speak("ok sir i'll restart the computer")
            os.system("shutdown /r /t 1")

        elif 'open file' in user:
            print(f"User : {user}")
            print("Jarvis : Enter the path of the file")
            speak("Enter the path of the file")
            path = input()
            try:
                os.open(path)
            except:
                print("Jarvis : Sorry sir can't open the file. Maybe the path dosen't exist")
                speak("Sorry sir can't open the file. Maybe the path dosen't exist")

        elif 'generate password' in user:
            print(f"User : {user}")
            password = generate_pass()
            print("Jarvis : Your randomly generated password is",password)
            speak(f"Your randomly generated password is {password}")

        elif 'who are you' in user:
            print(f"User : {user}")
            print("Jarvis : I am Jarvis sir and I am here to assist you")
            speak("I am Jarvis sir and I am here to assist you")

        elif 'open website' in user:
            print(f"User : {user}")
            print("Jarvis : Ok sir enter the link")
            speak("Ok sir enter the link")
            link = input()
            try:
                webbrowser.open(link)
            except:
                print("Jarvis : Sir the link dosen't exist")
                speak("Sir the link dosen't exist")
        
        elif 'quit' in user:
            quit()

        else:
            print(f"User : {user}")
            print("Jarvis : Didn't Understand Your Command")
            speak("Didn't Understand Your Command")