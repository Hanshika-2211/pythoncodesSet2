# Write a program that creates a dictionary of cubes of odd numbers in the range 1-10.
dictionary = {number: number**3 for number in range(1, 11) if number % 2 != 0}
print("Dictionary of cubes of odd numbers:", dictionary)