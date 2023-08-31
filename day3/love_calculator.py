print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_name = (name1 + name2).lower()

t_occurs = combined_name.count("t")
r_occurs = combined_name.count("r")
u_occurs = combined_name.count("u")
e_occurs = combined_name.count("e")
true_ = t_occurs + r_occurs + u_occurs + e_occurs

l_occurs = combined_name.count("l")
o_occurs = combined_name.count("o")
v_occurs = combined_name.count("v")
e_occurs = combined_name.count("e")
love = l_occurs + o_occurs + v_occurs + e_occurs

score = int(str(true_) + str(love))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif 40<score<50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")