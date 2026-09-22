#List in Python

#Creating a list
my_list = [1,2,3, "apple", "banana"]
print("List: ")
print(my_list)

#Accessing elements in a list
print("Accessing elements in a list: ")
print(my_list[0])
print(my_list[2])
print(my_list[4])

#Modifying elements in a list
my_list[2] = 'orange'
print("Modified list: ")
print(my_list)

#Adding elements in a list
my_list.append('finger chips')
my_list.append(20)
print("List after adding elements: ")
print(my_list)

#Removing elements in a list
my_list.remove('orange')
print("List after removing elements: ")
print(my_list)
