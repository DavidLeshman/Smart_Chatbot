import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import wavio as wv
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import datetime
import json
import pyjokes

i = 10
while i < 1000:
    freq = 44100
    duration = 7
    recording = sd.rec(int(duration * freq), 
                       samplerate=freq, channels=2)
    sd.wait()
    write("recording0.wav", freq, recording) 
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
        weather="can you tell me the weather"
        news="tell me the latest news"
        joke="tell me a joke"
        close1 ="shutdown"
        time= "tell me the time"
        

        
        if text1 == hey:
            x = datetime.datetime.now()
            print(x)
            class MusicPlayer:
                def __init__(self, window ):
                    window.geometry('320x100'); window.title('Music Player'); window.resizable(0,0)
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
            

            
            
        elif text1 == weather:
            print("Which city do you want the weather data from?")
    
            freq = 44100
            duration = 5
            recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
            sd.wait()
            write("recording1.wav", freq, recording) 
            wv.write("recording1.wav", recording, freq, sampwidth=2)
            r = sr.Recognizer()
            file_audio = sr.AudioFile('recording3.wav')
            with file_audio as source:
                audio_text = r.record(source)
                print(r.recognize_google(audio_text))
                text1 =  r.recognize_google(audio_text)
                print(text1)
                city = text1
                print("Weather data from "+city)
                url = "https://www.google.com/search?q="+"weather"+city
                html = requests.get(url).content
                soup = BeautifulSoup(html, 'html.parser')
                temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
                str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
                data = str.split('\n')
                time = data[0]
                sky = data[1]
                listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
                strd = listdiv[5].text
                pos = strd.find('Wind')
                other_data = strd[pos:]
                print("Temperature is", temp)
                print("Time: ", time)
                print("Sky Description: ", sky)
                
                
  
                
                
                
        elif text1 == joke:
            if text1 == hey:
                My_joke = pyjokes.get_joke(language="en", category="neutral")
  
                print(My_joke)
        elif text1 == close1:
            break
    
        elif text1 == time:
            x = datetime.datetime.now()
            print(x)
            from win32com.client import Dispatch
            speak = Dispatch("SAPI.Spvoice")
            speak.Speak(x)  
            
            

            
            
        elif text1 == news:
            def NewsFromBBC():
                query_params = {
                  "source": "bbc-news",
                  "sortBy": "top",
                  "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
                }
                main_url = " https://newsapi.org/v1/articles"
                res = requests.get(main_url, params=query_params)
                open_bbc_page = res.json()
                article = open_bbc_page["articles"]
                results = []
                for ar in article:
                    results.append(ar["title"])  
                for i in range(len(results)):
                    print(i + 1, results[i])
                from win32com.client import Dispatch
                speak = Dispatch("SAPI.Spvoice")
                speak.Speak(results)                
            if __name__ == '__main__':
                NewsFromBBC()
                        

            
        else:
            print("Sorry couldnt hear you. Can you try again?")


