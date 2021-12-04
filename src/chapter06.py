"""Chapter 06 - Dictionaries"""

"""
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
"""
print("\n/// 6-1")

fiction_person = {'first_name': 'John',
                  'last_name': 'Smith',
                  'age': 33,
                  'city': 'Los Angeles'}

print(fiction_person.get('first_name'))
print(fiction_person.get('last_name'))
print(fiction_person.get('age'))
print(fiction_person.get('city'))

"""
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a
favorite number for each person, and store each as a value in your dictionary. 
Print each person’s name and their favorite number. For even more fun, poll a 
few friends and get some actual data for your program.
"""
print("\n/// 6-2")

favourite_numbers = {'Hanna': 6,
                     'Joseph': 12,
                     'Peter': 34,
                     'Maria': 13,
                     'Dan': 19}

for name, number in favourite_numbers.items():
    print(f"{name}'s favourite number is {number}, now you know it ...")

"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
•	 Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
•	 Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output
"""
print("\n/// 6-3")

programming_words = {'programming': 'making computers do stuff',
                     'coding': 'using code to make computers work',
                     'python': 'great programming language',
                     'duck typing': 'the expression used to explain dynamic '
                                    'data types',
                     'multi-paradigm': 'term used for programming languages,'
                                       'which can be used as functional,'
                                       'structured or object-oriented'}

for expressions, explanation in programming_words.items():
    print(f"{expressions.upper()}: \n\t- {explanation}")

"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""
print("\n/// 6-4")

for key in fiction_person:
    print(key)
for key in fiction_person.keys():
    print(key)
for value in fiction_person.values():
    print(value)
for key, value in fiction_person.items():
    print(key, value)

"""
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
•	 Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
•	 Use a loop to print the name of each river included in the dictionary.
•	 Use a loop to print the name of each country included in the dictionary
"""
print("\n/// 6-5")

rivers = {'Danube': 'Slovakia',
          'Vltava': 'Czech Republic',
          'Themes': "England"}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")
for river in rivers:
    print(f"River: {river}")
for country in rivers.values():
    print(f"Country: {country}")

"""
6-6. Polling: Use the code in favorite_languages.py (page 97).
•	 Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""
print("\n/// 6-6")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

poll_people = ['jen', 'thomas', 'edward', 'john']

for person in poll_people:
    if person in favorite_languages:
        print(f"Thank you {person.title()} to taking the poll and selecting the "
              f"{favorite_languages.get(person).title()} as the favorite language.")
    else:
        print(f"Dear {person.title()}, would you like to take the poll about"
              f"your favorite language?")

"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""
print("\n/// 6-7")

person1 = {'first_name': 'John',
                  'last_name': 'Smith',
                  'age': 33,
                  'city': 'Los Angeles'}

person2 = {'first_name': 'David',
                  'last_name': 'Beckham',
                  'age': 43,
                  'city': 'London'}

person3 = {'first_name': 'Cristiano',
                  'last_name': 'Ronaldo',
                  'age': 36,
                  'city': 'Manchester'}

persons = [person1, person2, person3]
for person in persons:
    print()
    for key, value in person.items():
        print(f"{key}: {value}")

"""
6-8. Pets: Make several dictionaries, where each dictionary represents a
different pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your
list and as you do, print everything you know about each pet.
"""
print("\n/// 6-8")

pet1 = {'animal': 'dog',
        'owner': 'dog ownerson'}
pet2 = {'animal': 'cat',
        'owner': 'catherine cathson'}
pet3 = {'animal': 'mouse',
        'owner': 'mickey the mouse'}

pets = [pet1, pet2, pet3]
for pet in reversed(pets):
    print()
    for key, value in pet.items():
        print(f"{key}: {value.title()}")

"""
6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places
"""
print("\n/// 6-9")

favorite_places = {'Freddie': 'Barcelona',
                   'Kevin': ['New York', 'Chicago'],
                   'Natasha': ['Moscow', 'St. Pettersburg', 'Kyjev']}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are "
          f"{', '.join(place for place in places) if type(places) is list else places}")

"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99)
so each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""
print("\n/// 6-10")

favourite_numbers = {'Hanna': [6, 1, 7],
                     'Joseph': [12, 13, 14],
                     'Peter': [34],
                     'Maria': [13, 100],
                     'Dan': [19, 29, 39, 49, 59]}

for name, numbers in favourite_numbers.items():
    print(f"{name}'s favourite numbers are "
          f"{', '.join(str(number) for number in numbers)}")

"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the
information you have stored about it
"""
print("\n/// 6-11")
cities = {'Prague':
              {'country': 'Czech Rep', 'population': 1000000, 'rating': 2},
          'Valencia':
              {'country': 'Spain', 'population': 800000, 'rating': 1},
          'Osaka':
              {'country': 'Japan', 'population': 20000000, 'rating': 3},
          }

for city, information in cities.items():
    print()
    print(f"{city.upper()}:")
    for element, info in information.items():
        print(f"\t- {element}: {info}")

"""
6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example
programs from this chapter, and extend it by adding new keys and values,
changing the context of the program or improving the formatting of the output.
"""
# all done above
