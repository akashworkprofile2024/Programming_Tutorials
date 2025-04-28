# Normal String
a = "Python Class"
print("String: ",a +" "+"Type: ",type(a),'\n')


# Quote inside Quote
b = "100 Rupees 'Paid' "
print('Quote inside Quote:',b,'\n')

# Multi Line String
c = """Python is 5th generation language \n 
This Language Easy to Learn \n 
Python is Robust Language
"""
print("MultiLine:",c,'\n')

# Strings are Arrays
aa = "Akash Biswas"
print("String Arrays: ",aa[0],'\n')

#Looping Through a String
print('Looping String')
for i in aa:    
    print(i,end='',) 
print('\n')

# String Length
textlen = "antidisestablishmentarianism"  
print("String_Length: ",len(textlen),'\n')

# Check String
txtcheck = "Akash"
print("String Check:")
print('Akash' in txtcheck)
print("Gupta" in txtcheck)
print("akash" in txtcheck,'\n')

#Check Using If else
print("Check String With If Else:")
if "Gupta" in txtcheck:
    print('String present')
else:
    print("String Not Present",'\n')    


# Check String if NOT
txtcheck = "Akash"
print("String If Not Present:")
print("Akash" not in txtcheck)    
print("Ak" not in txtcheck)    
print("Gupta" not in txtcheck)    