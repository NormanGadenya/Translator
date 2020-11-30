from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton,MDFloatingActionButton
from kivy.uix.label import Label
from kivy.uix.image import Image 
from kivy.core.window import Window
from kivy.core.text import LabelBase
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
from kivy.lang.builder import Builder
import threading 
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog

Window.size=(360,600) 
Builder.load_file("test.kv")
class ContainerBox(BoxLayout):
    pass
class TheTranslator(MDApp):
    icon='voice-1.png'
    language='en'
    language1='en'
    

    def show_data(self):
        help_data='To use the application \nchoose the language from  and then select the language to and then hit the translate button '
        close_btn=MDFlatButton(text='close',on_release=self.close_dialog)
        self.dialog=MDDialog(title='Help' ,text=help_data,size_hint_x=None,width=200,buttons=[close_btn])
        self.dialog.open()
                                                                                                                                                                                                                                                                   
    def close_dialog(self,obj):
        self.dialog.dismiss()

    def build(self):
        return ContainerBox() 
    def imageguy(self):
        self.root.ids.ande.source="mand.gif"

    def remove(self):
        self.root.ids.ande.sourc=''
        self.root.ids.anim.opacity=1
       
    def start_t(self):
        
        t=threading.Thread(target=self.tr)
        t.start()
        self.root.ids.ande.source="mand.gif"
        self.root.ids.ande.opacity=1
        
    def tr(self):
        global language
        global language1
        r=sr.Recognizer()
        try:
            with sr.Microphone() as source:
                audio=r.adjust_for_ambient_noise(source)
                toast('we are listening')     
                audio=r.listen(source)
                text=r.recognize_google(audio,language=language1)
            toast('you said: {}'.format(text))
            
            translator=Translator()
    
            mytext=translator.translate(text,dest=language).text
            myobj = gTTS(text=mytext, lang=language, slow=False) 
    
            myobj.save("speech.mp3")
            playsound('speech.mp3')
            os.remove("speech.mp3")
            self.root.ids.ande.source=''
            self.root.ids.ande.opacity=0
        except sr.RequestError:
            toast('no internet connection')
            self.root.ids.ande.source=''
            self.root.ids.ande.opacity=0
        except sr.UnknownValueError:
            toast('sorry we didnt get what you said')
            self.root.ids.ande.source=''
            self.root.ids.ande.opacity=0
        except sr.WaitTimeoutError:
            toast('Time out')
            self.root.ids.ande.source=''
            self.root.ids.ande.opacity=0
        
        except:
            toast('error')
            self.root.ids.ande.source=''
            self.root.ids.ande.opacity=0
            
    def eng(self):
        global language
        language='en'
        return language
    def ger(self):
        global language
        language='de'
        return language
    def fre(self):
        global language
        language='fr'
        return language
    def eng1(self):
        global language1
        language1='en'
        return language1
    def ger1(self):
        global language1
        language1='de'
        return language1
    def fre1(self):
        global language1
        language1='fr'
        return language1
    

#here is the animation

        
if __name__ == '__main__':
    LabelBase.register(name='MilkyNiceOne',fn_regular='MilkyNice.ttf')
    LabelBase.register(name='FeelingPassionate',fn_regular='Feeling Passionate.ttf')
    LabelBase.register(name='WalkwayUB',fn_regular='Walkway_UltraBold.ttf')
    TheTranslator().run()