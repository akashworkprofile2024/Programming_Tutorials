x0 = 5           #integer

y0 = 5.0         #float 

z0 = True        #boolean
print(type(x0), type(y0) , type(z0),"\n")

x1 = 1j          #Complex
y1 = ["Akash" , "Biswas"]   #List
z1 = ("Akash" , "Biswas")   #Tuple

print(type(x1) , type(y1) , type(z1))

x2 = range(9)                              #Range

y2={"Name:":"Akash" , "lastname":"Biswas"} #Dict

z2={"Akash" , "Biswas"}                    #Set 
print(type(x2) , type(y2) , type(z2))


x3 = frozenset({"Akash","Biswas"})        #Frozenset                            

z3=b"Hello"                               #Bytes
print(type(x3)  , type(z3))

x4=bytearray(5)                          #ByteArray  

y4=memoryview(bytes(5))                  #MemoryView

z4=None                                  #None Empty
print(type(x4),type(y4),type(z4))



''' 
Memoryview: 

In Python, memoryview is a built-in type that lets you access the memory of other binary objects without copying them.
It’s super useful when you want to work with large data (like bytes, bytearrays, or other buffers) efficiently. 


ByteArray:

    bytearray is a mutable sequence of bytes (integers from 0 to 255).

    Think of it like a list of small numbers (0-255), but stored efficiently in memory.

    You can modify it (unlike bytes, which are immutable).

Frozenset:

    A frozenset is just like a set — a collection of unique, unordered elements.

    BUT: it is immutable — once you create it, you can't add, remove, or change elements.

    Basically:
    → set = mutable
    → frozenset = immutable



'''