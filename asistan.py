import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import random
import time
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
    if "bende iyiyim" in voice:
        speak("Allah iyilik versin")
    if "görüşürüz" in voice:
        selection = ["görüşürüz yavrum","bi siktir git artık","sonunda","görüşmek üzere"]
        selection = random.choice(selection)
        speak(selection)
        exit()
    if "tarih" in voice:
        today = time.strftime("%A")
        today = today.lower()
        if today == "monday":
            today = "pazartesi"
        elif today == "tuesday":
            today = "salı"
        elif today == "wednesday":
            today = "çarşamba"
        elif today == "thursday":
            today = "perşembe"
        elif today == "friday":
            today = "cuma"
        elif today == "saturday":
            today = "cumartesi"
        else:
            today = "pazar"
        month = time.strftime("%B")
        if month == "january":
            month = "ocak"
        elif month == "february":
            month = "şubat"
        elif month == "march":
            month = "mart"
        elif month == "april":
            month = "nisan"
        elif month == "may":
            month = "mayıs"
        elif month == "june":
            month = "haziran"
        elif month == "july":
            month = "temmuz"
        elif month == "august":
            month = "ağustos"
        elif month == "september":
            month = "eylül"
        elif month == "october":
            month = "ekim"
        elif month == "november":
            month = "kasım"
        else:
            month = "aralık"
        speak("tarih",today,month,time.strftime("%Y"))
    if "hangi yıldayız" in voice:
        speak(time.strftime("%Y")+" yılındayız")
    if "hangi aydayız" in voice:
        month = time.strftime("%B")
        if month == "january":
            month = "ocak"
        elif month == "february":
            month = "şubat"
        elif month == "march":
            month = "mart"
        elif month == "april":
            month = "nisan"
        elif month == "may":
            month = "mayıs"
        elif month == "june":
            month = "haziran"
        elif month == "july":
            month = "temmuz"
        elif month == "august":
            month = "ağustos"
        elif month == "september":
            month = "eylül"
        elif month == "october":
            month = "ekim"
        elif month == "november":
            month = "kasım"
        else:
            month = "aralık"
        speak(month+" ayındayız")
    if "hangi gündeyiz" in voice:
        today = time.strftime("%A")
        today = today.lower()
        if today == "monday":
            today = "pazartesi"
        elif today == "tuesday":
            today = "salı"
        elif today == "wednesday":
            today = "çarşamba"
        elif today == "thursday":
            today = "perşembe"
        elif today == "friday":
            today = "cuma"
        elif today == "saturday":
            today = "cumartesi"
        else:
            today = "pazar"
        speak("bugün "+today)
    if "saat kaç" in voice:
        selection = ["şu anda saat","saat","hemen bakıyorum saat","eti kemik geçiyor"]
        selection = random.choice(selection)
        if selection == "eti kemik geçiyor":
            speak(selection)
        else:
            clock = time.strftime("%H %M")
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
    selection = ["saat","sana nasıl yardımcı olabilirim","size nasıl yardım edebilirim","gene ne var","beş dakika uyutmadınız dır dır dır ne var söyle","merhaba"]
    selection = random.choice(selection)
    if selection == "saat":
        clock = time.strftime("%H")
        if clock<11:
            selection = ["günaydın bugün sana nasıl yardımcı olabilirim","bu saatte mesaiye mi çağırılır","günaydın","sabah sabah beni neden uyandırdın","daha kargalar sikini duvara sürtmediler beni neden uyandırdın"]
            selection = random.choice(selection)
            speak(selection)
        elif clock<16:
            speak("tünaydın sana nasıl yardım edebilirim")
        else:
            selection = ["iyi akşamlar","iyi akşamlar hayırdır bu saatte","bu saate mesaiyede çağrılmaz ki","akşam akşam beni neden rahatsız ettin"]
            selection = random.choice(selection)
            speak(selection)
    else:
        speak(selection)
    while True:
        voice = record()
        if voice != "":
            voice = voice.lower()
            print(voice)
            responce(voice)
