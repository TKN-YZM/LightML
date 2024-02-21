import datetime

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  confusion_matrix
import  VeriTabani


class MachineLearning:
    def __init__(self):
        self.db=VeriTabani.DataBase()
        self.alldata=self.db.verileriGetir()
        saat=self.alldata[["Saat"]]
        tarih=self.alldata[["Tarih"]]
        durum=self.alldata[["Durum"]]
        self.x_Train,self.x_Test,self.y_Train,self.y_Test=train_test_split(saat,durum,test_size=0.3,random_state=2)

    def __tahminOrani(self,data_true,data_predict):
        cf=confusion_matrix(data_true,data_predict)
        # True Positive  ---
        tp = cf[1, 1]
        # False Positive (FP)
        fp = cf[0, 1]
        # True Negative (TN) --
        tn = cf[0, 0]
        # False Negative (FN)
        fn = cf[1, 0]
        istatistic = (tp + tn) / (tp + fp + tn + fn) * 100
        print("Algoritma Başarı İstatistik: ", istatistic)
        return (tp + tn) / (tp + fp + tn + fn) * 100

    def tahminAlgoritma(self,saat:float):
        lgr=LogisticRegression()
        lgr.fit(self.x_Train.values,self.y_Train.values.ravel())
        predict=lgr.predict(self.x_Test.values)
        self.__tahminOrani(self.y_Test,predict)
        return lgr.predict([[saat]])



