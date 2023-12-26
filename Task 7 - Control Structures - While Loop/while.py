# This Python program explains using while loop for finding average of numbers entered by user until -1

# Declaring variables with inital values
num = 0
total_sum = 0
count = 0

# while loop checking for condition not equal to -1 and getting input from user
# try and except used to check if valid input is entered by user
while num != -1:
    num = input("Enter a number: ")
    try:
        num = int(num)
        if num != -1:
            total_sum = total_sum + num
            count += 1
    except ValueError:
            print("Invalid input")
            break
# Average calculation of entered numbers by user
# try and except used to check if count of numbers entered is not zero
try:            
    average = total_sum/count
    print("average: " + str(average))
except ZeroDivisionError:
    print("No input entered by user")