# 5-1
car = 'subaru'
print("Is car == 'subraru'? I predict True.")
print(car == 'subaru')

print("\nIs car 'audi'? I predict False.")
print(car == 'audi')

print(f"subaru is not subraru: {car != 'subaru'}")
print(f"subaru is not audi: {car != 'audi'}")

# 5-2
car = 'kia'
print('Kia'.lower() == car)
print(len(car) == 3)
print(len(car) > 2)
print(len(car) < 4)
print(len(car) < 4 and len(car) > 2)
print(len(car) > 2 or len(car) < 2)

cars = ['audi', 'subaru', 'skoda']
print(car in cars)
print(car not in cars)

# 5-3
alien_color = 'green'
if alien_color == 'green':
    print("You have just earned 5 points!")

# 5-4
alien_color = 'red'
if alien_color == 'green':
    print("You have just earned 5 points!")
else:
    print("You have earned nothing ...")

# 5-5
# alien_color = 'green'
# alien_color = 'yellow'
alien_color = 'red'

if alien_color == 'green':
    print("You have just earned 5 points!")
elif alien_color == 'yellow':
    print("You have just earned 10 points!")
elif alien_color == 'red':
    print("You have just earned 15 points!")

# 5-6
age = 37
if age < 2:
    print("This person is just a baby!")
elif 2 <= age < 4:
    print("This person is a toddler.")
elif 4 <= age < 13:
    print("This person is a kid..")
elif 13 <= age < 20:
    print("This person is a teenager.")
elif 20 <= age < 65:
    print("This person is an adult")
elif age >= 65:
    print("This person is an elder.")

# 5-7
favourite_fruits = ['melon', 'peach', 'pineapple']
if 'melon' in favourite_fruits:
    print("You like melons!")
if 'peach' in favourite_fruits:
    print("You like peach!")
if 'apple' in favourite_fruits:
    print("You like apples!")
if 'pineapple' in favourite_fruits:
    print("You like pineapples!")
if 'banana' in favourite_fruits:
    print("You like bananas!")

# 5-8
users = ['manager', 'employee', 'admin', 'ba', 'watcher']
# users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging again.")
else:
    print("We need to find some users!")

# 5-10
current_users = users[:]
new_users = current_users[:]
current_users_upper = [user.upper() for user in current_users]
new_users.remove("manager")
new_users.remove("admin")
new_users.insert(1, "teacher")
new_users.insert(2, "student")

print(new_users)
print(current_users_upper)
for username in new_users:
    if username.upper() not in current_users_upper:
        print(f"The {username} username is available.")
    else:
        print(f"The {username} is not available. Please choose different"
              f" username.")
# 5-11
ordinal_numbers = [num for num in range(1, 10)]
for number in ordinal_numbers:
    if number > 3:
        print(f"{number}th")
    elif number == 3:
        print(f"{number}rd")
    elif number == 2:
        print(f"{number}nd")
    elif number == 1:
        print(f"{number}st")



