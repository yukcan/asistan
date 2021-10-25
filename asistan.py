import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
import time
from datetime import datetime
import webbrowser
import requests
from bs4 import BeautifulSoup

r = sr.Recognizer()

def speak(read):
    tts = gTTS(text= read, lang="tr")
    file = "answer.mp3"
    tts.save(file)
    print(read)
    playsound(file)
    os.remove(file)

def record():
    with sr.Microphone() as source:
        print("dinliyorum")
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            speak("anlayamadım lütfen tekrar söyle")
        except sr.RequestError:
            speak("sistem çalışmıyor")
        return voice

wakeUp = False
while True:
    voice = record()
    if voice != "":
        voice = voice.lower()
        print(voice)
        if "alo" in voice:
            print("uyandım")
            wakeUp = True
            break

def responce(voice):
    if "nasılsın" in voice:
        selection = ["iyiyim sen nasılsın","iyiyim siz nasılsınız","iyiyim sen nasılsınız","bu seni hiç alakadar etmez","nasıl olalım yuvarlanıp gidiyoruz sen nasılsın","dolar","euro"]
        selection = random.choice(selection)
        if selection == "dolar":
            s = requests.get("https://bigpara.hurriyet.com.tr/doviz/dolar/")
            soup = BeautifulSoup(s.content,"lxml")
            soup = soup.find("span",attrs={"class":"value up"}).text
            speak("dolar olmuş "+soup+" nasıl olmamı bekliyorsun")
        elif selection == "euro":
            s = requests.get("https://bigpara.hurriyet.com.tr/doviz/euro/")
            soup = BeautifulSoup(s.content,"lxml")
            soup = soup.find("span",attrs={"class":"value up"})
            speak("euro "+soup+" olmuş neyseki maaşımı euroyla almıyorum")
        else:
            speak(selection)
    if "görüşürüz" in voice:
        selection = ["görüşürüz yavrum","bi siktir git artık","sonunda","görüşmek üzere"]
        selection = random.choice(selection)
        speak(selection)
        exit()
    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today = today.lower()
        if today == "monday":
            today = "pazartesi"
        elif today == "tuesday":
            today == "salı"
        elif today == "wednesday":
            today == "çarşamba"
        elif today == "thursday":
            today == "perşembe"
        elif today == "friday":
            today == "cuma"
        elif today == "saturday":
            today == "cumartesi"
        else:
            today == "pazar"
        speak("bugün"+today)
    if "saat kaç" in voice:
        selection = ["şu anda saat","saat","hemen bakıyorum saat","eti kemik geçiyor"]
        selection = random.choice(selection)
        if selection == "eti kemik geçiyor":
            speak(selection)
        else:
            clock = datetime.now().strftime("%H %M")
            speak(selection + clock)
    if "google'da ara" in voice:
        selection = ["google'da ne aratmamı istersin","google'da ne aramak istiyorsun","lütfen aratmak istediğin şeyi söyle"]
        selection = random.choice(selection)
        speak(selection)
        while True:
            search = record()
            if search != "":
                url = "https://www.google.com/search?q=" + search
                webbrowser.get().open(url)
                break

if wakeUp:
    selection = ["sana nasıl yardımcı olabilirim","size nasıl yardım edebilirim","gene ne var","beş dakika uyutmadınız dır dır dır ne var söyle","merhaba"]
    selection = random.choice(selection)
    speak(selection)
    while True:
        voice = record()
        if voice != "":
            voice = voice.lower()
            print(voice)
            responce(voice)