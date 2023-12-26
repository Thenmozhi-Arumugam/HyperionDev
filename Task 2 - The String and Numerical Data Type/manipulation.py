# This Python program deals with string functions such as len(), replace(), slicing method

# Getting a sentence as input from user
str_manip = input("Please enter a sentence: ")
print(f"Length of the given sentence is: {(len(str_manip))}")

# Replace the last letter with @ for every occurrence of last letter in the sentence
last_letter = str_manip[-1]
replace_last = str_manip.replace(last_letter,'@')
print(f"After replacing last letter with '@' in every occurence of that letter in the sentence: {replace_last}")

# Print last three characters in the sentence backwards
last_char_index = len(str_manip)-1
last_three_char = str_manip[last_char_index:last_char_index-3:-1]
print(f"Last three characters in the sentence printed backwards: {last_three_char}")

# Create a word using first three characters and last two characters
first_three_char = str_manip[0:3]
last_two_char = str_manip[last_char_index:last_char_index-2:-1]
print(first_three_char + last_two_char[::-1])