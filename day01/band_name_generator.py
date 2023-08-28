"""
ALGORITHM
    1. Greeting.
    2. Take city name
    3. Take pet name
    4. Combine two inputs and create band name
    5. Return band name

Uzbek tilida:
    1. Salomlashish
    2. Shahar nomini olish
    3. Pet(uy hayvoni) nomini olish
    4. Olingan inputlardan foydalanib guruh nomini yaratish
    5. Foydalanuvchiga guruh nomini qaytarish
"""


print("Welcome to band name generator!")
city = input("What city did you grow up in?\n")
pet_name = input("What's your pet's name?\n")
band_name = city + " " + pet_name
print("Your band name could be: " + band_name)


# UZBEK

print("Band Nomi Generatori'ga xush kelibsiz!")
shahar = input("Qaysi shaharda o'sgansiz?\n")
jonivor = input("Uy-hayvoningiz nomi nima?\n")
guruh_nomi = shahar + " " + jonivor
print("Sizning guruh nomingiz quyidagicha mumkin:  " + guruh_nomi)
