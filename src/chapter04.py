# 4-1
pizzas = ["vegan", "plant-based", "simple"]
for pizza in pizzas:
    print(f"I like only {pizza.title()} pizza!")
print("Yes, actually I don't think it is a good think to eat pizzas!")

# 4-2
animals = ["Elephant", "Giraffe", "Tiger"]
for animal in animals:
    print(f'{animal.title()} is a really cool!')
print("This kinds of animal you can see \"live\" mainly in Africa.")

# 4-3
for number in range (1, 21):
    print(number)

# 4-4
numbers = [num for num in range(1, 1_000_001)]
# for number in numbers:
#     print(number)

# 4-5
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# 4-6
odd_numbers = [num for num in range(1, 21, 2)]
for number in odd_numbers:
    print(number)

# 4-7
multiples_of_three = [num for num in range(3, 30, 3)]
for number in multiples_of_three:
    print(number)

# 4-8, 9
cubes = [num**3 for num in range(1, 11)]
[print(cube) for cube in cubes]

# 4-10
print(f'The first three items in the cubes are {cubes[:3]}.')
print(f'The three items in the middle of the cubes are {cubes[3:7]}.')
print(f'The last three items in the cubes are {cubes[-3:]}.')

# 4-11
friend_pizzas = pizzas[:]
pizzas.append("Another veggie")
friend_pizzas.append('Ham')

print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("My friend's favourite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())

# 4-12?

# 4-13
foods = ('spaghetti', 'soup', 'vegan steak', 'sandwich', 'cake')
for food in foods:
    print(food)
# foods[2] = 'hamburger'
foods = ('hamburger', 'soup', 'vegan steak', 'hot dog', 'cake')
print(foods)
