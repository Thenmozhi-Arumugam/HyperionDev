# This Python program deals with control structures: if, elif, else statements

# Get age of the user as input and using casting function - int() converting the data type from string to int
age = int(input("Please enter your age: "))

# Depending on the age received from user, the output is displayed accordingly
if (age > 100):
    print("Sorry, you're dead.")
elif (age >= 65):
    print("Enjoy your retirement!")
elif (age >= 40):
    print("You're over the hill.")
elif (age == 21):
    print("Congrats on your 21st!")
elif (age < 13):
    print("You qualify for the kiddle discount.")
else:
    print("Age is just a number.")