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

"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
"""
print("\n/// 9-6")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, number_serverd=0):
        super().__init__(restaurant_name, cuisine_type, number_serverd)
        self.flavors = ["banana", "lemon", "chocolate"]

    def display_flavors(self):
        print("This ice cream stand offers following flavors: ")
        for flavor in self.flavors:
            print(f"\t - {flavor}")


ic_stand = IceCreamStand("IC for yoy", "ice cream")
ic_stand.display_flavors()

"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""
print("\n/// 9-7")


class Admin(User):

    def __init__(self, first_name, last_name, age, status, active=True):
        super().__init__(first_name, last_name, age, status, active=True)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator privileges: ")
        for privilege in self.privileges:
            print(f"\t- {privilege}")


admin1 = Admin("John", "Smith", 60, "occupied")
admin1.show_privileges()

"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""
print("\n/// 9-8")


class Admin2(User):

    def __init__(self, first_name, last_name, age, status, active=True):
        super().__init__(first_name, last_name, age, status, active=True)
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Administrator2 privileges: ")
        for privilege in self.privileges:
            print(f"\t- {privilege}")


admin2 = Admin2("John", "Smith", 60, "occupied")
admin2.privileges.show_privileges()

"""
9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 100 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.
"""
print("\n/// 9-9")


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
         self.make = make
         self.model = model
         self.year = year
         self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size <= 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 0

        print(f"This car can go about {range} miles on a full charge.")


electric_car = ElectricCar("Tesla", "Hybrid", 2021)
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()

"""
9-10. Imported Restaurant: Using your latest Restaurant class, store it in a 
module. Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is 
working properly.
"""
print("\n/// 9-10")

from chapter09_restaurant import Restaurant as ImportedRestaurant

new_restaurant = ImportedRestaurant("Vegan Bistro", "plant based")
new_restaurant.describe_restaurant()

"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173).
Store the classes User, Privileges, and Admin in one module. Create a separate 
file, make an Admin instance, and call show_privileges() to show that 
everything is working correctly.
"""
print("\n/// 9-11")

from chapter09_user import Admin as AdminImported

new_admin = AdminImported("Anette", "Tester", 29, "single")
new_admin.privileges.show_privileges()

"""
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""
print("\n/// 9-12")
from chapter09_admin_privilege_separate import Admin as AdminSeparate

new_admin_separate = AdminSeparate("Julia", "Roberts", 41, "nice")
new_admin_separate.privileges.show_privileges() # from Privilege class
new_admin_separate.describe_user() # from User (base) class

"""
9-13. Dice: Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll it
10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times
"""
print("\n/// 9-13")




print("\n/// 9-1")
print("\n/// 9-1")
print("\n/// 9-1")