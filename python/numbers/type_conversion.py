x = 1
y = 1.0


print("Before:" , x , y)
print("Type Before: ", type(x),type(y),'\n')

a = float(x) #convert int to float
b = int(y) #convert float to int
c = complex(x) #convert int to complex

print("After:" , a ,b , c)
print("Type Before: ", type(a),type(b),type(c))



# Random Value
import random
print("Random_Generate:" , random.randrange(1,10))