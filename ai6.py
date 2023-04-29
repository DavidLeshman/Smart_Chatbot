import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import wavio as wv
import requests
from bs4 import BeautifulSoup
import pyjokes

import datetime













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
    print(text1)
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



#say ur ques

r = sr.Recognizer()

file_audio = sr.AudioFile('recording1.wav')

with file_audio as source:
   audio_text = r.record(source)

#print(type(audio_text))
print(r.recognize_google(audio_text))
 #r.recognize_google(audio_text)
text1 =  r.recognize_google(audio_text)
print(text1)



hey= "weather"
if text1 == hey:
    
       
    
    print("Which city do you want the weather data from?")
    
    freq = 44100
    # Recording duration
    duration = 5
    # Start recorder with the given values 
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
# Record audio for the given number of seconds
    sd.wait()
# This will convert the NumPy array to an audio
# file with the given sampling frequency
    write("recording2.wav", freq, recording) 
# Convert the NumPy array to audio file
    wv.write("recording3.wav", recording, freq, sampwidth=2)
    r = sr.Recognizer()

    file_audio = sr.AudioFile('recording3.wav')

    with file_audio as source:
        audio_text = r.record(source)

        #print(type(audio_text))
        print(r.recognize_google(audio_text))
        #r.recognize_google(audio_text)
        text1 =  r.recognize_google(audio_text)
        print(text1)
    
    
        city = text1
        print("Weather data from "+city)
        # creating url and requests instance
        url = "https://www.google.com/search?q="+"weather"+city
        html = requests.get(url).content
 
        # getting raw data
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
        str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
 
        # formatting data
        data = str.split('\n')
        time = data[0]
        sky = data[1]
 
        # getting all div tag
        listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
        strd = listdiv[5].text
 
        # getting other required data
        pos = strd.find('Wind')
        other_data = strd[pos:]
 
        # printing all data
        print("Temperature is", temp)
        print("Time: ", time)
        print("Sky Description: ", sky)
        # print(other_data)




r = sr.Recognizer()

file_audio = sr.AudioFile('recording1.wav')

with file_audio as source:
   audio_text = r.record(source)

#print(type(audio_text))
print(r.recognize_google(audio_text))
 #r.recognize_google(audio_text)
text1 =  r.recognize_google(audio_text)
print(text1)



            hey= "tell me a joke"
            joke1 = "tell me a joke"
            if joke1 == hey:
                My_joke = pyjokes.get_joke(language="en", category="neutral")
  
                print(My_joke)
            else:
                print("Try Again")

            freq = 44100
            duration = 10
            recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
            sd.wait()
            write("recording0.wav", freq, recording) 
            wv.write("recording1.wav", recording, freq, sampwidth=2)
            r = sr.Recognizer()
            file_audio = sr.AudioFile('recordin1.wav')
            with file_audio as source:
                audio_text = r.record(source)
                print(r.recognize_google(audio_text))
                print()
                text1 =  r.recognize_google(audio_text)
                print(text1)
                time1 = "can u tell me the time"
                if time1 == text1:
                    tm = datetime.time(1, 50, 20, 133257)
  
                    print('Time tm is ',
                    tm.hour, ' hours ',
                    tm.minute, ' minutes ',
                    tm.second, ' seconds and ',
                    tm.microsecond, ' microseconds' )
                else:
                    print("Try Again")
else:
    print("Try again")
    
    






    
    
    




