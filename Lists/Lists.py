#The list is a most versatile datatype available in Python
#which can be written as a list of comma-separated values (items) between square
#brackets. Important thing about a list is that items in a list need not be of
#the same type.

# declare a list

list1 = ['physics','math', 1908, 1990, 'CSE', 2000]

# Accessing Values in list

print ("list1[2:5]: ", list1[2:5])

# Updating Lists
list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001
print ("New value available at index 2 : ")
print (list[2])

# Delete List element

list2 = ['physics', 'chemistry', 1997, 2000]
print (list2)
del list2[2]
print ("After deleting value at index 2 : ")
print (list2)
