import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser

# Init speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Normal voice
voices = engine.getProperty('voices')


#Commands
timeCmd = "time"
openGoogleCmd = "open google"
yourNameCmd = "your name"
changeVoiceCmd = "change voice"
displayCommandsCmd = "display commands"
stopCmd = "stop"
exitCmd = "exit"
goodByeCmd = "goodbye"

def speak(text):
    print("MARK II:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("There was a problem with the speech service.")
        return ""

def indexOfVoice() :
    
    # Get the current voice
    current_voice = engine.getProperty('voice')
    current_voice_index = None
    for idx, voice in enumerate(voices):
        if voice.id == current_voice:
            current_voice_index = idx
            break
            
    return current_voice_index

def yourName() :
    current_voice_index = indexOfVoice()
    
    if current_voice_index == 0 :
        speak("I am LUCIFER - Mark II, your assistant.")
    else :
        speak("I am AISHA - Mark II, your assistant.")

def respond(command):
    if timeCmd in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif openGoogleCmd in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")
    elif yourNameCmd in command:
        yourName()
    elif changeVoiceCmd in command:
        changeVoice()
    elif displayCommandsCmd in command:
        speak("Right Away Sir, here are the commands")
        displayCommands()
    elif "stop" in command or "exit" in command or "goodbye" in command:
        speak("Goodbye Sir!")
        exit()
    else:
        speak("I don't understand that yet.")


def changeVoice() :
    speak("Changing Voice")
    
    # Find the index of the current voice
    current_voice_index = indexOfVoice()
            
    if current_voice_index == 0 :
        current_voice_index = 1
    else :
        current_voice_index = 0

    engine.setProperty('voice', voices[current_voice_index].id)
    speak("This is My New Voice Sir, I hope you like it.")
        
        
        
def displayCommands():
    print("1." + timeCmd)
    print("2." + openGoogleCmd)
    print("3." + yourNameCmd)
    print("4." + changeVoiceCmd)
    print("5." + displayCommandsCmd)
    print("6." + stopCmd + " or " + exitCmd + " or " + goodByeCmd)
    
def initialize() :    
    # Main loop
    speak("Hello Sir, I am LUCIFER - Mark 2.")
    speak("I can help you with the following commands")
    displayCommands()
    while True:
        command = listen()
        if command:
            respond(command)
