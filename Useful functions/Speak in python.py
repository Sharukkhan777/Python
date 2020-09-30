
# text to speech in python console

# -------------------
## NOTE
#If the module is not found
#Download from the link below
#https://github.com/Ishanvaid9/pyttsx-files or use --- pip install pyttsx3 ---
#
#Save as the Above file as pyttsx
#So that it wont show the module not found error
#
#Save as in the location 
#Lib\site-packages\
# -------------------

import pyttsx   # import pyttsx3
engine = pyttsx.init()    # engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# print(voices[1].id)
engine.setProperty('rate', 150)
#engine.say("Hello, How are you ?")
engine.runAndWait()


def speak(str):
    engine.say(str)
    engine.runAndWait()

speak("Hello, What's going on")




















