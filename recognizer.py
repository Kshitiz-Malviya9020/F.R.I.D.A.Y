import speech_recognition as sr
from speech_engine import speak

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Reduce background noise
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that.")
            speak("Sorry, I couldn't understand that.")
            return None
        except sr.RequestError:
            print("Could not connect to speech recognition service.")
            speak("Could not connect to speech recognition service.")
            return None
        except sr.WaitTimeoutError:
            print("Listening timed out. Please speak again.")
            speak("Listening timed out. Please speak again.")
            return None