import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:

	try:

		with speech_recognition.Microphone() as mic1:

			recognizer.adjust_for_ambient_noise(mic1,duration=0.2)
            	 	audio = recognizer.listen(mic1)

 	 	        text = recognizer.recognize_google(audio)
            		text = text.lower()

            		print(f"Recognized {text}")
            		word = "alexa what is the weather"
            		if text == word:
                		print("The weather is 32C")
            		else:
                		print("hi")
				

    	except:
		recognizer.adjust_for_ambient_noise(mic1,duration=0.2)
            	audio = recognizer.listen(mic1)

 	        text = recognizer.recognize_google(audio)
       		text = text.lower()

       		print(f"Recognized {text}")
        	continue