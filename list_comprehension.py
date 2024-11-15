# list comprehension = a concise way to create lists in python 
#       compact and easier to read than traditional loops
#       [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x*2)
# print(doubles)

# instead of doing all that you can have it all in one line 
# doubles = [expression for value in iterable]

# doubles = [x*2 for x in range(1, 11)]
# print(doubles)
# triples = [y*3 for y in range(1, 11)]
# print(triples)
# squares = [z*z for z in range(1, 11)]
# print(squares)

# Example with words
# fruits = ["apple", "orange", "banana", "coconut"]
# fruits = [fruit.upper() for fruit in fruits]
# print(fruits)
# you can also do
# fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
# print(fruits)

# another example of use
# fruits = ["apple", "orange", "banana", "coconut"]
# fruits_chars = [fruit[0] for fruit in fruits]
# print(fruits_chars)

# numbers = [1, -2, 3, -4, 5, -6, 8, -7]
# positive_nums = [num for num in numbers if num >= 0]
# negative_nums = [num for num in numbers if num < 0]
# even_nums = [num for num in numbers if num % 2 == 0]
# odd_nums = [num for num in numbers if num % 2 == 1]
# print(positive_nums)
# print(negative_nums)
# print(even_nums)
# print(odd_nums)

# # this is how it would be written in one line 
# positive_nums = [num for num in [1, -2, 3, -4, 5, -6] if num >= 0]
# print(positive_nums)

# grades = [85, 42, 79, 90, 56, 61, 30]
# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)

# practice
# numbers = [3, 7, 10, 15, 21]
# double_values = [number * 2 for number in numbers]
# print(double_values)

# values = [8, 11, 20, 25, 32, 47, 55]
# odd_numbers = [num for num in values if num % 2 == 1]
# print(odd_numbers)

# words = ["apple", "banana", "cherry", "date"]
# word_length = [len(word) for word in words]
# print(word_length)

# nums = [4, 5, 6, 7, 8, 9, 10]
# squared_evens = [z*z for z in nums if z % 2 == 0]
# print(squared_evens)
# names = ["Alice", "Bob", "Amanda", "Charlie", "Anna", "David"]
# names_starting_with_a = [name for name in names if name[0] == "A"]
# print(names_starting_with_a)

# sentence = ["hello", "world", "python", "is", "great"]
# uppercase_words = [word.upper() for word in sentence]
# print(uppercase_words)

################################################List comprehension###############################################
# List Comprehensions Practice #1
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create a square_values list consisting of the numbers in the values list, squared.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #2
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# Create an even_values list consisting of the numbers in the values list that (you guessed it!) are even.

# values = [1, 2, 3, 4, 5, 6, 9.5]




# List Comprehensions Practice #3
# To do the coding exercise below, you can choose different paths. While the correct path in programming is the one that returns the correct result, I encourage you to try applying list comprehension concepts to begin to assimilate them for the future. They can be very useful in your professional practice!

# For the following list of temperatures in degrees Fahrenheit, express these same values in a new list of temperature values in degrees Celsius. The conversion between type of units is as follows:

# °C = (°F - 32) * (5/9)

# or expressed in another way:

# (degrees_fahrenheit-32)*(5/9)

# The list of temperatures is as follows:

# temperature_fahrenheit = [32, 212, 275]

# Store this new list in a variable called degrees_celsius




