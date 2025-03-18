import datetime
import os
import sys
import webbrowser
import pyautogui
import speech_recognition as sr                       # sr acts as a alias for speech recognition module
import pyttsx3
#from numpy.core.defchararray import lower
import wikipedia
import random






# *****          first step ==> oru voice choose pannanum           *****************


engine = pyttsx3.init('sapi5')         # => pyttsx3 la irunthu sapi5 ngra oru microsoft speech api aaa initiate panrathu
voices = engine.getProperty('voices')      #engine la irunthu voice propertyaa voices nu oru object la storepanren
# print(voices)                             #=> to find how many voices in our computer
engine.setProperty('voice',voices[1].id)              # set property engine la irunthu voice get pannikkithu

# print(voices[1].id)            ==> voice 1 => zira (girl) voice
# print(voices[0].id)               # ==> voice 0 => David (boy) voice


def speak(audio):
    """speak("namma kudukkura textaaa audiovaa maathi kudukkum")"""
    engine.say(audio)
    engine.runAndWait()


def wishme():
    """datetime module la datetime funciton la now function la hour => now hour sollum"""

    speak("Hi sir,")                   #function kulla oru function

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning ")
    elif(hour>=12 and hour<18 ):
        speak("good afternoon ")
    elif(hour >=18 and hour <24):
        speak("Good evening ")

    # time = datetime.datetime.now().strftime("%H:%M")
    # speak("the time is")
    # speak(time)
    speak("This is Friday, What can i do for you sir")
    speak("Waiting for your code word")

    # if hour>=0 and hour<12:
    #     speak("Good Morning !,this is Friday")
    #     #speak(" Naanthaan Friday. Sollungal boss naan enna seyyanumm!!!")
    #
    # elif hour>=12 and hour<18:
    #     speak("Good Afternoon ,this is Friday")
    #     #speak(" Naanthaan Friday. Sollungal boss naan enna seyyanumm!!!")
    #
    # elif hour>=18 and hour<21:
    #     speak("good evening ,this is friday")
    #     #speak(" Naanthaan Friday. Sollungal boss naan enna seyyanumm!!!")
    #
    # else:
    #     speak("Good night !,this is friday ")
    #     #speak(" Naanthaan Friday. sikkiram poi thoongunga . Sollungal boss naan enna seyyanumm!!!")



def takecommand():

    """take command func is used for jarvis taking an input as voice recognisation"""
    #global query
    recognizer = sr.Recognizer()           # sr la recognizer funcionaaa recognizer la store panren
    with sr.Microphone() as source:         #microphoneaaa sourceaaa aliasaaa maathirukkom
        print("Listening.......")           # => while taking input as voice.. print this litsening
        recognizer.pause_threshold=1        #recognizer la pause threshold nu oru function call panrom    ==> func of pause threshold is => oru oru word kku nadula kudukkura space seconds
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)    # instead of using source , we can  use sr.recognizer


    # if the above content are ok, then it works the code
    # in case if not, it will go to except



    try:
        print("wait for few moments.................")
        query = recognizer.recognize_google(audio,language='en-in')    #recognize panna audio va google la paathu english la type panni query la store panni vekkum
        print("USer said :",query)


    except Exception as e:
        #print(e)                        # enna error nu therila na print statementaaa comment la pottukkalam
        query = "Nothing"
        print(query)

    return query





if __name__ == "__main__":
    wishme()
    #takecommand()

    while True:
        query = takecommand().lower()
        if "wake" in query:
            """wake up function for friday"""
            speak("Yes sir, I am in, What we do!")

            while True:
                query = takecommand().lower()                       #takecommand is a function   .lower=> vara stringaa lowercase la maathi query la store pannum
                if "wikipedia" in query:
                    speak("searching in wikipedia..........")
                    query = query.replace("wikipedia", "")
                    result = wikipedia.summary(query, sentences=3)
                    speak("according to internet")
                    speak(result)


                elif "youtube" in query:
                    webbrowser.open("youtube.com")

                elif ("music" in query) or ("random music" in query):
                    musicdir = "D:\\Music"
                    songs = os.listdir(musicdir)
                    length = len(songs)
                    print(songs)
                    randsong = random.randint(0,length-1)
                    os.startfile(os.path.join(musicdir,songs[randsong]))

                elif "chrome" in query:
                    path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    os.startfile(path)

                elif "whatsapp" in query:
                    path = "https://web.whatsapp.com/"
                    webbrowser.open(path)
                    while True:
                        command = takecommand().lower()
                        if 'santosh' in command:
                            pyautogui.moveTo(463,219)
                            pyautogui.click()
                            pyautogui.PAUSE = 2
                            pyautogui.typewrite('santhosh')
                            pyautogui.press('enter')
                            pyautogui.PAUSE = 2
                            pyautogui.typewrite("hai Santhosh")
                            pyautogui.press('enter')

                        elif 'anbu' in command:
                            pyautogui.moveTo(463, 219)
                            pyautogui.click()
                            pyautogui.PAUSE = 2
                            pyautogui.typewrite(query)
                            pyautogui.press('enter')
                            pyautogui.PAUSE = 2
                            pyautogui.typewrite("hai Anbu")
                            pyautogui.press('enter')

                        elif 'parasu' in command:
                            pyautogui.moveTo(463, 219)
                            pyautogui.click()
                            pyautogui.PAUSE = 2
                            pyautogui.typewrite('parasu')
                            pyautogui.press('enter')
                            pyautogui.PAUSE = 2
                            pyautogui.typewrite("hai Parasu")
                            pyautogui.press('enter')
                        elif 'close' in command:
                            pyautogui.moveTo(1885,22)
                            pyautogui.PAUSE = 2
                            pyautogui.click()
                            break

                elif "movies" in query:
                    videopath = "D:\\movies"
                    movies = os.listdir(videopath)
                    length = len(movies)
                    any = random.randint(0,length-1)
                    os.startfile(os.path.join(videopath,movies[any]))

                elif "time" in query:
                    time = datetime.datetime.now().strftime("%H:%M")
                    speak("the time is ")
                    speak(time)

                elif "pycharm" in query:
                    path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
                    os.startfile(path)

                elif "portfolio" in query:
                    path = "https://ramesh645.000webhostapp.com/"
                    webbrowser.open(path)

                elif "my photo" in query:
                    speak('Opening Profile')
                    os.startfile("C:\\Users\\vasan\\OneDrive\\Desktop\\photo.jpg")

                elif ("tata" in query) or ("good bye" in query) or ("bye" in query):
                    speak("ok boss, bye, see you soon")
                    sys.exit()                                # this function wil exit the program

                elif "rest" in query:
                    speak("ok sir, wait for your call")
                    break

                elif ("shutdown" in query) :
                    os.system("shutdown /s /t 1")

                elif "restart" in query:
                    os.system("shutdown /r /t 1")

                elif ("sleep" in query) or ("logout" in query):
                    speak("ok boss, bye. See you soon")
                    os.system("shutdown -l")

                else:
                    speak("Sorry sir, can't understand")
#======================================================================================================================




