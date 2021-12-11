"""Chapter 10 - Files and Exceptions"""

"""
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by 
storing the lines in a list and then working with them outside the with block.
"""
print("\n/// 10-1")

with open("chapter10_learning_python.txt", "r") as f:
    print()
    print(f.read())

with open("chapter10_learning_python.txt", "r") as f:
    print()
    for line in f:
        print(line, end="")

with open("chapter10_learning_python.txt", "r") as f:
    lines = []
    for line in f.readlines():
        lines.append(line)

print("\n")
for line in lines:
    print(line, end="")

"""
10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""
print("\n/// 10-2")

with open("chapter10_learning_python.txt", "r") as f:
    content = f.read()
    print(content.replace("python", "C"))

"""
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
"""
print("\n/// 10-3")

with open("chapter10_guests.txt", "a") as f:
    name = input("Dear guest, tell me your name (q for quit): ")
    f.write(name)

"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""
print("\n/// 10-4")
with open("chapter10_guest_book.txt", "a") as f:
    while True:
        name = input("Dear guest, tell me your name (q for quit): ")
        if name == 'q':
            break
        else:
            print(f"Hello {name} my friend, welcome!")
            f.write(f"{name}\n")

"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""
print("\n/// 10-5")

with open("chapter10_programming_poll.csv", "a") as f:
    f.write("Reason why I like programming\n")
    while True:
        reason = input("Why do you like programing? (q for quit): ")
        if reason == 'q':
            break
        else:
            f.write(f"{reason}\n")

"""
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
"""
print("\n/// 10-6")

num1 = input("Please provide first number: ")
num2 = input("Please provide second number: ")

try:
    print(int(num1) + int(num2))
except ValueError:
    print("One or both of your entries is not a number!")
finally:
    print("Thank you for participate.")

"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number.
"""
print("\n/// 10-7")

while True:
    num1 = input("Please provide first number: ")
    num2 = input("Please provide second number: ")

    try:
        print(int(num1) + int(num2))
        break
    except ValueError:
        print("One or both of your entries is not a number! Please try again.")
    finally:
        print("Thank you for participate.")

"""
10-8. Cats and Dogs: Make two files, chapter10_cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a 
different location on your system, and make sure the code in the except block
executes properly
"""
print("\n/// 10-8")

for file in ["chapter10_cats.txt", "chapter10_dogs2.txt"]:
    try:
        with open(file, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"I cannot find the file {file}, sorry ...")
    finally:
        print(f"The reading of file {file} is over.")

"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""
print("\n/// 10-9")

for file in ["chapter10_cats.txt", "chapter10_dogs2.txt"]:
    try:
        with open(file, "r") as f:
            print(f.read())
    except FileNotFoundError:
        pass

print(f"The reading of files is over.")

"""
10-10. Common Words: Visit Project Gutenberg (https://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text. This will be
an approximation because it will also count words such as 'then' and 'there'.
Try counting 'the ', with a space in the string, and see how much lower your
count is.
"""
print("\n/// 10-10")

with open("chapter10_text_to_analyze.txt", "r", encoding="utf8") as f:
    text = f.read()
    word_to_search = " the "
    count = text.lower().count(word_to_search)
    print(f"The word '{word_to_search}' is present {count}-times in the text.")

"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate 
program that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
"""
print("\n/// 10-11")
import json

favorite_number = input("What is your favorite number? ")

filename = "chapter10_fav_num.json"
with open(filename, "w") as f:
    json.dump(favorite_number, f)

with open(filename, "r") as f:
    number = json.load(f)
    print(f"Your favorite number is {number}!")

"""
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works.
"""
print("\n/// 10-12")

filename = "chapter10_fav_num2.json"


def set_number(num):
    with open(filename, "w") as f:
        json.dump(num, f)


def get_number():
    try:
        with open(filename, "r") as f:
            num = json.load(f)
        return num
    except FileNotFoundError:
        return False


def reveal_number():
    num = get_number()
    if num:
        print(f"Hi, your favorite number is {num}!")
    else:
        num = input("Hi, what is your favorite number? ")
        set_number(num)
        print("Your favorite number will be remembered now!")

reveal_number()
reveal_number()

"""
10-13. Verify User: The final listing for remember_me.py assumes either that the
user has already entered their username or that the program is running for the
first time. We should modify it in case the current user is not the person who
last used the program.
Before printing a welcome back message in greet_user(), ask the user if
this is the correct username. If it’s not, call get_new_username() to get the correct
username.
"""
print("\n/// 10-12")


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
        return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        verify_user = input(f"Is this really you {username}? (y/n) ")
        if verify_user == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            remembering_call(username)
    else:
        username = get_new_username()
        remembering_call(username)


def remembering_call(username):
    """Print remembering call"""
    print(f"We'll remember you when you come back, {username}!")


greet_user()
greet_user()
greet_user()
