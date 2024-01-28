import tkinter as tk
from tkinter import *
from tkinter import filedialog,Frame,PhotoImage
from tkinter.ttk import Combobox
import pyttsx3
import os
from gtts import gTTS
from playsound import playsound
root=Tk()
root.title("Text to Speech Converter")
root.geometry("1000x580+200+80")
root.resizable(True,True)
root.configure(bg="#CCFFCC")
#root.mainloop()
tts=pyttsx3.init()
def speaknow():
    text=text_box.get(1.0,END)
    gender=gender_box.get()
    speed=speed_box.get()
    voices=tts.getProperty('voices')
    
    def setvoice():
        if(gender=='Male'):
            tts.setProperty('voice',voices[0].id)
            tts.say(text)
            tts.runAndWait()
            else:
                tts.setProperty('voice',voices[1].id)
                tts.say(text)
                tts.runAndWait()
                
        if(text):
            if(speed=='Fast'):
                tts.setProperty('rate',250)
                setvoice()
            elif(speed=='Medium'):
                tts.setProperty('rate',150)
                setvoice()
            else:
                tts.setProperty('rate',60)
                setvoice()
logo=PhotoImage(file="C:/Users/KIIT/Desktop/images.png")
Label(root,image=logo,bg="#CCFFCC").place(x=880,y=539)
#root.mainloop()
logo_image=PhotoImage(file="C:/Users/KIIT/Desktop/lo.png")
root.iconphoto(False,logo_image)
#root.mainloop()
upper_frame= Frame(root,bg="#14A700",width=1300,height=130)
upper_frame.place(x=0,y=0)
picture=PhotoImage(file="C:/Users/KIIT/Desktop/MLProject/logo.jpeg")
Label(upper_frame,image=picture,bg="#14A700").place(x=90,y=10)
#root.mainloop()
Label(upper_frame,text="Text to Speech Converter",font="TimesNewroman 40 bold",bg="#14A700",fg='white').place(x=250,y=35)
#root.mainloop()
text_box=Text(root,font="calibri 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
text_box.place(x=30,y=150,width=940,height=180)
#root.mainloop()
gender_box=Combobox(root,values=['Male','Female'],font="Robote 12",state='r',width=12)
gender_box.place(x=340,y=400)
gender_box.set('Male')
#root.mainloop()
speed_box=Combobox(root,values=['Fast','Medium','Slow'],font="Robote 12",state='r',width=12)
speed_box.place(x=540,y=400)
speed_box.set('Medium')
#root.mainloop()
Label(root,text="Select Voice",font='TimesNewRoman 15 bold',bg="#CCFFCC",fg="black").place(x=340,y=370)
Label(root,text="Select Speed",font='TimesNewRoman 15 bold',bg="#CCFFCC",fg="black").place(x=340,y=370)
#root.mainloop()
play_button=PhotoImage(file="C:/Users/KIIT/Desktop/play_btnn.png")
play_btn=Button(root,text="Play",compound=LEFT,image=play_button,bg='white',width=130,font="arial 14 bold",borderwidth='0.1c',command=speaknow)
play_btn.place(x=435,y=450)
root.mainloop()
