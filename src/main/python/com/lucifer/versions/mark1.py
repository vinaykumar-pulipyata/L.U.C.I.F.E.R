#Mark - 1

import pyttsx3
import speech_recognition as sr


def initialize() : 
    #Voice Test
    engine = pyttsx3.init()
    greetings = "Hello, I am LUCIFER - MARK 1" 
    print(greetings)
    engine.say(greetings)
    engine.runAndWait()

    mikeInput = "I repeat what you say."
    print(mikeInput)
    engine.say(mikeInput)
    engine.runAndWait()


    #Mike Test
    recognizer = sr.Recognizer()

    while True :
        kindMsg = "Kindly speak something"
        print(kindMsg)
        engine.say(kindMsg)
        engine.runAndWait()
            
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            engine.say("You said:" + text)
            engine.runAndWait()
            exitMsg = "Thank you exiting Program."
            print(exitMsg)
            engine.say(exitMsg)
            engine.runAndWait()
            break
        except Exception as e:
            sorryMsg = "Sorry, I could not understand. Please try again"
            print(sorryMsg + " Error:", e)
            engine.say(sorryMsg)
            engine.runAndWait()
