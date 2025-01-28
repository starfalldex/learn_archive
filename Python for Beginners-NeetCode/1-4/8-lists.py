# list
# list is mutable
# uses 0 based indexing list[index]
# also use negative indexing as -4,-3,-2,-1
# 'in' operator -find an element in list
# 'not in' - opposite of 'in'
# boolvalue - 'element' in 'list'
# some function use with list
# sum,min,max function
# append(variable) - add a element
# pop() -  remove last, pop(index) - remove at index
# index(element) - first occurance of element in 0 indexing
# list slicing as same as strings

# tuples are same as list 
#  tuple are immutable

print("\n-Example 1-")
my_list = [1,8,9,4,6,5,6]
for i in my_list:
    print(i, end="-")
print()


print("\n-Example 2-")
my_list = [1,8,9,4,6,5,6]
if 1 in my_list: 
    print("yeah")
else :
    print("nah")


print("\n-Example 3-")
my_list = [1,8,9,4,6,5,6]
print(sum(my_list))
print(min(my_list))
print(max(my_list))


print("\n-Example 4-")
my_list = [1,8,9,4,6,5,6]
number = 7
my_list.append(number)
print(my_list)


print("\n-Example 5-")
my_list = [1,8,9,4,6,5,6]
number = 4
print(my_list.index(number))


print("\n-Example 6-")
my_tuple = (1,8,9,4,6,5,6)
number = 9
print(my_tuple)
print(my_tuple.index(number))