#converts speech from english to french
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
r=sr.Recognizer()
with sr.Microphone() as source:
    print('speak anything')
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print('you said: {}'.format(text))
    
translator=Translator()
mytext=translator.translate(text,dest='fr').text

myobj = gTTS(text=mytext, lang='fr', slow=False) 
myobj.save("speech.mp3")
playsound('speech.mp3')
os.remove("speech.mp3")
