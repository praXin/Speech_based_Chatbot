import pyttsx
def TextToSpeech(text, choice):
    e = pyttsx.init()
    voices = e.getProperty('voices')
    if choice == 1:
        e.setProperty('voice', voices[1].id)
    elif choice == 2:
        e.setProperty('voice', voices[0].id)
    e.say(text)
    e.runAndWait()

      
