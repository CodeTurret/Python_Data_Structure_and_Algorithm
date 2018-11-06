#Declare an array

from array import *

 #arrayName = array(typecode, [initializer])

arrayName = array('i', [10,20,21,22,45,32])

 #print array

for i in arrayName:
     print(i)


# Insertion Operation
#arrayName.insert(position, value)
arrayName.insert(1,98)

for i in arrayName:
     print(i)

# Deletion Operation

arrayName.remove(98)

# Search Operation

print(arrayName.index(45))

# Update Operation

array1 = array('i', [10,20,30,40,50])

array1[2] = 80

for x in array1:
 print(x)
