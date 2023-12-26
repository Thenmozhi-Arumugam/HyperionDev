# This Python program deals with casting operation with string and integer variables

# Get input from user for their favourite restaurant and favourite number

string_fav = input("Enter your favourite restaurant: ")

int_fav = int(input("Enter your favourite number: "))

# Printing out the values given by user using different methods f-strings and concatenation method.
print(f"Your favourite restaurant is {string_fav}")

# In concatenation method, we are using casting function to display integer value as the print statement accepts only string variables
print("Your favourite number is " + str(int_fav))

# Trying to convert string_fav to an integer
conv_string_fav = int(string_fav)

# The above conversion does not work and throw an error as string variable cannot be converted to integer and integer variable would not accept string as its value