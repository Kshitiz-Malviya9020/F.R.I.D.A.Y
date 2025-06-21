import os
import subprocess
import webbrowser
from speech_engine import speak  
from gemini_chat import chat_with_gemini  
from recognizer import recognize_speech
import pyautogui
import time
from pywinauto import Application

def execute_command(command):
    # Open websites
    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        time.sleep(5)
        while True:
            command = recognize_speech()
            if command is None:
                speak("Sorry, could you specify what you want to do on YouTube?")
                continue

            if "search" in command:
                search_query = command.replace("search", "").strip()
                speak(f"Searching for {search_query} on YouTube.")
                pyautogui.press('/')  # Focus search bar
                pyautogui.write(search_query)
                pyautogui.press('enter')
                time.sleep(5)

            elif "play" in command and "video" in command:
                word_to_num = {
                    "first": 1,"second": 2,"third": 3,"fourth": 4,"fifth": 5,"sixth": 6,"seventh": 7,"eighth": 8,"ninth": 9,"tenth": 10
                }
                # Convert command into a list
                command_list = command.split()

                # Find the word representing the video position (first, second, etc.)
                position_word = None
                for word in command_list:
                    if word.lower() in word_to_num:
                        position_word = word.lower()
                        break

                # If a position word is found, proceed with the action
                if position_word:
                    # Get the position number from word_to_num dictionary
                    video_position = word_to_num[position_word]
                    speak(f"Playing the {position_word} video.")

                    # Press 'Tab' the appropriate number of times to reach the video
                    for _ in range(video_position):
                        pyautogui.press('tab')
                        time.sleep(0.2)

                    # Press 'Enter' to play the video
                    pyautogui.press('enter')

                    # Optional: Wait for the video to start
                    time.sleep(5)

            elif "pause" in command:
                speak("Pausing the video.")
                pyautogui.press('k')

            elif "play video" in command:
                speak("Resuming the video.")
                pyautogui.press('k')

            elif "full screen" in command:
                pyautogui.press('f')

            elif "exit full screen" in command:
                pyautogui.press('esc')

            elif "close youtube" in command or "stop" in command:
                speak("Closing YouTube interaction.")
                break
    elif "open spotify" in command:
        speak("Opening Spotify")
        os.system("spotify")
        time.sleep(5)
        while True:
            command = recognize_speech()
            if "play" in command:
                pass
        return
    
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
        return
    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
        return  
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")
        return
    # Open applications (Windows specific)
    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")
        return
    elif "open command prompt" in command or "open cmd" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")
        return
    elif "open camera" in command:
        speak("Opening Camera")
        subprocess.run("start microsoft.windows.camera:", shell=True)
        return  
    elif "open file explorer" in command:
        speak("Opening File Explorer")
        os.system("explorer")
        return    
    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")
        time.sleep(2)  # Let the calculator open
        while True:
            command = recognize_speech()
            if command is None:
                speak("Sorry, could you specify what you want to do with the calculator?")
                continue
            if "add" in command:
            # Extract all numbers from the command
                numbers = [int(s) for s in command.split() if s.isdigit()]
                
                if len(numbers) >= 2:
                    speak(f"Adding {' plus '.join(map(str, numbers))}")
                    time.sleep(1)

                    for index, number in enumerate(numbers):
                        pyautogui.write(str(number))
                        if index != len(numbers) - 1:
                            pyautogui.press('+')
                    pyautogui.press('enter')
                    speak("The result is displayed on the calculator.")
                else:
                    speak("Please provide at least two numbers to add.") 
            
             # Subtraction
            elif "subtract" in command or "minus" in command:
                numbers = [int(s) for s in command.split() if s.isdigit()]
                if len(numbers) >= 2:
                    speak(f"Subtracting {' minus '.join(map(str, numbers))}")
                    time.sleep(1)
                    for index, number in enumerate(numbers):
                        pyautogui.write(str(number))
                        if index != len(numbers) - 1:
                            pyautogui.press('-')
                    pyautogui.press('enter')
                    speak("The result is displayed on the calculator.")
                else:
                    speak("Please provide at least two numbers to subtract.")

            # Multiplication
            elif "multiply" in command or "times" in command:
                numbers = [int(s) for s in command.split() if s.isdigit()]
                if len(numbers) >= 2:
                    speak(f"Multiplying {' times '.join(map(str, numbers))}")
                    time.sleep(1)
                    for index, number in enumerate(numbers):
                        pyautogui.write(str(number))
                        if index != len(numbers) - 1:
                            pyautogui.press('*')
                    pyautogui.press('enter')
                    speak("The result is displayed on the calculator.")
                else:
                    speak("Please provide at least two numbers to multiply.")

            # Division
            elif "divide" in command or "division" in command:
                numbers = [int(s) for s in command.split() if s.isdigit()]
                if len(numbers) >= 2:
                    speak(f"Dividing {' divided by '.join(map(str, numbers))}")
                    time.sleep(1)
                    for index, number in enumerate(numbers):
                        pyautogui.write(str(number))
                        if index != len(numbers) - 1:
                            pyautogui.press('/')
                    pyautogui.press('enter')
                    speak("The result is displayed on the calculator.")
                else:
                    speak("Please provide at least two numbers to divide.")
            # closing the calculator
            # elif "close calculator" in command or "exit" in command or "close" in command:
            #     speak("Closing Calculator.")
            #     os.system("taskkill /f /im Calculator.exe")
            #     break
            elif "close calculator" in command or "exit" in command:
                speak("Closing Calculator.")
                try:
                    app = Application(backend="uia").connect(title_re=".*Calculator.*")
                    app.window(title_re=".*Calculator.*").close()
                except Exception as e:
                    speak("Calculator is not open or could not be closed.")
                    print(f"Error closing calculator: {e}")
                break
    elif "open task manager" in command:
        speak("Opening Task Manager")
        os.system("taskmgr")
        return
    else:
        answer = chat_with_gemini(command)
        print("Friday:", answer)
        speak(answer)