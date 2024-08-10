import random
# numbers = [1, 2, 3, 4]

# modified_numbers = [number+1 for number in numbers]
# print(modified_numbers)

# name = "Prithwish"

# modified_name = [item for item in name]
# print(modified_name)

# ranged_number = [item * 2 for item in range(1, 5)]
# print(ranged_number)

# # conditional list comprehension
# names = ["John", "Emma", "Liam", "Mia", "Noah", "Olivia", "James", "Grace", "Ethan", "Sarah"]

# short_names = [name for name in names if len(name) <= 5]
# long_names = [name.upper() for name in names if len(name) > 5]

# print(short_names)
# print(long_names)

# Dictionary Comprehension

# sample_dict = {
#     "fruit": "apple",
#     "color": "blue",
#     "animal": "dog",
#     "city": "Paris",
#     "car": "Tesla",
#     "country": "Japan",
#     "language": "Python",
#     "book": "1984",
#     "movie": "Inception",
#     "drink": "coffee"
# }

# new_dict = { value: key for (key, value) in sample_dict.items()}

# print(new_dict)

# name_dict = {name: random.randint(0, 100) for name in names}

# print(name_dict)

# pass_student = {name: marks for (name, marks) in name_dict.items() if marks >= 34}

# print(pass_student)

student_dict = {
    "students": ["Abir", "Raj", "Biraj"],
    "score": [88, 56, 84]
}


# for (key, value) in student_dict.items():
#     print(key)

import pandas

student_data_fame = pandas.DataFrame(student_dict)
# print(student_data_fame)

# Loop through the data frame
for (index, row) in student_data_fame.iterrows():
    if row.students == 'Abir':
        print(row.score)



