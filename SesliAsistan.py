import datetime
import random
import time
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import pyaudio
import os
import RobotikKodlama
import VeriTabani


class SesliAsistan:

    def __init__(self):
        self.r = sr.Recognizer()
        self.rb = RobotikKodlama.RoboticIslem()
        self.db = VeriTabani.DataBase()
        #print(self.db.verileriGetir())
    def seslendirme(self, metin):
        metin_seslendirme = gTTS(text=metin, lang="tr")
        dosya = str(random.randint(0, 10000000000)) + ".mp3"
        metin_seslendirme.save(dosya)
        playsound(dosya)
        os.remove(dosya)

    def mikrofon(self):

        with sr.Microphone() as kaynak:
            print("Sizi dinliyorum..")
            listen = self.r.listen(kaynak)
            ses = ""
            try:
                ses = self.r.recognize_google(listen, language="tr-TR")
            except sr.UnknownValueError:
                self.seslendirme("ne dediğinizi anlayamadım")
            return ses.lower()

    def sesKarslik(self, gelen_Ses):

        if gelen_Ses in "lambayı yak":
            self.seslendirme("Lambanızı hemen açıyorum...")
            time.sleep(1)
            self.db.veriEkle(datetime.datetime.now(),1)
            self.rb.lambaIslem(1)

        elif gelen_Ses in "lambayı kapat":
            self.seslendirme("Lambanızı kapatıyorum...")
            self.db.veriEkle(datetime.datetime.now(), 0)
            self.rb.lambaIslem(0)

        elif gelen_Ses in "merhaba":
            print("merhabalar")

    def uyanmaFonksiyonu(self, gelen_Ses):
        if (gelen_Ses in "hey siri"):
            self.seslendirme("dinliyorum...")
            ses = self.mikrofon()
            if (ses != ""):
                print(ses)
                self.sesKarslik(ses)
                time.sleep(1)
                self.rb.otomatikLamba()


asistan = SesliAsistan()

while True:
    gelen_Ses = asistan.mikrofon()
    if (gelen_Ses != ""):
        print(gelen_Ses)
        asistan.uyanmaFonksiyonu(gelen_Ses)

