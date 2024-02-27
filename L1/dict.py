band = {
    "vocals": "Plant", 
    "guitar": "Rocker"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access the items
print(band["vocals"])
print(band.get("guitar"))
#Print keys and values
print(band.keys())
print(band.values())
#Returns boolean
print("guitar" in band)
#updates band
band["vocals"] = "BANG"
print("Plant" in band)

#remove items
print(band.pop("vocals"))
print(band)


band["drums"] = "Barker"
print(band)


band["mykey"] = "Delete"
print(band)
del band["mykey"]
print(band)


#copy a dictionary
band3 = band.copy()
band3["heaven"] = "Seven"
print(band3)


#NESTED Dictionary
member1 = {
    "name": "YEP",
    "instrument": "guitar"
}
member2 = {
    "name": "NOPE",
    "instrument": "drums"
}
band4 = {
    "member1": member1,
    "member2": member2
}
print(band4)
print(band4["member1"]["name"])

#SETS
nums = {1, 2, 3, 4, 5}
nums2= set((1,2,3,4))
print(type(nums2))


#NO DUPLICATES ALLOWE
nums4 = {2, 2 ,4, 5}

print(nums4)

#Add new element to set
nums4.add(8)
print(nums4)

morenums = {3, 29, 9}
nums4.update(morenums)
print(nums4)

#Merge two sets to create a new set
one = {1, 2, 3}
two = {4, 6, 7}

mynewset = one.union(two)
print(mynewset)

#Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 7}

one.intersection_update(two)
print(one)

#keep everything but the duplicates
one={1,2,3}
two={2,3,7}

one.symmetric_difference_update(two)
print(one)
