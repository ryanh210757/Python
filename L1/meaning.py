#command + / to comment out all

meaning = 40
catchphrase = "Hi I'm "
name = "Dave"

print(type(meaning))
print(isinstance(meaning, str))

#print("hell yea brother") if meaning > 10 else print('nope')


#CONSTRUCTOR FUNCTION
pizza = str("Pepperoni")
print(type(pizza))


#print(catchphrase + name)


#escaping special characters
sentence = 'I\' the mutha\'fuckn truth\t\n\n ya heard me\\hoe'
print(sentence)

#String Methods
print(name)
print(name.lower())
print(name.upper())
print(name.title())
print(sentence.replace("truth", "TRUTH"))
print(len(sentence))
print(len(name))

#Printing a Menu
print("MENU".center(20, "-"))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Dougnuts".ljust(16, ".") + "5".rjust(4))
print("Tea".ljust(16, ".") + "$2".rjust(4))

print("")

test = "this is a test"

print(test[0:-1])
print(test[4:])
print(test[-1])

price = 100
gpa = 3.2
print(price)
print(isinstance(price, int))

import math 

print(math.pi)
print(math.sqrt(64))
print(math.ceil(2.4))


zipcode = "60615"
zip = int(zipcode)
print(type(zip))