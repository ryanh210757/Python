# r = Read
# a = Append
# w = Write
# x = Create

import os
#Read - error if it doesnt exist
f = open("names.txt")
# print(f.read())
# print(f.read(4))
#print(f.readline())
#print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f=open("names.txt")
    print(f.read())
except:
    print("The file you want to read does mot exist")
finally:
    f.close()


f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

#Write (overwrite)
f = open("context.txt", "w")
f.write("I deleted all the content")
f.close()

f = open("context.txt")
print(f.read())
f.close()

#opens file for writing, creates the file if it doesnt exists
f = open("name_list.txt", "w")
f.close()


#creates specified file but returns error if file exists
if not os.path.exists("ryan.txt"):
    f = open("ryan.txt", "x")
    f.close()

#delete file

#avoid an error if it doesnt exist
if os.path.exists("ryan.txt"):
    os.remove("ryan.txt")
else:
    print("file that you wish to delete does not exist.")



with open("more_names.txt") as f:
    content = f.read()
with open("names.txt", "w") as f:
    f.write(content)