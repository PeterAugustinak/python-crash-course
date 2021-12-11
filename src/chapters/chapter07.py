"""Chapter 07 - User input and while loops"""

"""
7-1. Rental Car: Write a program that asks the user what kind of rental car
they would like. Print a message about that car, such as “Let me see if I can
 find you a Subaru.”
"""
print("\n/// 7-1")
car_to_rent = input("What kind of car would you like to rent? ")
print(f"Ok, let me see if I can find you some {car_to_rent}.")

"""
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message
saying they’ll have to wait for a table. Otherwise, report that their table
is ready.
"""
print("\n/// 7-2")
group_to_sit = int(input("Hello, how many people are in your dinning group? "))
if group_to_sit <= 8:
    print("Ok, your table is ready.")
else:
    print("Ok, you need to wait for your table.")

"""
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
"""
print("\n/// 7-3")
user_number = int(input("Tell me a number an I will tell you if it is a"
                        " multiple of 10. "))
if user_number % 10 == 0:
    print(f"Yes, the {user_number} actually is a multiple of 10!")
else:
    print(f"No, the {user_number} is not a multiple of 10.")

"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""
print("\n/// 7-4")
pizza_topping = None
while pizza_topping != 'quit':
    pizza_topping = input("Please select a topping for your pizza (input "
                          "'quit' to finish): ")

"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending
on a person’s age. If a person is under the age of 3, the ticket is free; 
if they are between 3 and 12, the ticket is $10; and if they are over age 12,
the ticket is $15. Write a loop in which you ask users their age, and then tell
them the cost of their movie ticket
"""
print("\n/// 7-5")
age = None
while age != 'q':
    age = input("What is your age? ")
    try:
        age = int(age)
        if age < 3:
            print("The ticket is free!")
        elif 3 <= age < 12:
            print("The ticket is $10.")
        else:
            print("The ticket is 15$.")
    except ValueError:
        if age == 'q':
            break
        else:
            print("Incorrect answer, please input age or 'q' to quit.")
            age = None

"""
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise
7-5 that do each of the following at least once:
•	 Use a conditional test in the while statement to stop the loop.
•	 Use an active variable to control how long the loop runs.
•	 Use a break statement to exit the loop when the user enters a 'quit' value
"""
print("\n/// 7-6")
from random import randint
attempts = 3
number = randint(1, 11)
while attempts > 0:
    answer = input(f"Attempt {attempts}: Guess the number between 1-10: ")
    try:
        answer = int(answer)
        if answer != number:
            print("This is not a correct number! ")
            attempts -= 1
        elif answer == number:
            print("That's a correct number!")
            break
    except ValueError:
        if answer == 'q':
            print("Thank you for playing!")
            break
        else:
            print("Please answer number o 'q' for exit. ")
else:
    print("Sorry, your attempts are over ..")

"""
7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.)
"""
print("\n/// 7-7")
# while True:
#     print("This is an infinite loop, please stop me!")

"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of
various sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""
print("\n/// 7-8")

sandwich_orders = ['veggie', 'plant-based', 'cherry', 'fresh']
made_sandwiches = []

while sandwich_orders:
    made_one = sandwich_orders.pop()
    print(f"Your {made_one} is ready!")
    made_sandwiches.append(made_one)

print(f"All your sandwiches are done: "
      f"{', '.join(san for san in made_sandwiches)}")
print(f"Remaining sandwiches: {sandwich_orders}")

"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""
print("\n/// 7-9")
sandwich_orders = ['pastrami', 'veggie', 'pastrami', 'plant-based', 'cherry',
                   'fresh', 'pastrami']
made_sandwiches = []

print("Sorry, we are out of pastrami, all the pastrami sandwiches won't be "
      "made today ...")
while sandwich_orders:
    made_one = sandwich_orders.pop()
    if made_one == 'pastrami':
        pass
    else:
        print(f"Your {made_one} is ready!")
        made_sandwiches.append(made_one)

print(f"All your sandwiches are done: "
      f"{', '.join(san for san in made_sandwiches)}")
print(f"Remaining sandwiches: {sandwich_orders}")

"""
7-10. Dream Vacation: Write a program that polls users about their dream 
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the
poll.
"""
print("\n/// 7-10")
poll_result = {}
polling = True
while polling:
    name = input("What is your name? ")
    poll_result[name] = []
    done = False
    while not done:
        place = input("What is your favourite place to holiday? ")
        poll_result[name].append(place)
        next_place = input("Another place? If not, put 'n': ")
        if next_place == 'n':
            done = True
    else:
        cont = input("Another person to poll? y/n ")
        if cont == 'n':
            polling = False
else:
    print("Thank you all to taking this poll! Here are the results:")
    for name, places in poll_result.items():
        print(f"{name.upper()}:")
        print(f"\tFavourite places: {', '.join(place for place in places)}")
