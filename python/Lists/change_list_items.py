# Change Item Value
thislist = ["Python", "Java", "C++", "JavaScript", "Ruby"]
thislist[1] = "Html"
print(thislist)

# Change a Range of Item Values
mylist = ["Python", "Java", "C++", "JavaScript", "Ruby"]
mylist[1:3] = ["Html", "CSS"]
print(mylist)

# Change the second value by replacing it with two new values:
mylist1 = ["apple",'bannana','cherry']
mylist1[1:2] = ["watermelon", "mango"]
print(mylist1)

# Change the second and third value by replacing it with one value:
mylist2 = ["apple",'bannana','cherry']
mylist2[1:3] = ["watermelon"]
print(mylist2)

# Insert Items
mylist3 = ["apple", "banana", "cherry"]
mylist3.insert(2, "orange")  # Insert "orange" at index 2
print(mylist3)