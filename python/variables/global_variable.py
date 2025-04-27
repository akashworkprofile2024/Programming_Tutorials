# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

x = 'awesome1'
def func():
    print('Python is' +" "+x)

func()



y = "fantastic"
def func1():
    y = 'awesome2'
    print('Python is' + " " + y) #awesome2
func1()

print('Python is' + " " + y) #fantastic

# The Global Keyword
def function():
    global z
    z = 'easy to learn'

function()
print('Python is' + " " + z)



