"""Chapter 09 - Classes"""

"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message 
indicating that the restaurant is open. Make an instance called restaurant from 
your class. Print the two attributes individually, and then call both methods.
"""
print("\n/// 9-1")


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This {self.restaurant_name} is a {self.cuisine_type} place")

    @staticmethod
    def open_restaurant():
        print("The restaurant is opened!")


my_restaurant = Restaurant("Juksuu", "whole-food, plant-based")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""
print("\n/// 9-2")
your_restaurant = Restaurant("Balans Bistro", "vegan")
their_restaurant = Restaurant("Organilla Food", "vegan/vegetarian")

my_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
their_restaurant.describe_restaurant()

"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""
print("\n/// 9-3")


class User:

    def __init__(self, first_name, last_name, age, status, active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status
        self.active = active

    def describe_user(self):
        print("User information: ")
        print(f"\t- {self.first_name}")
        print(f"\t- {self.last_name}")
        print(f"\t- {self.age}")
        print(f"\t- {self.status}")
        print(f"\t- {self.active}")

    def greet_user(self):
        print(f"Hello my dear {self.first_name}! How are you today?")


user1 = User("John", "Smith", 37, "free")
user2 = User("Joe", "Doe", 25, "married", False)
user3 = User("Helen", "Right", 22, "single")
usr_lst = user1, user2, user3

for user in usr_lst:
    user.describe_user()
    user.greet_user()

"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number 
you like that could represent how many customers were served in, say, a day 
of business.
"""
print("\n/// 9-4")


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_serverd=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_serverd

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, increment):
        self.number_served += increment

    def describe_restaurant(self):
        print(f"This {self.restaurant_name} is a {self.cuisine_type} place")

    @staticmethod
    def open_restaurant():
        print("The restaurant is opened!")


restaurant = Restaurant("Juksuu", "WFPB", 27)
print(restaurant.number_served)
restaurant.number_served = 39
print(restaurant.number_served)
restaurant.set_number_served(92)
print(restaurant.number_served)
restaurant.increment_number_served(2)
print(restaurant.number_served)

"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 162). Write a method called increment_login
_attempts() that increments the value of login_attempts by 1. Write another
method called reset_login_attempts() that resets the value of login_attempts
to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""
print("\n/// 9-5")


class User:

    def __init__(self, first_name, last_name, age, status, active=True):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.status = status
        self.active = active
        self.logging_attempts = 1

    def increment_login_attempts(self):
        self.logging_attempts += 1

    def reset_login_attempts(self):
        self.logging_attempts = 0

    def describe_user(self):
        print("User information: ")
        print(f"\t- {self.first_name}")
        print(f"\t- {self.last_name}")
        print(f"\t- {self.age}")
        print(f"\t- {self.status}")
        print(f"\t- {self.active}")

    def greet_user(self):
        print(f"Hello my dear {self.first_name}! How are you today?")


user = User("John", "Smith", "38", "single")
print(user.logging_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.logging_attempts)
user.reset_login_attempts()
print(user.logging_attempts)


print("\n/// 9-1")
print("\n/// 9-1")
print("\n/// 9-1")
print("\n/// 9-1")
print("\n/// 9-1")
print("\n/// 9-1")
print("\n/// 9-1")
