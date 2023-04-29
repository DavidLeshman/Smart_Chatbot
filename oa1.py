import openai
import sounddevice as sd
import speech_recognition as sr
from scipy.io.wavfile import write
from playsound import playsound
import wavio as wv
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import datetime
import json
import numpy as np
import imageio
import imageio.v2 as imageio
import scipy.ndimage
import cv2
import pyjokes
from pydub import AudioSegment
from pydub.playback import play
openai.api_key = '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'
messages = [ {"role": "system", "content":
			"You are a intelligent assistant."} ]




i = 10
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
	print(type(audio_text))
	print(r.recognize_google(audio_text))
	r.recognize_google(audio_text)
	text1 =  r.recognize_google(audio_text)
	print(text1)










message = text1
if message:
	messages.append(
		{"role": "user", "content": message},
		)
	chat = openai.ChatCompletion.create(
		model="gpt-3.5-turbo", messages=messages
		)
	reply = chat.choices[0].message.content
	print(f"ChatGPT: {reply}")
	messages.append({"role": "assistant", "content": reply})
	from win32com.client import Dispatch
	speak = Dispatch("SAPI.Spvoice")
	speak.Speak(reply) 


