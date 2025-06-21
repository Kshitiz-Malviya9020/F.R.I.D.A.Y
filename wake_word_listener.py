import json
import vosk
import pyaudio
import random
import speech_engine

# Load VOSK Model
model = vosk.Model("vosk_model")
recognizer = vosk.KaldiRecognizer(model, 16000)
pa = pyaudio.PyAudio()
stream = pa.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=8192
)
stream.start_stream()

def listen_for_wake_word():
    print("Waiting for wake word...")
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            text = result.get("text", "").lower()
            print(f"Heard: {text}")
            if "friday" in text:
                greetings = [
                    "At your service, sir.",
                    "Ready when you are.",
                    "What can I help with today?"
                ]
                speech_engine.speak(random.choice(greetings))
                return True
