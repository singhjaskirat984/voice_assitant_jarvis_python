import pyttsx3 as pyt 
import speech_recognition as sr
from selenium import webdriver
import os
import wolframalpha
import pyautogui as pyg
import psutil
import pyjokes
import datetime




engine = pyt.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
 

def get_audio(): 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please")

        return "None"

    return query 
  

def time():
    Time = datetime.datetime.now().strftime("%I:%S:%M")
    speak("The current time is")
    speak(Time) 

def date():
    yr = datetime.datetime.now().year
    mon = datetime.datetime.now().month
    dat = datetime.datetime.now().day
    speak("The current date is")
    speak(dat)
    speak(mon)
    speak(yr)

def screenshot():
    img = pyg.screenshot()
    img.save("C:\\Users\\Jaskirat Singh\\Desktop\\Jarvis_screenshots\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def wishme():
    speak("checking remote servers!")
    speak("importing prefernces and loading all the system drivers!!")
    speak("establishing secure connection!")
    os.startfile("C:\\Program Files\\Rainmeter\\Rainmeter.exe")
    speak("secure connection established!!")
    speak("We are online!!")
    speak("Welcome back Sir!")
    speak("Jarvis at your service Please tell me how can i help you?")

def process_text(input):
    if "search" in input:
        search_web(input)
            
    elif "time" in input:
        time()

    elif "date" in input:
        date()

    elif "calculate" in input.lower(): 
              
            # write your wolframalpha app_id here 
            app_id = "EREVQK-5RG7WW7JEX" 
            client = wolframalpha.Client(app_id) 
  
            indx = input.lower().split().index('calculate') 
            query = input.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            speak("The answer is " + answer) 

    elif "open" in input:     
        # another function to open  
        # different application availaible 
        open_application(input.lower())  
        return

    elif "logout" in input:
        os.system("shutdown -l") 

    elif "shutdown" in input:
        os.system("shutdown /s /t 1")

    elif "restart" in input:
        os.system("shutdown /r /t 1")

    elif "play songs" in input or "play music" in input or "songs" in input or "music" in input or "play song" in input or "song" in input:
        songs_dir = "G:\\Music"
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[0]))

    elif "take screenshot" in input or "take ss" in input:
        screenshot()
        speak("screenshot taken!")

    elif "cpu" in input:
        cpu()

    elif "jokes" in input or "joke" in input:
        jokes()


    elif "who are you" in input or "define yourself" in input: 
        text = '''Hello, I am Jarvis. Your personal Assistant. 
        I am here to make your life easier. You can command me to perform 
        various tasks such as calculating sums or opening applications, searching web, telling jokes, playing music, cpu or battery usage, 
        taking screenshots, logout shutdown or restart ypur PC, telling you date and time'''
        speak(text) 
         

    elif "who made you" in input or "created you" in input: 
        text = "I have been created by Jaskirat Singh."
        speak(text) 
           

def search_web(input):
    driver = webdriver.Chrome("C:\\anaconda3\\envs\\voice_assistant_jarvis_python\\voice_assistant_code_files\\jarvis\\chromedriver.exe")
    driver.implicitly_wait(1)
    driver.maximize_window()
    if 'youtube' in input.lower():
        speak("Opening in Youtube!")
        indx = input.lower().split().index('youtube') 
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower(): 
  
        speak("Opening Wikipedia") 
        indx = input.lower().split().index('wikipedia') 
        query = input.split()[indx + 1:] 
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
        return

    else: 
  
        if 'google' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        elif 'search' in input: 
  
            indx = input.lower().split().index('google') 
            query = input.split()[indx + 1:] 
            driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
  
        else: 
  
            driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 
            return


def open_application(input): 
  
    if "chrome" in input: 
        speak("Opening Google Chrome") 
        os.startfile('C:\\Users\\Jaskirat Singh\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe') 
        return
  
    elif "word" in input: 
        speak("Opening Microsoft Word") 
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk') 
        return
  
    elif "excel" in input: 
        speak("Opening Microsoft Excel") 
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk') 
        return

    elif "excel" in input: 
        speak("Opening Microsoft Excel") 
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk') 
        return

    elif "Android Studio" in input: 
        speak("Opening Android studio ") 
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio.lnk') 
        return

    elif "eclipse" in input: 
        speak("Opening eclipse ") 
        os.startfile('C:\\Users\\Jaskirat Singh\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Eclipse.lnk') 
        return

    elif "sublime text" in input: 
        speak("Opening sublime text ") 
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sublime Text 3.lnk') 
        return

    else: 
        speak("Application not available") 
        return


# Driver Code 
if __name__ == "__main__": 
    wishme()
    while True:
        query = get_audio().lower()

        if len(query) == 0:
            continue

        if "exit" in str(query) or "bye" in str(query) or "sleep" in str(query) or "offline" in str(query):
            speak("disconnecting all servers!")
            speak("Going Offline!")
            quit()
            

        # calling process text to process the query 
        process_text(query) 





