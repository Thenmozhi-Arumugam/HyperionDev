# This Python code deals with multiple string oprations such as replace, upper and reverse
# Given sentence as a single string
original_string = "The!quick!brown!fox!jumps!over!the!lazy!dog."

# With replace() function, '!' (exclamatory mark) present in the original sentence is replaced with spaces
replace_string = original_string.replace('!',' ')
print(replace_string)

# Using upper() funtion to display replaced sentence in Upper case
print(replace_string.upper())

# Using slicing method, displaying the replaced sentence in reverse order
print(replace_string[::-1])