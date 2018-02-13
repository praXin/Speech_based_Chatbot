from watson_developer_cloud import SpeechToTextV1
from Tkinter import *
from PIL import Image
import json
import StringIO
import pyaudio
import wave
import os
import re
import pyttsx
import random
import stt
import remain
import TextToInteger
import text_to_speech
import CtoPython

def working1(event):
    while(True):
        text1 = stt.SpeechToText()
        print("YOU: "+text1)
        if (text1.upper() == "BYE ") or (text1.upper() == "QUIT ") or (text1.upper() == "BYE") or (text1.upper() =="QUIT"):
            break
        else:
            text2 = CtoPython.Heart(text1)
            print("BOT: "+text2)
            text_to_speech.TextToSpeech(text2, 2)
 

def working2(event):
    while(True):
        text1 = stt.SpeechToText()
        print "YOU: "+text1
        if (text1.upper() == "BYE ") or (text1.upper() == "QUIT ") or (text1.upper() == "BYE") or (text1.upper() =="QUIT"):
            break
        else:
            text2 = CtoPython.Heart(text1)
            print "BOT: "+text2
            text_to_speech.TextToSpeech(text2, 1)
"""
def remind1(event):
    textRemind=e1.get()
    textTime=int(e2.get())
    remain.Reminder(textTime, textRemind)
"""
root = Tk()

frame = Frame(width=300, height=300)
frame.pack(side=RIGHT, fill=BOTH)

"""
Label(root, text="Reminder").grid(row=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
Label(root, text="Time(in min) from now").grid(row=0, column=2)
e2 = Entry(root)
e2.grid(row=0, column=3)
Button(root, text='Set!', command=remind1).grid(row=0, column=4)
"""
button1 = Button(root, text="Speak To a Male assistant")
button1.bind("<Button-1>", working1)
button1.pack()
button2 = Button(root, text="Speak To a Female assistant")
button2.bind("<Button-1>", working2)
button2.pack()

status = Label(root, text="Listening...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()