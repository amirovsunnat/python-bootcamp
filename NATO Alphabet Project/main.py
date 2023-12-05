import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = {row.letter: row.code for index, row in data.iterrows()}
user_word = input("Enter a word: ").strip().upper()
new_nato_words = [data_dic[letter] for letter in user_word if letter in data_dic]

print(new_nato_words)
