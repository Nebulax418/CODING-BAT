divider = "-" * 10

# Trick one: Swapping two variables
# swap two variables

a = 8
b = 9

a, b = b, a

print(a, b)




# Trick 2: Min and max for lists

# max and min for the largest and smallest value in variables
print(divider)

dedi = [1, 2, 3, 4]
largest = max([dedi])
smallest= min([dedi])
print(largest)
print(smallest)





# Trick 3: Using list comprehension

# use list comprehension man
print(divider)

evens = [x for x in range(20) if x % 2 == 0]

print(evens)





# Trick 4: Using the map function

# map function --> applys a function to each element of an iterable
# you can pass more than one iterable to the map function
print(divider)

def square(number):
    return number ** 2

mapper = [1, 2, 3, 4, 5, 6, 7, 8] 

# square() is applied to each element in mapper list
# returns an object of map class 
# so we need to convert to a data structure to work with it

modified_mapper = list(map(square, mapper))

print(mapper)
print(modified_mapper)

# for i in modified_mapper:
#     print(i)

print(i for i in modified_mapper)




# Trick 5: Listing elements in the same line
print(divider)
list_things = [2, 3, 4, 5, 6, 7, 8, 9]

# list all in the same line
print(*list_things)





# Trick 6: Using any and all
print(divider)

heat = 500
earth = 992
maps = 2232

conditions = [
    
    heat < 50, 
    earth < 70, 
    maps > 90

]


"""
# if all(conditions):
#     print(True) 
 
# if any(conditions):
#     print(True)
"""


# Trick 7: Using the TERNARY OPERATOR

# if a is less than b then return 7. if it isn't then return 10
# c now evaluates to a value based on the condition
print(divider)
c = 7 if a < b else 10

print(c)





# Trick number 8:

# Taking multiple inputs at a time

# taking multiple inputs at a time 
# and type casting using list() function

# x makes a list of inputs 
# Needs int values to be mapped to each list element - applys int() function TO EACH ELEMENT OF THE ENTERED NUMBERS
# allows for iteration
"""
print(divider)
x = list(
    
    map(
        
        # CONVERTS THE INPUT TO INT - USING map
        int, input (
        
            "Enter multiple values: "
        
        ).split()
    
    )
)
# """



# Trick number 9: - Use \ to extend variables
print(divider)


a = 1 + 2 + 3 \
    + 4+ 5



# Trick 10
# Just use lambdas to simplify everything

num1 = [1,2,3]
num2 = [4,5,6]

squares = list(map(lambda n1 : n1 ** 2 if n1 % 2 == 0 else float(n1/2), num1))
print(squares)



# Trick 11: Using pdb
# extremely nice debugging 
# very large python file
"""import pdb
   pdb.set_trace()"""
   
"""Also so import this for the zen of python"""
""" ~import this~ """
   
   

# Trick 12: Multiline assignment
print(divider)

x, y, z, w, h = 1, 2, 3, 4, 5
print(*(x, y, z, w, h))




# Trick 13:

# Using the zip funtion to pair list elements and values to correspond together
print(divider)
ages = [12, 13, 14]
names = ["Bill", "Bob", "John"]
fav_colors = ["Blue", "Red", "Greem"]

# keep in mind that if one of the lengths of the list is not equal then python
# will just skip that element and print whatever is up to the last element
# the most common last number available in all lists as long as lists are not empty
# if one of them is empty then python will just do the other lists with the other lists

# make new tuples of paired items/values so that duplicates do not occur
zipped = list(zip(ages, names, fav_colors))

print(zipped)

# we can also iterate through zip

for age, name, color in zip(ages, names, fav_colors):
    print(*(name, age, color))
    
    

# Trick 14: Using help()
# We can get help on anything (mostly) from modules, classes, methods, and keywords



# Trick 15: Using the dir function to get attributes related to an object


# Trick 16: Using annoymous variables
# If you do not need don't put it
# We do not rely on the iterator variable
print(divider)
for _ in range(5):
    print("Hello") 




# Trick 17: Using .join()
print(divider)
words = ["Hello", "nt", "name", "is"]
# you can seperate using any delimiter/seperator
print(", ".join(words))



# Trick 18: Reversing a string
print(divider)
st = "Hello"

# reversing a string
print(st[::-1])



# Trick 19: hello world trick
print(divider)
# import __hello__


# using sys - Trick 20
import sys
print(divider)
x = 100
# get the size of any object
print(sys.getsizeof(x))



# Trick 21: get the most frequent element from a list
print(divider)
o = [1,2,3,4,5, 5, 5]
print(max(set(o), key=o.count))


# Trick 22: Getting the most frequent element

jj = [(1, 2), (3, 4), (5, 6)]

# lambda function of y which returns y[1] in each of the tuples
print(max(jj, key=lambda y: y[1]))


# Trick 23
# import antigravity


# Trick 24: Split and unpack
kkl = [1,2,3,4,5]
# print(1,2,3,4,5) --> *kkl



# takes unlimited number of arguments
def fun(*args):
    print(args)

# also **kwargs prints things as a dictionary



# other tricks
print(divider)

thinger = [1,2,3,3,3,4,5,5,6]

print(set(thinger))


# taking multiple paramenters
print(divider)

def takeMultiple(*args):
    result = 0
    for i in args:
        result+=i
    
    return result 
    
print(takeMultiple(2,3,4,5,6,7))    



# Palindrome - if the reverse of the string is the same
# as the string


stx = "wow"

print(True if stx == stx[::-1] else False)

