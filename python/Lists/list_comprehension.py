# List Comprehension
mycomlist = ['python', 'java', 'c++', 'javascript']
newlist = []
for x in mycomlist:
    if 'java' in x:
        newlist.append(x)
print(mycomlist,'\n')


mycomlist1 = ['python', 'java', 'c++', 'javascript']
newlist1 = [x for x in mycomlist1 if 'java' in x]
print(mycomlist1)
print('\n')


# Condition
# The condition is like a filter that only accepts the items that evaluate to True.
mycomlist2 = ['python', 'java', 'c++', 'javascript']
newlist2 = [x for x in mycomlist1 if x != 'java']
print(mycomlist2)
print('\n')

# Iterable 
# The iterable can be any iterable object, like a list, tuple, set etc.

mycomlist3 = ['python', 'java', 'c++', 'javascript']
newlist3 = [x for x in mycomlist3]
print(mycomlist3)
print('\n')


newlist4 = [x for x in range(10) if x < 5]
print(newlist4)
print('\n')

#Expression
mycomlist4 = ['python', 'java', 'c++', 'javascript']
newlist5 = [x.upper() for x in mycomlist4]
print(newlist5)
print('\n')


# Replace all elements with Fire string

mycomlist5 = ['python', 'java', 'c++', 'javascript']
newlist6 = ['fire' for x in mycomlist5]
print(newlist6)
print('\n')

# Return "orange" instead of "banana":

mycomlist6 = ['apple', 'banana', 'cherry', 'orange']
newlist7 = [x if x != 'banana' else 'pineapple' for x in mycomlist6]
print(newlist7)
print('\n')