height = float(input("Enter your height here in m: "))
weight = float(input("Enter your weight here in kg: "))

# Find BMI
BMI = round(weight / height ** 2)
# check some conditions and return result based on comparing
if BMI <18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI<25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI<30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI<35:
    print(f"Your BMI is {BMI}, you are a obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
    

