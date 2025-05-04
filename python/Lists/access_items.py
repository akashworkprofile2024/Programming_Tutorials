# Access Items in a List
listarr = ["Python", "Java", "C++", "JavaScript", "Ruby"]
print('Access Items: ',listarr[3],'\n')  # Accessing the first item

# Negative Indexing
print('Negative Indexing: ',listarr[-1],'\n')  # Accessing the last item

# Range of Indexes
print('Range of Indexes [1:4]: ',listarr[1:4],'\n')  # Accessing a range of items
print('Range of Indexes [:3]: ',listarr[:3],'\n')  # Accessing a range of items from the beginning
print('Range of Indexes [2:]: ',listarr[2:],'\n')  # Accessing a range of items from the end
print('Range of Negative Indexes [-4:-1]: ',listarr[-4:-1],'\n')  # Accessing a range of items using negative indexing


# Check if Item Exists
if "C++" in  listarr:
    print('C++ is in the list','\n')
else:
    print('C++ is not in the list','\n')    