#To convert text to speech
# pip install gTTS to install this module
from gtts import gTTS
import os
  
speech = input("Enter text to be convert in speech(English) : ")
speech = gTTS(text=speech, lang = 'en' , slow=False)
speech.save("speech.mp3")
os.system("speech.mp3")     #audio will be played