from time import sleep
from os import system

studentlist = []
lessons = []
examinfo = {}
courselist = ["Matematik","İstatistik","Ekonometri","İstatistiksel Analiz","İktisadi Analiz","İktisat","İşletme"]

def main_menu():
    print("""
    [1] Öğrenci Kaydı Oluştur
    [2] Öğrenci Girişi
    """)
    select = input("Lütfen bir işlem seçiniz : ")
    if select == "1":
        system('cls')
        create_student()
    elif select == "2":
        system('cls')
        login()
        main_menu()
    else:
        print("Yanlış seçim yaptınız...")
        sleep(2)
        main_menu()

def create_student():
    while True:
        print("## Lütfen kayıt bilgilerini doğru girdiğinizden emin olun... ##","\n")
        name = input("Adınız : ".upper())
        surname = input("Soyadınız : ".upper())
        student = name+" "+surname
        studentlist.append(student)
        select = input("Başka bir öğrenci eklemek için 'Ekle', ana memüye dönmek için 'Tamam' yazınız... : ")
        if select == "Ekle" or select == "ekle":
            continue
        elif select == "Tamam" or select == "tamam":
            main_menu()
            break
        else:
            print("Yanlış giriş yaptınız...")
            sleep(2)
            main_menu()

def login():
    system('cls')
    print("### Bilgilerinizi girerken doğru olduğundan emin olun. Doğru giriş için '3' hakkınız bulunmaktadır ###","\n")
    wrong = 3
    while wrong>0:
        name = input("Adınız : ".upper())
        surname = input("Soyadınız : ".upper())
        student = name+" "+surname
        if student in studentlist:
            print("Giriş Başarıyla gerçekleşti. Hoşgeldin {} {}. ".format(name,surname),"\n")
            system('cls')
            main_menu2()
            break
        else:
            wrong-=1
            print("Hatalı giriş yaptınız.")
    else:
        print("3 defa hatalı giriş yaptınız. Giriş işleminiz başarısız oldu. Lürfen daha sonra tekrar deneyin")
        sleep(3)
        system('cls')
        main_menu()

def main_menu2():
    system('cls')
    print("******  Öğrenci Menüsü  ******")
    print("""
       [1] Ders Ekle
       [2] Sınav Notu Gir
       [3] Sınav Notlarını Görüntüle
       """)
    select = input("Lütfen bir işlem seçiniz : ")
    if select == "1":
        system('cls')
        add_lesson()
    elif select == "2":
        system('cls')
        add_exam()
    else:
        print("Yanlış seçim yaptınız...")
        sleep(3)
        main_menu2()


def add_lesson():
    print("Ders Listesi : ")
    for i in range(len(courselist)):
        print(f"{i + 1}. {courselist[i]}")
    lesson_number = int(input("Kaç ders almak istiyorsunuz? : "))
    courselistcount= int(len(courselist))
    if lesson_number > courselistcount:
        print("Yanlış seçim yaptın. Lütfen ders sayısını doğru girin")
        sleep(3)
        add_lesson()
    elif lesson_number < 3 :
        print("Üzgünüm, Sınıfta Kaldın","\n","Bu durumu düzeltmek için öğrenci menüsüne giderek baştan ders eklemen gerekmektedir")
        sleep(3)
        main_menu2()
        system("cls")
    elif lesson_number > 5:
        print("Üzgünüm, {} ders alamazsın. Alınacak ders sayısı 5'i geçmemeli".format(lesson_number),"\n","Bu durumu düzeltmek için öğrenci menüsüne giderek baştan ders eklemen gerekmektedir")
        sleep(3)
        main_menu2()
        system("cls")
    else:
        for i in range(lesson_number):
            lesson = input("{}. Seçtiğiniz Dersin Adı : ".format(i + 1))
            lessons.append(lesson.title())
    print("Eklediğiniz dersleri aşağıda görebilirsiniz...")
    while True:
        for i in range(lesson_number):
            print("{}. {}".format(i + 1,lessons[i]))
        select = input("Öğrenci menüsüne dönmek için '1', Not girmek için '2', ana memüye dönmek için 'Q'ya basınız... : ")
        if select == "1":
            system("cls")
            main_menu2()
        elif select == "2":
            system("cls")
            add_exam()
        elif select == "Q" or select == "q":
            system("cls")
            main_menu()
        else:
            print("Hatalı giriş yaptınız")
            sleep(3)
            main_menu2()



def add_exam():
    if len(lessons)>0:
        for i in range(len(lessons)):
            print("{}. {}".format(i + 1,lessons[i]))
        print("Yukarıda seçmiş olduğunuz dersler bulunmaktadır.")
        select = int(input("Lütfen sınav notunu gireceğiniz dersin numarasını seçin : "))
        mid = int(input("{} dersinden aldığınız vize notunu giriniz: ".format(lessons[select-1])))
        final = int(input("{} dersinden aldığınız final notunu giriniz: ".format(lessons[select-1])))
        project = int(input(("{} dersinden aldığınız proje notunu giriniz: ".format(lessons[select-1]))))
        grade_value = (mid * 0.3) + (final * 0.5) + (project * 0.2)

        if grade_value > 90:
            point = 'AA'
        elif 70 < grade_value < 90:
            point = 'BB'
        elif 50 < grade_value < 70:
            point = 'CC'
        elif 30 < grade_value < 50:
            point = 'DD'
        else:
            point = 'FF'

        examinfo = {str(lessons[select-1]): [mid, final, project, grade_value, str(point)]}


        if point == 'FF':
            print("{} Dersinde başarısız oldun!..".format(lessons[select-1]))
            main_menu2()
        else:
            print("**** {} Dersinin Notları **** ".format(lessons[select-1]))
            print(" Vize Notu :", examinfo[lessons[select-1]][0], "\n", "Final Notu :", examinfo[lessons[select-1]][1], "\n", "Proje Notu :",
                  examinfo[lessons[select-1]][2], "\n")
            print(f"{examinfo[lessons[select-1]][3]} puan ile {examinfo[lessons[select-1]][4]} notunu aldın. Tebrikler...", "\n")
            sleep(5)
            main_menu2()

    else:
        print("Not girişi yapılacak ders bulunamadı. Öncelikle ders eklemeniz gerekmektedir.")
        print("Ders eklemeniz için sizi yönlediriyoruz...")
        sleep(5)
        add_lesson()



main_menu()
