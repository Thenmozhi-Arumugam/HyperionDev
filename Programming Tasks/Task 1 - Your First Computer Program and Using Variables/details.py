"""
This program tells us on how to get several inputs from user and print it as one sentence
Pseudo code for the Python code:
request name of the user as input
store input from user in variable called "name"
request age of the user as second input
store input from user in variable called "age"
request house number of the user as third input
store input from user in variable called "house_no"
request street name of the user as fourth input
store input from user in variable called "street_name"
Using concatenation (+) function display the required desired sentence with received inputs from user
"""
name = input("Enter your name: ")
age = input("Enter your age: ")
house_no = input("Enter your House number: ")
street_name = input("Enter your Street name: ")
print("This is " + name + ". He is " + age + " years old and lives at house number " + house_no + " on " + street_name + " Street.")