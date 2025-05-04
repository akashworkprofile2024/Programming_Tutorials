# Center()
a='Akash'
print(a.center(20,'*'),'\n') # center the string with * in 20 spaces

# Count()
b='This is Python Class , Python is 5th Gen Language'
print(b.count('Python'),b.count('is')) # count the number of times 'Python' appears in the string

# Find()
c='This is Python Class , Python is 5th Gen Language'
print('Find Python',c.find('Python'),'\n'+'Find is:',c.find('is'),'\n') # find the first occurrence of 'Python' in the string

#Format()
text = "The mouse Price is Rs {price:.2f}"
print(text.format(price=100),'\n')

text1 = "The mouse Price is Rs {price:.2f}".format(price=100)  # format the string with the price value in one line
print(text1,'\n')

# Name Format Indexing
text2 = "{product1} price is {product1_price:.2f} and {product2} price is {product2_price:.2f}".format(product1='Mouse',product1_price=250, product2='Keyboard',product2_price=500)
print('Name Format Indexing: ',text2,'\n') # format the string with the product name and price values

#Number Format indexing
text3 = "My name is {0} {1}".format("Akash",'Biswas')
print('Number Format indexing: ',text3,'\n') # format the string with the name and last name values

#Empty Placeholder indexing
text4 = "My name is {} {}".format("Akash",'Biswas')
print("Empty Placeholder indexing: ",text4,'\n') # format the string with the name and last name values

#index()
container  = 'What a Wonderful World'
print('Index of Wonderful:',container.index('Wonderful'),'\n') # find the first occurrence of 'Wonderful' in the string
print('Index of World:',container.index("onder" , 2 , 20),'\n')  #Count 2 as 0th index and 20 as 19th index

container2 = "Hello, welcome to my world."

print("Using Find Function:",container2.find("q"),'\n') # Find returns -1 if the substring is not found
#print("Using Index Function: ",container2.index("q")) # Index raises ValueError if the substring is not found

# Isalnum()
container3 = "Hello123"
container4 = "Hello 123"
print('Is Alphanumeric:',container3.isalnum()) # check if the string is alphanumeric
print('Is Alphanumeric:',container4.isalnum(),'\n') # check if the string is alphanumeric


# Isalpha()
container5 = "Hello"
container6 = "Hello123"
print('Is Alphabet:',container5.isalpha()) # check if the string is alphabetic
print('Is Alphabet:',container6.isalpha(),'\n') # check if the string is alphabetic


# Isdigit()
container7 = "12345"
container8 = "12345abc"
print('Is Digit:',container7.isdigit()) # check if the string is numeric
print('Is Digit:',container8.isdigit(),'\n') # check if the string is numeric

# Islower()
container9 = "hello"
container10 = "Hello"   
print('Is Lower:',container9.islower()) # check if the string is in lowercase
print('Is Lower:',container10.islower(),'\n') # check if the string is in lowercase

# Isupper()
container11 = "HELLO"
container12 = "Hello"
print('Is Upper:',container11.isupper()) # check if the string is in uppercase
print('Is Upper:',container12.isupper(),'\n') # check if the string is in uppercase

# Isspace()
container13 = "   "
container14 = "Hello"
print('Is Space:',container13.isspace()) # check if the string is whitespace
print('Is Space:',container14.isspace(),'\n') # check if the string is whitespace

# Isprintable()
container15 = "Hello"
container16 = "Hello\n"
print('Is Printable:',container15.isprintable()) # check if the string is printable
print('Is Printable:',container16.isprintable(),'\n') # check if the string is printable

# Isidentifier()
container17 = "Hello123"
container18 = "123Hello"
print('Is Identifier:',container17.isidentifier()) # check if the string is a valid identifier
print('Is Identifier:',container18.isidentifier(),'\n') # check if the string is a valid identifier

# Isnumeric()
container19 = "12345"
container20 = "12345abc"
print('Is Numeric:',container19.isnumeric()) # check if the string is numeric
print('Is Numeric:',container20.isnumeric(),'\n') # check if the string is numeric

# Isdecimal()
container21 = "12345"
container22 = "12345abc"
print('Is Decimal:',container21.isdecimal()) # check if the string is decimal
print('Is Decimal:',container22.isdecimal(),'\n') # check if the string is decimal

#lstrip()
container23 = "   Grow Win Institute   "
container24 = ",,,,,.wwxxyy,,,,,,Grow Win Institute"
print("Without lstrip:",'Welcome to',container23) # remove leading whitespace from the string
print("With lstrip:",'Welcome to',container23.lstrip(),'\n') # remove leading whitespace from the string

print("Without lstrip:",'Welcome to',container24) # remove leading whitespace from the string
print("With lstrip:",'Welcome to',container24.lstrip('.,wwxxyy'),'\n') # remove leading whitespace from the string


#maketrans()
container25 = "Hello mython"
mytable = str.maketrans("mython", "python")
print('Before maketrans:',container25) # print the original string
print('After maketrans:',container25.translate(mytable),'\n') # translate the string using the translation table

#partition()
container26 = "Python is popular among developers"
refine = container26.partition("popular") # partition the string into three parts: before, separator, and after
print(refine,'\n') 

#Replace()
container27 = "Python is popular among developers"
container28 = "Python is popular among developers and Python is easy to learn"
print("Replace Method: ",container27.replace("developers", "Programmers")) # replace the first occurrence of 'developers' with 'Programmers'
print("Replace Method: ",container28.replace("Python", "Java"),'\n') # replace the first occurrence of 'Python' with 'Java'


#rfind()
container29 = "Python is popular among developers"
refine2 = container29.rfind("among") # find the last occurrence of 'casa' in the string
print('Last Occurrence of among:',refine2) # find the last occurrence of 'casa' in the string


