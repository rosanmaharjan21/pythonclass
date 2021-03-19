# x = 5
# y = 10
# z = x + y
# print(f"the sum of x and y is: {z}")

# x = '5'
# print(type(x))  # it is a string type since it is in single colon ''
# x = '5'
# x = int(x)
# print(type(x)) it changes its string type to integer

# boolean example
# user_Name = 'rosan'
# print('z' in user_Name) prints false
# print('r' in user_Name)  prints true

# list example
# data = ['rosy', 'romi', 'rosan', 'kriti']
# # print(data[2])  prints 3rd value in index because index count starts with zero
# print(data[1:3])  prints value from 1:3 but it doesnot prints the 3rd value

# data = [
#     ['rosy', 'romi', 'rosan', 'kriti'],
#     ['tulasa', 'krishna', 'sita', 'gita'],
#     ['samiel', 'unnati', 'krisha', 'sabhya'],
#     ['prajwol', 'ajay', 'nabin', 'rabin']
# ]
# # print(data[3][1])  [3][1] means it prints 4th row 2nd value because index count starts with zero

# list example
# data = ['father', 'mother', 'sister', 'brother']
# data[0:4] = 'krishna', 'tulasa', 'rosy', 'rosan'   replaces data accordingly
# data[1] = 'tulasa'  replaces mother with tulasa because it is in 1 place. starts from zero
# print(data)

# tuple example
# data = ('rosan', 'romi', 'rosy')
# data[0] = 'kriti'
# print(data) it shows error because we cannot change the value in tuple

# set example  it doesnot allows duplicate data in the set so it removes the duplicate data
# data = {'ram', 'sita', 'gita', 'ram','sita'}   kun chai duplicate data chai remove garxa sir lai sodnu
# print(data)


# dictionary example
# data = [
#     {"name": "rosan", "age": "30", "sex": "male"},
#     {"name1": "romi", "age": "32", "sex": "female"},
#     {"name2": "rosy ", "age": "34", "sex": "female"}
#
# ]
# print(data["name"])

# if condition
# if 5 > 2:
#     print("this is true")
# else:
#     print("this is false")


# # concatenate case
# x = 'awesome'
# print("python is " + x)

# creating variable outside of function and using inside function

# x = 'awesome'
#
#
# def myfunc():
#     print("python is " + x)
#
#
# myfunc()

# x = "awesome"
#
#
# def myfunc():
#     x = "fantastic"
#     print("Python is " + x)  creating variable with same name inside function prints the variable created with in function

#
#
# myfunc()  it prints python is fantastic
# print("python is " +x)  it prints python is awesome

# if you define vaiable as global it prints global value not the value inside or outside the function
# x = "awesome"
#
# def myfunc():
#     global x
#     x = "fantastic"
#     print("Python is " + x)
#
# myfunc()
#
# print("Python is " + x)  just prints python is fantastic

# strip function helps to remove space in the front and back of the value
# txt = "       Hello World "
# x = txt.strip()
# print(x)   it prints "hello world" instead of "     Hello world"

# len function
# x = "Hello World"    it helps to get the length of the value. it counts space as well
# print(len(x))  the output is 11.since it counts the space too

# upper function
# txt = "Hello World"   it converts value to all uppercase
# txt = txt.upper()
# print(txt) it prints HELLO WORLD instead of Hello World

# lower funtion
# txt = "Hello World"   it converts all letters to lower case
# txt = txt.lower()
# print(txt)    it prints hello world instead of Hello World

# # replace function
# txt = "Hello World"  it replaces h character with j
# txt = txt.replace("H", "J")
# print(txt)   it prints jello world

# # place holder for age
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# append function
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")    it helps to add value in the existing list
# print(fruits)   it prints apple,banana,cherry,orange

x = 5
x ^= 3
print(x)
