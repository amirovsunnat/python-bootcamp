line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input()
letters = ["a", "b", "c"]
letter = position[0].lower()
number = int(position[1]) - 1
letter_index = letter.index(letter)
map[number][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")