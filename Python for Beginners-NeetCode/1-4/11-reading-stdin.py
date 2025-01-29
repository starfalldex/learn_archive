# reading standard input
# type conversions

print("\n-Example 1-")
user_input_name = input ("Enter your name:")
user_input_age = int(input ("Enter your age: "))
print("Hello, " + user_input_name + "!")
print("your age is:", user_input_age, "and its of <int> data type")

number_string = "1,2,3"
string_list = number_string.split(",")
print(string_list)

line = input("Enter list of string")
list_of_strings= line.split(",")
list_of_int = []

for str in list_of_strings:
    list_of_int.append(int(str))

print(list_of_strings) # list of string numbers
print(list_of_int) # list of int numbers

