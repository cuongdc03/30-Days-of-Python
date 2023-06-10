# letter = "P"  # A string could be a single character or a bunch of texts
# print(letter)  # P
# print(len(letter))  # 1
# greeting = "Hello, World!"  # String could be made using a single or double quote,"Hello, World!"
# print(greeting)  # Hello, World!
# print(len(greeting))  # 13
# sentence = "I hope you are enjoying 30 days of Python Challenge"
# # print(sentence)

# multiline_string = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string)

# # Another way of doing the same thing
# multiline_string = """I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python."""
# print(multiline_string)

# first_name = "Asabeneh"
# last_name = "Yetayeh"
# space = " "
# full_name = first_name + space + last_name
# print(full_name)  # Asabeneh Yetayeh
# # Checking the length of a string using len() built-in function
# print(len(first_name))  # 8
# print(len(last_name))  # 7
# print(len(first_name) > len(last_name))  # True
# print(len(full_name))  # 16
# print("I hope everyone is enjoying the Python Challenge.\nAre you ?")  # line break
# print("Days\tTopics\tExercises")  # adding tab space or 4 spaces
# print("Day 1\t3\t5")
# print("Day 2\t3\t5")
# print("Day 3\t3\t5")
# print("Day 4\t3\t5")
# print("This is a backslash  symbol (\\)")  # To write a backslash
# print(
#     'In every programming language it starts with "Hello, World!"'
# )  # to write a double quote inside a single quote

# # output
# I hope every one is enjoying the Python Challenge.
# Are you ?
# Days	Topics	Exercises
# Day 1	5	    5
# Day 2	6	    20
# Day 3	5	    23
# Day 4	1	    35
# This is a backslash  symbol (\)
# In every programming language it starts with "Hello, World!"
# Strings only
first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "I am %s %s. I teach %s" % (first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius**2
formated_string = "The area of circle with a radius %d is %.2f." % (
    radius,
    area,
)  # 2 refers the 2 significant digits after the point
print(formated_string)
python_libraries = ["Django", "Flask", "NumPy", "Matplotlib", "Pandas"]
formated_string = "The following are python libraries:%s" % (python_libraries)
print(
    formated_string
)  # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
