#funtions

# without paramenteres
# def greet ():
#     print ("Hello World")
# greet()


# with paramenteres
# def greet ( name ):
#     print ("Hello "+ name)
# greet("Dex")


# with multiple paramenteres
# def greet ( name ,  age ):
#     print ("Hello "+ name, "\nAge-", age )
# greet("Dex" , 21)


# with return
# def greet ( name ,  age ):
#     age +=100
#     print ("Hello "+ name)
#     return age
# vampire_age = greet("Dex" , 21)
# print("Vampire Age-", vampire_age)


#function with type hints
# def greet (name:str, age: int ) -> int :
#     age +=100
#     print ("Hello "+ name)         #Hello Dex
#     return age
# vampire_age = greet("Dex" , 21)
# print("Vampire Age-", vampire_age) #Vampire Age- 121
# print( type(vampire_age))          #<class 'int'>


# scope - global- can use anyone //// local-  can only be used inside where declared


# default parameters - when no arguments is given then use the default parameters
# def greet(name = "no one?"):
#     print ("Hello " + name)
# greet("Dex") #Hello Dex
# greet()      #Hello no one?
