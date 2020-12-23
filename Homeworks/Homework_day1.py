employe = list()
print("Lütfen Adınız ve Soyadınızı Giriniz")

name = input("Adınız : ").upper()
surname = input("Soyadınız : ").upper()

print(f'Hoş geldin {name} {surname}', "\n" "Lütfen sizden istenen  bilgileri doğru girdiğinizden emin olun")

print()
bdate = input("Doğum Tarihiniz (gg.aa.yyyy): ").upper()
bplace = input("Doğum Yeriniz :").upper()
height = float(input("Boyunuz :"))
weight = float(input("Kilonuz :"))
adress = input("Adresiniz  :").upper()
zicode = int(input("Posta Kodunuz :"))

info = (name,surname,bdate,bplace,height,weight,adress,zicode)

employe.append(info)

print()
print("{} {} isimli çalışan {} yılında {} 'da doğmuştur. Boyu ve kilosu {} // {}. Adresi: {}  Pk: {}".format(info[0],info[1],info[2],info[3],info[4],info[5],info[6],info[7]))

print()
print("kullanmış olduğunuz type değerleri sırasıyla aşağıda yer almaktadır")
print(" employe type : ", type(employe), "\n","info type :", type(info), "\n","name type :", type(name), "\n","surname type :", type(surname), "\n","bdate type :", type(bdate), "\n","bplace type :", type(bplace), "\n","height type :", type(height), "\n","weight type :", type(weight), "\n","adress type :", type(adress), "\n","zicode type :", type(zicode))







