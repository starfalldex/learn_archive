# Exception Handling
# try, except, else, finally

# result = 10 / 0 # ZeroDivisionError: division by zero

a = 10
b = 5
try:
    result = a /b
    print(result)
except:
    print("Error Occured")
print("this will always work")

try:
    result = a / "0"
except Exception as error:
    print("Error:", error)

try:
    result = a / "0"
except TypeError:
    print("1Error: type error")
except ZeroDivisionError as error:
    print("2Error:", error)
except Exception as error:
    print("3Error:", error)
