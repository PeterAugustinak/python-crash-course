"""Chapter 08 - Functions"""
from chapter08_printing_functions import make_car_imported


"""
8-1. Message: Write a function called display_message() that prints one 
sentence telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
"""
print("\n/// 8-1")


def display_message():
    print("This chapter is about learning Python functions.")

display_message()
"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""
print("\n/// 8-2")


def favorite_book(title):
    print(f"One of my favourite books is {title.title()}")

favorite_book("Outliers")

"""
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
"""
print("\n/// 8-3")


def make_shirt(size, text):
    print(f"The t-shirt to be made will be: \n\tsize of {size} "
          f"\n\tsaying {text}")

make_shirt("L", "I'm positional!")
make_shirt(text="I am keyword!", size="M")

"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""
print("\n/// 8-4")


def make_shirt_with_default(size="L", text="I love Python"):
    print(f"The t-shirt to be made will be: \n\tsize of {size} "
          f"\n\tsaying {text}")

make_shirt_with_default()
make_shirt_with_default("M")
make_shirt_with_default("S", "Any message here!")

"""
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country
"""
print("\n/// 8-5")


def describe_city(city, country="Slovakia"):
    print(f"{city.title()} is in the {country.title()}.")

describe_city("Spisska Nova Ves")
describe_city("Martin")
describe_city("Warsaw", "Poland")

"""
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
"""
print("\n/// 8-6")


def city_country(city, country):
    return f"{city}, {country}"

print(city_country("New York", "USA"))
print(city_country("Paris", "France"))
print(city_country("Milan", "Italy"))

"""
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
"""
print("\n/// 8-7")


def make_album(artist, title, songs_count=None):
    album = {"artist": artist, "title": title} if not songs_count else \
        {"artist": artist, "title": title, "songs": songs_count}

    return album

print(make_album("Bad Religion", "Suffer"))
print(make_album("NOFX", "Punk in drublic"))
print(make_album("Offspring", "Americana", 13))

"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop
"""
print("\n/// 8-8")

while True:
    artist = input("Add the artist name (q for quit): ")
    if artist == 'q':
        break
    title =  input("Add the album title (q for quit): ")
    if title == 'q':
        break
    songs = input("Add the number of songs "
                  "(optional, ENTER for skip, q for quit): ")
    if songs == 'q':
        break
    album = make_album(artist, title, songs)
    print(album)

print("Thank you for cooperation!")

"""
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages(), which prints each text message.
"""
print("\n/// 8-9")
messages = ["Hey you!", "How you doing?", "I don't care."]


def show_messages(message_lst):
    for message in message_lst:
        print(message)

show_messages(messages)

"""
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
"""
print("\n/// 8-10")
original_messages = ["Hey you!", "How you doing?", "I don't care."]
sent_messages = []


# NEVER USE list.remove() in for loop! Use while loop instead!
def send_messages(message_lst):
    while message_lst:
        message  = message_lst.pop()
        sent_messages.append(message)

send_messages(original_messages)
print(f"Original list: {original_messages}")
print(f"Sent messages list: {sent_messages}")

"""
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
"""
print("\n/// 8-11")
original_messages = ["Hey you!", "How you doing?", "I don't care."]
sent_messages = []

send_messages(original_messages[:])
print(original_messages)
print(sent_messages)

"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the 
sandwich that’s being ordered. Call the function three times, using a different 
number of arguments each time.
"""
print("\n/// 8-12")


def make_sandwich_from(*ingredients):
    print("This sandwich will contain:")
    for ingredient in ingredients:
        print(f"\t - {ingredient}")


make_sandwich_from("cherry, vegan cheese, bread")
make_sandwich_from("beans")
make_sandwich_from()

"""
8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""
print("\n/// 8-13")


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('John',
                             'Smith',
                             location='Slovakia',
                             field='computers')

print(user_profile)


"""
8-14. Cars: Write a function that stores information about a car in a 
dictionary. The function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. Call the 
function with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this 
one: car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""
print("\n/// 8-14")


def make_car(manufacturer, model_name, **car_parameters):
    car_parameters['manufacturer'] = manufacturer
    car_parameters['model name'] = model_name
    return car_parameters


car = make_car("BTTF", "DeLorean", color = "silver", fly = True)
print(car)

"""
8-15. Printing Models: Put the functions for the example printing_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of printing_models.py, and modify the file to use the imported functions.
"""
print("\n/// 8-15")

car_imported = make_car_imported("Skoda", "Superb", color = "black", fly = False)
print(car_imported)

"""
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
"""
print("\n/// 8-16")

import chapter08_printing_functions
from chapter08_printing_functions import make_car_imported
from chapter08_printing_functions import make_car_imported as mki
import chapter08_printing_functions as pf
from chapter08_printing_functions import *

"""
8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.
"""
# all above
