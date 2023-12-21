import pandas
dataFrame = pandas.read_csv("./nato_phonetic_alphabet.csv")
nato_dict = {row["letter"]:row["code"] for (index,row) in dataFrame.iterrows()}
user_input = input("Enter a word : ").upper()
user_output = [nato_dict[letter] for letter in user_input]
print(user_output)
