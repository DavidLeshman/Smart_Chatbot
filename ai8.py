import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
import wavio as wv
import requests
from bs4 import BeautifulSoup





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











#say ur ques




# HERE IN THIS CASE WE WILL ASK FOR THE WEATHER FUNCTION








r = sr.Recognizer()

file_audio = sr.AudioFile('recording1.wav')

with file_audio as source:
   audio_text = r.record(source)

#print(type(audio_text))
print(r.recognize_google(audio_text))
 #r.recognize_google(audio_text)
text1 =  r.recognize_google(audio_text)
print("You asked for  "+text1+". Could you specify ?")



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
        #print(text1)
    
    
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















## FOR JOKES PART









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
    hey= "tell me a joke"
    if text1 == hey:
        My_joke = pyjokes.get_joke(language="en", category="neutral")
  
        print(My_joke)
    else:
        print("Try again")
        
        













## part for time code 









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
    hey= "tell me the time"
    if text1 == hey:
        x = datetime.datetime.now()
        print(x)
    else:
        print("Try again")
        





















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




