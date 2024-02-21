# Makine Öğrenmesi ile IoT Sistemi Oluşturma

Bu proje, sesli komutlarla ampul kontrolü sağlayan ve arka planda ampul-zaman sistemini takip eden bir IoT sistemi oluşturmayı amaçlar. Makine öğrenmesi algoritmaları, bu değerleri analiz ederek ampul açma/kapama kararlarını otomatik olarak verir.

## Teknolojiler ve Araçlar:
-Python / Makine Öğrenmesi Algoritmaları 
-Arduino / Röle (5V) / 15W Ampul (Voltajı fark etmez 220V uyumlu olması yeterli)
-Sklearn / Linear Model / LogisticRegression
-Ses Tanıma Teknolojileri / Speech_recognition / PyAudio / Playsound
-Veri Tabanı (SQL)

## Projenin çalışma mantığı
 Sesli komut ile kişisel asistana "Lambayı Aç" komutu gönderildiği zaman arka planda veri tabanına Arduino ve DHT11 nem ve sıcaklık sensörü ile veriler kaydedilir ve ardından makine öğrnemesi algoritaması (Logistic Reg) ile bu veriler eğitilir ve tahminde bulunması sağlanır. Ardından asistanı her çağırdımız zaman makine tahmin ile otomatik Ampul işlemleri gerçekleştirilir.


<div align="center">
  <img  src="https://github.com/TKN-YZM/KlimaML/blob/master/Z1.jpg" alt="Proje Çizim">
  <img  src="https://github.com/TKN-YZM/KlimaML/blob/master/Z2.jpg" alt="Proje Kod">
</div>