# Project Title->Text to Speech converter
Developed a Python-based Text-to-Speech converter using pyttsx3 and gTTS libraries, seamlessly integrated with a Tkinter interface. Utilized machine learning for efficient natural language processing, delivering an innovative solution for text-to-speech conversion

## Installation
To install the pyttsx3 and gTTS libraries, you can use the following commands in your terminal or command prompt:
pip install pyttsx3
pip install gtts
Make sure you have Python and pip installed on your system.

Once installed, you can use these libraries in your Python script. Here's an example of how to import them along with tkinter for building a simple Text-to-Speech converter:
import tkinter as tk
from gtts import gTTS
import pyttsx3

def text_to_speech():
    text = entry.get()
    
    # Using pyttsx3
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

    # Using gTTS
    tts = gTTS(text)
    tts.save("output.mp3")  # You can use any file name and extension you prefer

# GUI setup
root = tk.Tk()
root.title("Text-to-Speech Converter")

label = tk.Label(root, text="Enter text:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Convert", command=text_to_speech)
button.pack()

root.mainloop()


## Code Structure
`text_to_speech.py`: Main file for the text-to-speech conversion.
