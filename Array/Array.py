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

for i in arrayName:
     print(i)
