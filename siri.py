import pyttsx3
import speech_recognition 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
rate = engine.setProperty("rate",100)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "hi" in query:
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "ok bye" in query:
                    speak("Ok sir , You can me call anytime")
                    break 
                elif "hello" in query:
                    speak("Hello nayan, how are you ?")
                elif "i am fine" in query:
                    speak("That's great")
                elif "how are you" in query:
                    speak("I am fine sir")
                elif "thank you" in query:
                    speak("Welcome sir, I am here only for you")
                elif "who is rp" in query:
                    speak("R p means Rajesh Patra , is a profesor in Hooghly Engineering and Technology college. He is the H O D of basic science department in this college. Probability and Statics are the favorite part of mister R P sir")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)
