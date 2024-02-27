my_list = ['dave', 32, False]
print("Dave" in my_list)
print(my_list[0])
print(my_list[-2])
print(my_list.index('dave'))
print(my_list[0:2])
print(my_list[::-1])
print(len(my_list))
my_list.append("OR")
print(my_list)

my_list += ["jason"]
print(my_list)

my_list.insert(0, "Dave")
print(my_list)

my_list[2:2] = ['Eddie', 'Alex']
print(my_list)

my_list[1:3] = ["EDDIE", "BYE DAVE"]
print(my_list)

my_list.remove(32)

my_list.remove(False)
print(my_list)

my_list.sort()
print(my_list)

nums = [4, 412, 0, 20]
nums.sort()
print(nums)
print(sorted(nums, reverse=True))



my_tup = tuple((1, 3, 4, 3))
print(type(tuple))

newlist = list(my_tup)
newlist.append(10)
new_tup = tuple(newlist)
print(my_tup)
print(new_tup)