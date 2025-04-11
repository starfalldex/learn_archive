# string
# string is immutable
# python use 0 based indexing 
# ex-'string':(index-character):'0-s', '1-t' ... '4-n', '5-g'
# also use negative indexing as -4,-3,-2,-1


print("-Example 1-")
# direct print characters
for i in "string":
    print(i , end= "-")
print()


print("\n-Example 2-")
# len(str) - find string length
str1 = "hello world"
print (len(str1))


print("\n-Example 3-")
def longer_word(string1: str,string2: str) -> str:
    if len(string1) >= len(string2): 
        return string1
    return string2
print("the longer word is -",longer_word("word1", "string2"))


print("\n-Example 4-")
# concatination of string
str1= "hello"
str2= "world"
str3 =  str1 + str2
print(str3)


# string slicing 
# string[start:end]
# string[start:end:order]
# string[start:end:2]
# string[start:end:-1] reverseorder


print("\n-Example 5-")
# string formatting
name = "dex"
age = 23
msg = "hi {} you are {} years old".format(name, age)
print(msg)
print("hi {1} you are {0} years old".format(name, age))
# f-string
print ( f"hi {name} you are {age} years old")
