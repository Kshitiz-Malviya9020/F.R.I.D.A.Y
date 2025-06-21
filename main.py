import command_executor
import recognizer
import speech_engine
import wake_word_listener

while True:
    if wake_word_listener.listen_for_wake_word():
        while True:
            command = recognizer.recognize_speech()
            if command:
                if "stop listening" in command or "goodbye" in command or "exit" in command:
                    speech_engine.speak("Okay sir, See you next time.")
                    break
                else:
                    command_executor.execute_command(command)
