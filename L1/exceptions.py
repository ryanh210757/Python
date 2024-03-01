class JustNotCoolError(Exception):
    pass

x=2


try:
    raise JustNotCoolError("This isnt cool")
    #raise Exception("Im a custom exception")
    #print(x / 1)
    if not type(x) is str:
        raise TypeError("Only strings are allowed")
except NameError:
    print("NameError means something is probley undefined")
except ZeroDivisionError:
    print("Please dont not divide by zero")
except Exception as error:
    print(error)
else:
    print("no errors!")
finally:
    print("I'm going to print with or without error")