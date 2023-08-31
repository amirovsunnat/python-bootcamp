# we will find out whether entered number is odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:   # if number divided by 2 is 0, then do this
    print("It's an even number.")
else:   # otherwise do this
    print("It's an odd number.")


# UZBEKCHASIGA 
son = int(input("Son kiriting: "))
# son toq yoki juftligini if va else bloklaridan foydalanib tekshiramiz
if son % 2 == 0:   # ikkiga bo'lganda qoldiq 0 bo'lsa
    print("Siz kiritgan son - juft.")
else:   # agar qoldiq 0 bo'lmasa
    print("Siz kiritgan son - toq.")