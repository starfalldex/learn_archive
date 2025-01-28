# sets
# ordered collection of unique elements
# can convert list to set

print("\n-Example 1-")
my_set = {'a' , 'b', 'e' , 'z', 'f'}
print(my_set) #{'z', 'f', 'b', 'e', 'a'}  

print("\n-Example 2-")
my_set = {100, 5, 200, 1, 75, 50, 25}
print(my_set) #{1, 50, 100, 5, 200, 25, 75} 

print("\n-Example 3-")
my_set = set() #empty set
my_set.add(1)
my_set.add(40)
my_set.add(5)
my_set.add(70)
print(my_set) #{40, 1, 5, 70}

print("\n-Example 4-")
my_set = set() #empty set
my_set.add(1)
my_set.add(40)
my_set.add(5)
my_set.add(70)
my_set.remove(40) #remove based on value
my_set.remove(5)
print(my_set) #4{1, 70}

print("\n-Example 5-")
my_set = {"cat", "mouse", "dog", "bird"}
contains_dog = "dog" in my_set
contains_lion = "lion" in my_set
print(contains_dog) #True
print(contains_lion) #False

print("\n-Example 5-")
my_list = ["world", "hello", "world", "hello", "dex" ,"how"]
unique_words =set(my_list)
count = 0
for w in unique_words:
    count+=1
print(count) #4
print(len(unique_words)) #4