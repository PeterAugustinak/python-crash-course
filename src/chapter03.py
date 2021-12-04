#3-1
friends = ["Chandler", "Rachel", "Monica"]
print(friends[0])
print(friends[1])
print(friends[2])

#3-2
print(f"Hello my friend {friends[0]}, how are you?")
print(f"Hello my friend {friends[1]}, how are you?")
print(f"Hello my friend {friends[2]}, how are you?")

#3-3
favourite_transportation_vehicles = ["bicycle", "foot", "train"]
print(f"My favourite vehicle is {favourite_transportation_vehicles[0]} as it"
      f" is healthy, cheap and fast.")
print(f"I really like to go everywhere by "
      f"{favourite_transportation_vehicles[1]}, it is good as well!")
print(f"But if I need to go somewhere far, I definitely use "
      f"{favourite_transportation_vehicles[-1]}.")

#3-4
persons = ["Will Smith", "Wim Hoff", "Jaromir Jagr", "David Copperfield"]
print(f"Hello {persons[-1]}, I would like to invite you for a dinner.")

#3-5
persons.remove('Wim Hoff')
persons.append("Sandra Bullock")
print(f"Hi {persons[-1]}, I would like to invite to for a ... dinner yeah!")

#3-6
persons.insert(0, "Cindy Crawford")
persons.insert(-1, "Natalia Imbruglia")
persons.insert(2, "Shannaya Twain")
print(persons)

#3-7
print("Sorry, but in the end, I can invite only two persons for a dinner ...")
print(f"Sorry {persons.pop(0)}, there's no space for yoy for a dinner!")
print(f"Sorry {persons.pop(1)}, there's no space for yoy for a dinner!")
print(f"Sorry {persons.pop(2)}, there's no space for yoy for a dinner!")
print(f"Sorry {persons.pop(-2)}, there's no space for yoy for a dinner!")
print(f"Sorry {persons.pop(-2)}, there's no space for yoy for a dinner!")

print(persons)
print(f"{persons[0]}, you are still invited!")
print(f"{persons[-1]}, you are still invited!")

#3-8
places = ["Bora bora", "Moscow", "Egypt", "Dubai", "Australia"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#3-9
print(len(persons))

#3-10
cities = ["New York", "Paris", "Bratislava", "Valencia", "Osaka"]
print(len(cities))
cities.append("Brisbane")
cities.insert(2, "Prague")
cities.pop(-1)
cities.remove("Paris")
print(list(reversed(cities)))
print(sorted(cities))
cities.sort(reverse=True)
cities.reverse()
print(cities)

#3-11
# print(cities[12])
