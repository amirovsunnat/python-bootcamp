import random

tanlovlar = [
# Quduq
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

foydalanuvchi_tanlovi = int(input("Siz nimani tanlaysiz? Quduq uchun 0, Qog'oz uchun 1, Qaychi uchun 2 ni tanlang.\n>>> "))
if foydalanuvchi_tanlovi >= 3 or foydalanuvchi_tanlovi < 0:
    print("Siz noto'g'ri raqamni kiritdingiz.")
else:
    print(tanlovlar[foydalanuvchi_tanlovi])
    print("Computer tanladi: ")
    kompyuter_tanlovi = random.randint(0, 2)
    print(tanlovlar[kompyuter_tanlovi])

    if foydalanuvchi_tanlovi == 0 and kompyuter_tanlovi == 2:
        print("Siz g'alaba qozondingiz.")
    elif kompyuter_tanlovi == 0 and foydalanuvchi_tanlovi == 2:
        print("Kompyuter yutdi.")
    elif kompyuter_tanlovi > foydalanuvchi_tanlovi:
        print("Kompyuter yutdi.")
    elif foydalanuvchi_tanlovi > kompyuter_tanlovi:
        print("Siz g'alaba qozondingiz.")
    elif kompyuter_tanlovi == foydalanuvchi_tanlovi:
        print("Durrang!")

