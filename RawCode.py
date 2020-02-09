import pyttsx3
import webbrowser
import wikipedia
import speech_recognition as sr
import datetime
import os
#import espeak
espeak='en-us'
engine=pyttsx3.init('espeak')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

   
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("goog morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("hi boss what i have to do")

def takeCommand():
    mic=sr.Microphone()
    r=sr.Recognizer()
   
    with mic as source:
        print("listening...")
        #r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"user said: {query}\n")

    except Exception:
#        print("Say that again please...")
        return "None"
    return query
if __name__=="__main__":
    wishme()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
       
        elif 'open google' in query:
            webbrowser.open("google.com")
       
        elif 'play music' in query:
            music_dir='C:\\Users\\Public\\Music\\Bluetooth folder'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'play punjabi videos' in query:
            punjabi_dir='E:\\punjabi videos'
            video=os.listdir(punjabi_dir)
            print(video)
            os.startfile(os.path.join(punjabi_dir,video[0]))

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(strtime)
        elif 'thank you' in query:
            speak("welcome boss what else i have to do")
#        elif 'bye' or 'you can go' or 'you may leave' in query:
#           speak("have a nice day! bye")
#        elif ' ' in query:
#            speak("Please say something")
