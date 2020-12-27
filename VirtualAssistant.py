import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")
    elif hour>=12 and hour<18 :
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am qwerty my friend. Please tell mi how may i help you")

def takecommand():
    #converts input from microphone into string.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshould = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("I dind't understand,can you please ask again, i'll try to answer better this time.")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    while True :
        query = takecommand().lower()

        if "wikipedia" in query :
            speak("Searching Result..")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Acortding to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query :
            webbrowser.open("youtube.com")

        elif"open google" in query :
            webbrowser.open("google.com")

        elif "open stackoverflow" in query :
            webbrowser.open("stackoverflow.com")

        elif "play music online" in query :
            webbrowser.open("gaana.com")

        elif "play music" in query :
            music_dir = "C:\\Users\\shree\\Music"
            songs = os.listdir(music_dir)
            print("songs:")
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query :
            starTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is{starTime}")

        elif "open code" in query :
            codepath = "C:\\Users\\shree\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "open gmail" in query :
            webbrowser.open("gmail.com")

        elif "quit" in query:
            exit()

