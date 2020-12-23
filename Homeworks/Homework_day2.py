import datetime

userlist = []
now = datetime.datetime.now()
now = int(now.year)

while True:
    print(''' 
    [1] Enter user information
    [2] Can I go out
    [3] Show all user information
    ''')
    select = input("Please select option : ")

    while True:
        if select == '1':  # user kaydının yapıldığı alan
            print("Please enter the correct information")
            name = input("Firs Name : ")
            surname = input("Last Name : ")
            age = int(input("Age: "))
            birth_year = int(input("Date of birth (just year) : "))
            user_info = (name, surname, age, birth_year)
            userlist.append(user_info)  # user bilgilerini user listesine atar
            input("Please press 'Enter' to return to main menu ...")
            break
        elif select == '2':  # user yaş sorgulama alanı
            if len(userlist) >= 1:  # listenin boş olma durumu var. Bu sebeple kontrol eklendi
                i_name = input("Please enter your name : ")
                i_surname = input("Please enter your last name : ")

                if i_name in userlist and i_surname  in userlist: #kullancının bilgileriyle giriş sağlanıyor
                    if age >= 18 and now - birth_year > 18:
                        print("You can go out the street.")
                        input("Please press 'Enter' to return to main menu ...")
                        break
                    elif age < 18 and now - birth_year < 18:
                        print("You can't go out becaouse it's too dangerous.")
                        input("Please press 'Enter' to return to main menu ...")
                        break
                    else:
                        print("Please check your information.")
                        input("Please press 'Enter' to return to main menu ...")
                        break
                else:
                    print("Your name is not in system. Please check your information.")
                    input("Please press 'Enter' to return to main menu ...")
                    break
            else:
                print("System doesn't have any user information. Please enter your information firstly.")
                input("Please press 'Enter' to return to main menu ...")
                break
        elif select == '3':
            if len(userlist) > 0:  # listenin boş olma durumu var. Bu sebeple kontrol eklendi
                for i in userlist:
                    print("*************************")
                    print(f' User Name Surname: {i[0]} {i[1]}'.upper(), "\n", f'Age (Birth_Year) : {i[2]} ({i[3]})')
                    input("Please press 'Enter' to return to main menu ...")
                    break
            else:
                print("System doesn't have any user information. Please enter your information firstly.")
                input("Please press 'Enter' to return to main menu ...")
                break

        else:
            print("Please check your information.")
            input("Please press 'Enter' to return to main menu ...")
            break