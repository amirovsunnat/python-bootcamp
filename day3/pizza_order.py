print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# create new variable for keep track of cost
cost = 0
#Write your code below this line 👇
# checking size and calculating
if size == "S":
    cost += 15
elif size == "M":
    cost += 20
elif size == "L":
    cost += 25

# checking pepperoni selection and calculating
if add_pepperoni == "Y":
    if size == "S":
        cost += 2
    else:
        cost += 3

# checking extra_cheese is needed and calculating
if extra_cheese == "Y":
    cost += 1
print(f"Your final bill is: ${cost}.")


# --------------------------------------UZBEK VERSION-----------------------------
print("Python pitsa yetkazish dasturimizga xush kelibsiz!")
olcham = input("Qanaqa o'lchamdagi pitsani xohlaysiz? Kichik (K), O'rtacha(O), Katta(K): ")
qalampir_qoshilsin = input("Qalampir qo'shilsinmi? Ha(H) yoki Yo'q(Y)")
qoshimcha_pishloq = input("Qo'shimcha pishloq xohlaysizmi? Ha(H) yoki Yo'q(Y)")

# o'zgaruvchi yaratib olamiz narxni hisoblash uchun
narx = 0

# endi esa olchamni tekshiramiz va shunga qarab narx qo'shamiz
if olcham == "K":
    narx += 15
elif olcham == "O":
    narx += 20
else:
    narx += 25

# qalampir kerakmi yoki yo'q tekshiramiz va agar kerak bo'lsa narxni o'zgartiramiz
if qalampir_qoshilsin == "H":
    if olcham == "K":
        narx += 2  # kichkina pitsa uchun
    else:
        narx += 3  # o'rtacha va katta pitsalar uchun

# pishloq ham kerakmi tekshiramiz
if qoshimcha_pishloq == "H":
    narx += 1   # hamma pitsalar uchun $1

print(f"Sizning oxirgi to'lovingiz: ${narx} bo'ldi.")