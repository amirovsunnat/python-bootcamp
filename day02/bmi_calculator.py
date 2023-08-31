"""
BMI Calculator. Coding Exercise | Mashq.
Algorithm:
    1. Take user's height -- Foydalanuvchidan bo'yini so'rang
    2. Take user's weight -- Foydalanuvchidan vaznini so'rang
    3. Find the BMI -- BMI ni hisoblang
    4. Convert to integer -- integer qiymatga o'tkazish
    4. Return BMIs -- Foydalanuvchiga BMIni qaytaring
"""

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Finding BMI 👇
BMI = weight / height ** 2 
BMI = int(BMI)
print("Your BMI is: " + str(BMI))
print(f"Your BMI is: {BMI}") 


# UZBEK VERSION
boy = float(input("Bo'yingizni kiriting (metrda): "))
vazn = float(input("Vazningizni kiriting (kg)da: "))

# BMI topish👇
BMI = vazn / boy ** 2 
BMI = int(BMI)
print("Sizning BMIingiz: " + str(BMI))
print(f"Sizning BMIingiz: {BMI}")
