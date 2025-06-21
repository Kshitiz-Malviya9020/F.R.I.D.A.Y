import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()
def speak(text): 
    """Converts text to speech"""
    engine.say(text)
    engine.runAndWait()