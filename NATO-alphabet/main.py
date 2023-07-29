import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    # Access key and value
    pass

student_data_frame = pd.DataFrame(student_dict)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # Access index and row
    # Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

csv_data = pd.read_csv('nato_phonetic_alphabet.csv')

nato_alphabet = {row.letter: row.code for (index, row) in csv_data.iterrows()}
print(nato_alphabet)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("enter your name : ")

# values = [nato_alphabet.get(letter) for letter in name if letter in nato_alphabet]

# print(values)

for letter in name:
    if letter in nato_alphabet:
        print(nato_alphabet[letter])
