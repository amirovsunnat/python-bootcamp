"""
Life in weeks. Coding exercise. | Inson hayotida qancha hafta qolganini aytib beruvchi mashq.
Albatta bunda nisbiy olingan.
Algorithm -- Algoritm:
    1. Take user's age -- Foydalanuvchi yoshini oling
    2. Calculate how many years left (Take 100 years as a default age)-- Qancha yil qolganini hisoblang (100 yoshni nisbiy shaklda oling).
    3. Calculate how many months left -- Qancha oy qolganini hisoblang. 
    4. Calculate how many weeks left -- Qancha hafta qolganini hisoblang.
    5. Calculate how many days left -- Qancha kun qolganini hisoblang.
    6. Combine these and return it as a message to user -- Hammasini jamlab foydalanuvchiga xabar shaklida qaytaring. 
"""

# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remaining_years = 100 - age
remaining_months = remaining_years * 12
remaining_weeks = remaining_years * 52
remaining_days = remaining_years * 365
message = f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left."
print(message)


# UZBEK VERSION
yosh = int(input("Yoshingiz nechchida? "))

#Write your code below this line 👇
qolgan_yil = 100 - yosh
qolgan_oy = qolgan_yil * 12
qolgan_hafta = qolgan_yil * 52
qolgan_kun = qolgan_yil * 365
xabar = f"Sizda {qolgan_kun} kun, {qolgan_hafta} hafta va {qolgan_oy} oy qoldi"
print(xabar)