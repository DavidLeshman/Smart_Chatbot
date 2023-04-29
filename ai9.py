import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import wavio as wv
import requests
from bs4 import BeautifulSoup

from tkinter import *
from tkinter import filedialog
from pygame import mixer



## FOR ADDING TIME PART WE NEED TO USE DATETIME




import datetime



import json


# for adding jokes we are gonna use pyjokes



import pyjokes








##FOR ACTIVATING ALEXA USE KEY WORD ALEXA



















# Sampling frequency
freq = 44100
# Recording duration
duration = 5
# Start recorder with the given values 
# of duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
# Record audio for the given number of seconds
sd.wait()
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording) 
# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)


r = sr.Recognizer()

file_audio = sr.AudioFile('recording1.wav')

with file_audio as source:
    audio_text = r.record(source)

    #print(type(audio_text))
    print(r.recognize_google(audio_text))
    #r.recognize_google(audio_text)
    text1 =  r.recognize_google(audio_text)
    #print(text1)
    hey= "Alexa"
    if text1 == hey:
        print("Hello Shriyash")
    else:
        print("Try again")
 
 
 
 
 
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
# Record audio for the given number of seconds
sd.wait()
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording) 
# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)




udioFile('recording1.wav')

with file_audio as source:
    audio_text = r.record(source)

    #print(type(audio_text))
    print(r.recognize_google(audio_text))
    #r.recognize_google(audio_text)
    text1 =  r.recognize_google(audio_text)
    print(text1)
    hey= "tell me the latest news"
    if text1 == hey:
        x = datetime.datetime.now()
        print(x)



def NewsFromBBC():
     
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    # getting all articles in a string article
    article = open_bbc_page["articles"]
 
    # empty list which will
    # contain all trending news
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
         
        # printing all trending news
        print(i + 1, results[i])
 
    #to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)                
 
# Driver Code
if __name__ == '__main__':
     
    # function call
    NewsFromBBC()





    



#music player part



# Sampling frequency
freq = 44100
# Recording duration
duration = 7
# Start recorder with the given values 
# of duration and sample frequency
recording = sd.rec(int(duration * freq), 
                   samplerate=freq, channels=2)
# Record audio for the given number of seconds
sd.wait()
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording) 
# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)


r = sr.Recognizer()

file_audio = sr.AudioFile('recording1.wav')

with file_audio as source:
    audio_text = r.record(source)

    #print(type(audio_text))
    print(r.recognize_google(audio_text))
    #r.recognize_google(audio_text)
    text1 =  r.recognize_google(audio_text)
    #print(text1)
    hey= "open the music player"
    if text1 == hey:
        x = datetime.datetime.now()
        print(x)
        
        



class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x100'); window.title('Iris Player'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  width = 10, font = ('Times', 10), command = self.load)
        Play = Button(window, text = 'Play',  width = 10,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause',  width = 10, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 10, font = ('Times', 10), command = self.stop)
        Load.place(x=0,y=20);Play.place(x=110,y=20);Pause.place(x=220,y=20);Stop.place(x=110,y=60) 
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MusicPlayer(root)
root.mainloop()