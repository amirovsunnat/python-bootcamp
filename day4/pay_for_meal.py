import random
# foydalanuvchidan ismlarni olib ularni ro'yxat ko'rinishida saqlaydi
names = input("Bazimda kimlar qatnashdi? (Behruz, Bobur, Hilola): ").split(", ")
# tasodiy ismni tanlaymiz choice funksiyasi orqali
random_name = random.choice(names)
print(f"Bugungi hisobni {random_name} to'laydi.")
