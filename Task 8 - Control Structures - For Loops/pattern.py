# This Python program is designed to print out a following pattern using for loop and if - elif statements
store_star = '' # Empty string created for using in later stage

# for loop is used here with i ranging from 1 to 6 (7 is excluded)
# if-elif condition used to check value of i used in for loop
# The '*' is printed in multiples of the value of i and also stored in a string in separate line till the value of i is 5
# Once the value of i reaches 6 the stored string is printed in reverse

for i in range(1,7):
    if i>5:
        print (store_star[::-1].strip())

    else:
        count = i
        print ('*' * count)

# If value of i is 5 the '*' multiples are not stored, to get desired output
        if (i!=5):
            store_star = store_star + '\n' + ('*' * count)