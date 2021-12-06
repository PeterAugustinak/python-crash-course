"""Chapter 04 - Working with Lists"""

"""
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
•	 Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.
•	 Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!
"""
print("\n/// 4-1")

pizzas = ["vegan", "plant-based", "simple"]
for pizza in pizzas:
    print(f"I like only {pizza.title()} pizza!")
print("Yes, actually I don't think it is a good think to eat pizzas!")

"""
4-2. Animals: Think of at least three different animals that have a common 
characteristic. Store the names of these animals in a list, and then use a for 
loop to print out the name of each animal.
•	 Modify your program to print a statement about each animal, such as
A dog would make a great pet.
•	 Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!
Working with Lists 57
Making Numerical Lists
Many reasons exist to
"""
print("\n/// 4-2")

animals = ["Elephant", "Giraffe", "Tiger"]
for animal in animals:
    print(f'{animal.title()} is a really cool!')
print("This kinds of animal you can see \"live\" mainly in Africa.")

"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.
"""
print("\n/// 4-3")

for number in range (1, 21):
    print(number)

"""
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it 
by pressing ctrl-C or by closing the output window.)
"""
print("\n/// 4-4")

numbers = [num for num in range(1, 1_000_001)]
# for number in numbers:
#     print(number)

"""
4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
"""
print("\n/// 4-5")
print(max(numbers))

print(min(numbers))
print(sum(numbers))

"""
4-6. Odd Numbers: Use the third argument of the range() function to make a
list of the odd numbers from 1 to 20. Use a for loop to print each number.
"""
print("\n/// 4-6")

odd_numbers = [num for num in range(1, 21, 2)]
for number in odd_numbers:
    print(number)

"""
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.
"""
print("\n/// 4-7")

multiples_of_three = [num for num in range(3, 30, 3)]
for number in multiples_of_three:
    print(number)

"""
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes 
(that is, the cube of each integer from 1 through 10), and use a for loop to 
print out the value of each cube
4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes
"""
print("\n/// 4-8, 9")

cubes = [num**3 for num in range(1, 11)]
[print(cube) for cube in cubes]

"""
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
•	 Print the message The first three items in the list are:. Then use a slice 
to print the first three items from that program’s list.
•	 Print the message Three items from the middle of the list are:. Use a slice 
to print three items from the middle of the list.
•	 Print the message The last three items in the list are:. Use a slice to 
print the last three items in the list.
"""
print("\n/// 4-10")

print(f'The first three items in the cubes are {cubes[:3]}.')
print(f'The three items in the middle of the cubes are {cubes[3:7]}.')
print(f'The last three items in the cubes are {cubes[-3:]}.')

"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
•	 Add a new pizza to the original list.
•	 Add a different pizza to the list friend_pizzas.
•	 Prove that you have two separate lists. Print the message My favorite
pizzas are:, and then use a for loop to print the first list. Print the message
My friend’s favorite pizzas are:, and then use a for loop to print the second 
list. Make sure each new pizza is stored in the appropriate list.
"""
print("\n/// 4-11")

friend_pizzas = pizzas[:]
pizzas.append("Another veggie")
friend_pizzas.append('Ham')

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friend's favourite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())

"""
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods.
"""
print("\n/// 4-12")
# above

"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of 
five simple foods, and store them in a tuple.
•	 Use a for loop to print each food the restaurant offers.
•	 Try to modify one of the items, and make sure that Python rejects the
change.
•	 The restaurant changes its menu, replacing two of the items with different
foods. Add a line that rewrites the tuple, and then use a for loop to print
each of the items on the revised menu.
"""
print("\n/// 4-13")

foods = ('spaghetti', 'soup', 'vegan steak', 'sandwich', 'cake')
for food in foods:
    print(food)
# foods[2] = 'hamburger'
foods = ('hamburger', 'soup', 'vegan steak', 'hot dog', 'cake')
print(foods)
