names = []
with open("Input/Names/invited_names.txt") as file:
    names_n = file.readlines()
    for n in names_n:
        names.append(n.strip())

with open("Input/Letters/starting_letter.txt") as file:
    starting_letter = file.read()

for i in range(len(names)):
    with open(f"Output/ReadyToSend/letter_for_{names[i]}.txt", mode="w") as file:
        file.write(starting_letter.replace("[name]", names[i]))

