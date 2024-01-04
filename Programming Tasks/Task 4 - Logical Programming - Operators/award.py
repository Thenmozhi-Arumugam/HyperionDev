# This Python program deals with control structures: if, elif, else statements and logical operators: and, or, not

# Get the time taken(in minutes) by the participant to complete the events of a triathlon: swimming, cycling and running
# Using casting function int() as the input given will always be string and time taken(in minutes) is a number

swimming_completion_time = int(input("Please enter the time taken(in minutes) to complete swimming event: "))
cycling_completion_time = int(input("Please enter the time taken(in minutes) to complete cycling event: "))
running_completion_time = int(input("Please enter the time taken(in minutes) to complete running event: "))

# Calculate total time taken for completing all the three events by adding them and displaying the same using print() function
total_time_taken = swimming_completion_time + cycling_completion_time + running_completion_time
print(f"Total time taken(in minutes) to complete all the three events in triathlon is: {total_time_taken}")

""" Determine award for the participant depending on the total time taken to complete all the events 
using if,elif and else statments and logical operator: and"""

if total_time_taken >= 0 and total_time_taken <= 100:
    print("The participant is qualified for Provincial Colours award")
elif total_time_taken >= 101 and total_time_taken <= 105:
    print("The participant is qualified for Provincial Half Colours award")
elif total_time_taken >= 106 and total_time_taken <= 110:
    print("The participant is qualified for Provincial Scroll award")
elif total_time_taken >= 111:
    print("Thank you for participating. You will achieve an award in the next event.")