#tuple and set

# genders=("male","female","others",(1,2,3))
# print(genders)
# print(genders)
# print(len(genders))
# print(genders[0])
# print(genders[1:3])

#stackoverflow website

# tuple1=(1,2,3)
# tuple2=(4,5,6)
# combined_tuple=tuple1+tuple2
# print(combined_tuple)


# repeated_tuple=(1,2)*3
# print(repeated_tuple)

# print(genders.count("male"))
# print(genders.index("male"))

#tuple operation amd methods


#set

# s={10,2,3}  #set is unordered
# print(s)
# s2=set((1,2,3))
# print(s2)

# empty_set=set()
# print(empty_set)

# s1={1,2,3}
# s2={3,4,5}
# print(s1 | s2)  #union
# print(s1 & s2)  #inersection
# print(s1 - s2)  #difference
# print(s2 -s1)   #difference
# print(s1 ^ s2)   #symmetric difference


s={1,2,3}
print(s.add(4))
print(s)
print(s.discard(10))
print(s.pop())
print(s.clear())