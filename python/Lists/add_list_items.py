# Append Items
myarr = ["apple", "banana", "cherry"]
myarr.append("orange")  # Append "orange" to the end of the list
print(myarr)

#Insert Items
myarr1 = ["apple", "banana", "cherry"]
myarr1.insert(2, "orange")  # Insert "orange" at index 2
print(myarr1)

# Extend List
myarr2 = ["Python", "C++", "Java"]
myarrupdate2 = ['Html','Css','JavaScript']
myarr2.extend(myarrupdate2)  # Extend the list by adding the elements of another list
print(myarr2)

# Add Any Iterable
myarrlist = ["apple", "banana", "cherry"]
myarrlist1 = ("orange", "mango")
myarrlist.extend(myarrlist1)
print(myarrlist)

