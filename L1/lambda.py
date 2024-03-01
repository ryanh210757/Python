square = lambda num : num * num
print(square(2))

addTwo = lambda num : num + 2

print(addTwo(4))

sum_total = lambda a, b: a + b
print(sum_total(5,4))


new_lamb = lambda a,b : a * b + 3
print(new_lamb(2, 21))



####higher order func
def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(5))


###

lambda num : num * num
numbers = [3, 78, 12, 81, 20]

squarednums = map(lambda num : num * num, numbers)
print(list(squarednums))


####
lambda num : num % 2 != 0
oddnums = filter(lambda num : num % 2 != 0, numbers)
print(list(oddnums))


###
from functools import reduce

lambda acc, curr : acc + curr
numberss = [1, 2, 3, 4, 5, 1]
total = reduce(lambda acc, curr : acc + curr, numberss, 10)
print(total)
print(sum(numberss))



lambda acc, curr : acc + len(curr)
names = ["John Jaacob", "yah Yha ", "yerpr"]
char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)
print(char_count)