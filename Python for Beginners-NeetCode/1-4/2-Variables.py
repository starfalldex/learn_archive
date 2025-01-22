#variable in python
m = "this is a string variable"
print (m)
print (m+ " another way to add temp string?")

#naming convention in python
print("python use snake_case naming convetion which_uses_underscore_between_words")

#we can use the assignment in python like this
msg1, msg2 = "hello", "world"

#or we can swap very easy
msg1, msg2 =  msg2 , msg1 # world , hello

#integer, floating point numbers, boolean, string
age = 21 
temperature = 21.34345 
is_true = True 
name = "Dex"

#list - sequence of integer
lst1 = [1,2,3]

#type of funtion 
print(type(10)) #or type(variable)

#this is okay is python
#avoid if you can
variable = 10  #integer
print(type(variable))
variable = "name" #string
print(type(variable))
variable = [1,2,3] #list
print(type(variable))

#typecasting
variable1  = 10.9 #float
print(int(variable1)) 

# this dont work
# name = "dex"
# name = int(name) #like this

# but this work -  if string have numbers
age1 = "10" #<class 'str'> 
age1 = int (age1) # <class 'int'>

# intead of 'null' python has 'none' - <class 'NoneType'>
