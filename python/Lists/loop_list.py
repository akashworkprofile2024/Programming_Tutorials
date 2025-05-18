# Loop Through a List
myarr = ['Python', 'Java', 'C++', 'JavaScript']
for x in myarr:
    print(x)
print('\n')    

# Loop Through the Index Numbers
myarr1 = ['Python', 'Java', 'C++', 'JavaScript']
for i in range(len(myarr1)):
    print(myarr1[i])
print('\n')    

# Using a While Loop
myarr2 = ['Python', 'Java', 'C++', 'JavaScript']
i = 0 
while i < len(myarr2):
    print(myarr2[i])
    i = i + 1
print('\n')

# Looping Using List Comprehension
myarr3 = ['Python', 'Java', 'C++', 'JavaScript']
myarr4 = [x for x in myarr3]
print(myarr4)
print('\n')