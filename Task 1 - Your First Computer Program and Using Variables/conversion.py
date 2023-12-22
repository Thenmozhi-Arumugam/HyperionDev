#This program tells us on how to declare variables with values (which determine data type) and converting them into another data type using casting function.
"""
Pseudo code for the Python code:
declare variables as follows
  num1 = 99.23
  num2 = 23
  num3 = 150
  string1 = "100"
print the values of variables before converting them to required data types
print the variables in required format using casting function
"""
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"
print("Values of variables before converting to required data types:")
print(f"num1 : {num1}")
print(f"num2 : {num2}")
print(f"num3 : {num3}")
print(f"string1 : {string1}")
num1_int = int(num1)
num2_float = float(num2)
num3_str = str(num3)
string1_int = int(string1)
print("Values of variables after conversion:")
print(f"num1 converted to integer: {num1_int}")
print(f"num2 converted to float: {num2_float}")
print(f"num3 converted to string: {num3_str}")
print(f"string1 converted to integer: {string1_int}")
