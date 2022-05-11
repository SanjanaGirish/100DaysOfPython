# List Comprehension
# new_list = [new_item for item in list]
# Conditional List Comprehension
# new_list = [new_item for item in list if test]

# Dictionary Comprehension
# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# Conditional Dictionary Comprehension
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
# student_scores = {student: random.randint(1, 100) for student in names}
# passed_students = {student: scores for (student, scores) in
# student_scores.items() if scores > 50}

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# NATO ALPHABET PROJECT
import pandas
# Create a dictionary from the CSV file:
data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# A list of the phonetic code words from a word that the user inputs.
valid_input = False
while valid_input == False:
    word = input("Enter a word: ").upper()
    try:
        output_lst = [f'{letter}: {phonetic_dict[letter]}' for letter in word]
        print(output_lst)
        valid_input = True
    except KeyError:
        print("Sorry, only letters in the alphabet please")

