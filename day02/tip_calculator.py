# Print a welcome message
print("Welcome to the tip calculator!")

# Get the total bill amount from the user
bill = float(input("What was the total bill? $"))

# Get the desired tip percentage from the user
tip_percentage = int(input("What percentage tip would you like to give? (10, 12, or 15): "))

# Get the number of people to split the bill among
total_people = int(input("How many people will split the bill? "))

# Calculate the bill with tip
tip_amount = bill * tip_percentage / 100
total_bill = bill + tip_amount

# Calculate the amount each person should pay
each_person_bill = round(total_bill / total_people, 2)  # Rounded to 2 decimal places

# Display the amount each person should pay
print(f"Each person should pay: ${each_person_bill}")


# ------------------------------------UZBEK VERSION-------------------------------------------------------

# Salomlashish
print("Tip kalkulyatoriga xush kelibsiz!")

# Foydalanuvchidan umumiy hisobni so'rang
hisob = float(input("Umumiy hisob qancha edi? $"))

# Foydalanuvchidan istalgan baholash foizi ni so'rang
foiz = int(input("Siz qaysi baholash foizini berishni istaysiz? (10, 12, yoki 15): "))

# Qancha kishi hisobni bo'lmoqchi
odamlar_soni = int(input("Hisobni qancha kishiga bo'lishi kerak? "))

# Baholash bilan hisoblash
foiz_miqdori = hisob * foiz / 100
umumiy_hisob = hisob + foiz_miqdori

# Har bir kishiga to'lov qilishi kerak bo'lgan miqdorni hisoblash
har_bir_kishiga = round(umumiy_hisob / odamlar_soni, 2)  # 2 xonagacha yaxlitlash verguldan keyin

# Har bir kishining to'lov miqdorini chiqarish
print(f"Har bir kishi to'lovi: ${har_bir_kishiga}")