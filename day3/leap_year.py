# we are going to find out whether entered year is leap year or not.
year = int(input("Which year do you want to check? "))
# check if it is leap year
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")



# UZBEK VERSION
yil = int(input("Tekshirmoqchi bo'lgan yilingizni kiriting: "))
if yil % 4 == 0:
    if yil % 100 == 0:
        if yil % 400 == 0:
            print("Kabisa yili.")
        else:
            print("Kabisa yili emas.")
    else:
        print("Kabisa yili.")
else:
    print("Kabisa yili emas.")