import datetime
import sqlite3

import pandas as pd


class DataBase:

    def __init__(self):
        self.conn=sqlite3.connect("LambaVerileri.db")
        self.cursor=self.conn.cursor()
        self.__tabloOlustur()
    def __tabloOlustur(self):
        s="Create table if not exists LambaTablo (Saat DateTime,Tarih DateTime,Durum INT)"
        self.cursor.execute(s)
        self.conn.commit()

    def veriEkle(self,tarih:datetime,durum:int):

        __saat=tarih.strftime("%H:%M").replace(":",".")
        __tarih=tarih.strftime("%D").replace("/",".")

        # Sorguyu oluştur ve çalıştır
        sorgu = "SELECT * FROM LambaTablo WHERE Saat = ? AND  Durum= ?"
        self.cursor.execute(sorgu, (__saat, durum))
        sonuc = self.cursor.fetchone()

        if sonuc is None:
            sorgu_insert="Insert into LambaTablo values (?,?,?)"
            self.cursor.execute(sorgu_insert,(__saat,__tarih,durum))
            print("Veri Başarıyla Eklendi")
        else:
            print("veri zaten var")
        self.conn.commit()
    def verileriGetir(self):
        s="Select * from LambaTablo"
        #liste=self.cursor.execute(s).fetchall()
        data=pd.read_sql(s,self.conn)

        return data


