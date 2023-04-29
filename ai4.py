import speech_recognition
import requests
from bs4 import BeautifulSoup
import pyttsx3
recognizer = speech_recognition.Recognizer()
while True:
	try:
		with speech_recognition.Microphone() as mic:
			recognizer.adjust_for_ambient_noise(miz,duration=0.2)
			audio = recognizer.listen(mic)
			text = recognizer.recognize_google(audio)
			text = text.lower()
			
			print(f"Recognized {text}")
			word = "alexa what is the weather"
			
			if(text == word):
				recognizer.adjust_for_ambient_noise(miz,duration=0.2)
				audio = recognizer.listen(mic)
				text1 = recognizer.recognize_google(audio)
				text1 = text.lower()
				url=f"https://www.google.com/search?&q={text1}"
				r = requests.get(url)
				soup = BeautifulSoup(r.text,"html.parser")
				update=soup.find("div",class_="BNeawe").text
				print(f"{text} now is {update}")
    except:
        print("hi")    