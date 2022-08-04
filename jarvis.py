import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

 
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
       engine.say(audio)
       engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning ")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good evening")   

    speak("I am your assistant sir .How can i help you") 

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please...") 
        return "None"
    return query   

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sd51167228@gmail.com', 'Shubham@511')
    server.sendmail('sd51167228@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
      wishme()
      while True:
      #if 1:

        query = takeCommand().lower()

        if 'wikipedia' in query: 
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open christ university' in query:
            webbrowser.open("christuniversity.in")

        elif 'play music' in query:
            music_dir = 'D:\\samsung M20\\Xender\\audio'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[8]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'voltage if' in query:
            tmp = [int(s) for s in query.split() if s.isdigit()]
            voltage = tmp[0] * tmp[1]
            speak(f"{voltage} Volt")
            print(voltage, "V")

        elif 'current if' in query:
            tmp = [int(s) for s in query.split() if s.isdigit()]
            current = tmp[0] / tmp[1]
            speak(f"{current} Amps")
            print(current, "A")

        elif 'power if' in query:
            tmp = [int(s) for s in query.split() if s.isdigit()]
            power = tmp[0] * tmp[1]
            speak(f"{power} joules")
            print(power, "J")

        elif 'capacitance if' in query:
            tmp = [int(s) for s in query.split() if s.isdigit()]
            capacitance = tmp[0] / tmp[1]
            speak(f"{capacitance} farad")
            print(capacitance, "F")

        elif 'charge if' in query:
            tmp = [int(s) for s in query.split() if s.isdigit()]
            charge = tmp[0] * tmp[1]
            speak(f"{charge} coulombs")
            print(capacitance, "Coulombs")

        elif 'open code' in query:
            codePath = "C:\\Users\Mani Shankar Das\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'mail to shubham' in query:
            try:
                speak("What should I say???")
                content = takeCommand()
                to = "subham40404@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir . I am not able to send this email")    