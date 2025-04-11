#dictionaries
# stores in key valur pairs - {key:value, key:value}
# keys are unique


print("\n-Example 1-")
my_dict = {"Alice": 1, "Bob" : 3, "Charlie" : 4}
print(my_dict) # {'z', 'f', 'b', 'e', 'a'}  


print("\n-Example 2-")
my_dict = {}
my_dict ["Alice"]= 45
my_dict ["Bob"]= 26
my_dict ["Charlie"]= 78
my_dict ["Dog"]= 5
print(my_dict) # {'Alice': 45, 'Bob': 45, 'Charlie': 78, 'Dog': 5}


print("\n-Example 3-")
my_list = ["cat", "mouse", "dog", "bird", "cat"]
my_dict2 = {}
my_dict3 = {}
for i in range (len(my_list)):
    w = my_list [i]
    my_dict2 [i] = w
for i in range (len(my_list)):
    w = my_list [i]
    my_dict3 [w] = i
print(my_dict2) # {0: 'cat', 1: 'mouse', 2: 'dog', 3: 'bird', 4: 'cat'}
print(my_dict3)  # {'cat': 4, 'mouse': 1, 'dog': 2, 'bird': 3}


print("\n-Example 4-")
print(my_dict["Bob"]) # 45
print(len(my_dict)) # 3
print("dog" in my_dict) # False

print("\n-Example 5-")
for key in my_dict:
    value = my_dict[key]
    print(key, value)
print()
for key, value in my_dict.items():
    print(key, value)
# Alice 25
# Bob 57
# Charlie 21
print()


print("\n-Example 6-")
for k in my_dict.keys():
    print(k)
# Alice 
# Bob 
# Charlie 
for v in my_dict.values():
    print(v)
# 25
# 57
# 21
print()

print("\n-Example 7-")
my_key_list = list(my_dict.keys())
my_value_list = list(my_dict.values())
print(my_key_list) # ['Alice', 'Bob', 'Charlie']
print(my_value_list) # [25, 57, 21]


print("\n-Example 8-")
name_list = []
age_list = []
for name in my_dict:
    name_list.append(name)
for name in my_dict:
    age = my_dict[name]
    age_list.append(age)
    # age_list.append(my_dict[name])
print(name_list) # ['Alice', 'Bob', 'Charlie', 'Dog']
print(age_list) # [45, 45, 78, 5]


print("\n-Example 9-")
number_list = [1,2,4,5,3,7,8,3,3,9,6,5,7]
count_dict = {}
for num in number_list:
    if num not in count_dict:
        count_dict[num] = 1
    else:
        count_dict[num] += 1
print(count_dict)

print("\n-Example 10-")
print(my_dict.pop ("Alice"))
print(my_dict)
my_dict["Alice"] =25
print(my_dict.pop ("no", "not found"))
