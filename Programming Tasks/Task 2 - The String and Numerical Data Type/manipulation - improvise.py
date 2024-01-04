# This Python program deals with string functions such as len(), replace(), slicing method

# Getting a sentence as input from user
str_manip = input("Please enter a sentence: ")
print(f"Length of the given sentence is: {(len(str_manip))}")

# Check if the given input is empty
if len(str_manip) == 0:
    print("The input is empty")

else:
    # Replace the last letter with @ for every occurrence of last letter in the sentence
    last_letter = str_manip[-1]
    replace_last = str_manip.replace(last_letter,'@')
    print(f"After replacing last letter with '@' in every occurence of that letter in the sentence: {replace_last}")
    
# Checking for the length of sentence for certain string operations to be performed
    if len(str_manip) == 3:
        # Print last three characters in the sentence backwards
        last_three_char = str_manip[::-1]
        print(f"Last three characters in the sentence printed backwards: {last_three_char}")

    elif len(str_manip) > 3:
        # Print last three characters in the sentence backwards
        last_char_index = len(str_manip)-1
        last_three_char = str_manip[last_char_index:last_char_index-3:-1]
        print(f"Last three characters in the sentence printed backwards: {last_three_char}")

        if len(str_manip) > 4:
            # Create a word using first three characters and last two characters
            first_three_char = str_manip[0:3]
            last_two_char = str_manip[last_char_index:last_char_index-2:-1]
            print(f"New word formed from given sentence: {first_three_char + last_two_char[::-1]}")

        else:
            print("String operation for formation of five letter word require the length of string to be greater than 4")

    else:
        print("String operations such as printing last three characters in backwards and formation of five letter word require the length of string to be atleast 3 or greater than 4 respectively")
