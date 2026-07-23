import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    speaker.Speak("Hello Siddik, I am Jarvis AI.")
    s = input()
    speaker.Speak(s)