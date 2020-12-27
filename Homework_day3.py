from random import choice
from time import sleep


Turkey_Cities =['ADANA', 'ADIYAMAN', 'AFYON', 'AĞRI', 'AMASYA', 'ANKARA', 'ANTALYA', 'ARTVIN',
          'AYDIN', 'BALIKESIR', 'BILECIK', 'BINGÖL', 'BITLIS', 'BOLU', 'BURDUR', 'BURSA', 'ÇANAKKALE',
          'ÇANKIRI', 'ÇORUM', 'DENIZLI', 'DIYARBAKIR', 'EDIRNE', 'ELAZIĞ', 'ERZINCAN', 'ERZURUM', 'ESKIŞEHIR',
          'GAZIANTEP', 'GIRESUN', 'GÜMÜŞHANE', 'HAKKARI', 'HATAY', 'ISPARTA', 'MERSIN', 'ISTANBUL', 'IZMIR',
          'KARS', 'KASTAMONU', 'KAYSERI', 'KIRKLARELI', 'KIRŞEHIR', 'KOCAELI', 'KONYA', 'KÜTAHYA', 'MALATYA',
          'MANISA', 'KAHRAMANMARAŞ', 'MARDIN', 'MUĞLA', 'MUŞ', 'NEVŞEHIR', 'NIĞDE', 'ORDU', 'RIZE', 'SAKARYA',
          'SAMSUN', 'SIIRT', 'SINOP', 'SIVAS', 'TEKIRDAĞ', 'TOKAT', 'TRABZON', 'TUNCELI', 'ŞANLIURFA', 'UŞAK',
          'VAN', 'YOZGAT', 'ZONGULDAK', 'AKSARAY', 'BAYBURT', 'KARAMAN', 'KIRIKKALE', 'BATMAN', 'ŞIRNAK',
          'BARTIN', 'ARDAHAN', 'IĞDIR', 'YALOVA', 'KARABÜK', 'KILIS', 'OSMANIYE', 'DÜZCE']

name = input("Adınızı ve Soyadınızı arasından boşluk bırakarak girin :").upper()

print("Merhaba {} Seninle Bir oyuna başlıyoruz!".format(name))
sleep(1)
print("Harflerini tek tek girerek Türkiye'deki bir şehirin adını tahmin etmeye çalışacağız")
print("Hadi Başlayalım")
sleep(3)

city = choice(Turkey_Cities)
selects = ''.upper()
turns = len(city)

print(city)
print(f"Seçilen şehrimiz {turns} harfli. Bakalım bulabilecek misin")
while turns > 0:
    failed = 0

    for n in city:
        if n in selects:
            print(n)

        else:
            print("*")
            failed += 1
    if failed == 0:
        print("KAZANDINNNNN!")
        print("Kelime {} 'di: ".format(city))
        break

    select = input("Hadi bir harf gir: ").upper()
    selects += select

    if select not in city:
        turns -= 1
        print("Yanlış harfi seçitin.")
        print( turns, "bulman için harf kaldı")

        if turns == 0:
            print("Çok Üzgünüm, Kaybettin... ")
            print("Rasgele seçilen şehir, Ülkemizin güzide şehirlerinden biri olan : ", city)

