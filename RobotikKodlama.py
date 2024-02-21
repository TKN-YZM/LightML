import datetime
import serial
import MakineAlgoritmasi as ML
import time


class RoboticIslem():

    def __init__(self):
        self.port="COM4"
        self.band=9600

    def lambaIslem(self,durum:int):
        arduino_port = "COM4"  # Arduino'nun bağlı olduğu port (Windows'ta "COMx" olabilir)
        baud_rate = 9600  # Arduino ile aynı baud hızı

        arduino = serial.Serial(arduino_port, baud_rate)
        time.sleep(2)  # Arduino'nun hazır olması için biraz bekle

        arduino.write(str(durum).encode())  # Komutu Arduino'ya gönder

    def otomatikLamba(self):
        saat=float(datetime.datetime.now().strftime("%H.%M"))
        predict=ML.MachineLearning().tahminAlgoritma(saat)
        if predict:
            print("Lamba Açık")
            self.lambaIslem(1)
        else:
            print("Lamba Kapalı")
            self.lambaIslem(0)

