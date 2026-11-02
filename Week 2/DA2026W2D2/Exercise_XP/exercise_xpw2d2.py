# 🌟 Exercise 1: What Are You Learning?
# Goal: Create a function that displays a message about what you’re learning.

# Key Python Topics:

# Functions (defining and calling)
# print() function


# Step 1: Define a Function

# Define a function named display_message().
# This function should not take any parameters.

def display_message():
    print("I am learning about functions in Python.")

display_message()  # Call the function to display the message
# Step 2: Print a Message

# For example: “I am learning about functions in Python.”


# Step 3: Call the Function

# This will execute the code inside the function and print your message.


# Expected Output:

# I am learning about functions in Python.

# 🌟 Exercise 2: What’s Your Favorite Book?
# Goal: Create a function that displays a message about a favorite book.

# Key Python Topics:

# Functions with parameters
# String concatenation or f-strings
# Calling functions with arguments


# Step 1: Define a Function with a Parameter

# Define a function named favorite_book().
# This function should accept one parameter called title.

def favorite_book(title):
    print(f"One of my favorite books is {title}.")


favorite_book("Alice in Wonderland")  # Call the function with a book title
# Step 2: Print a Message with the Title

# The function needs to output a message like “One of my favorite books is <title>”.



# Step 3: Call the Function with an Argument

# Call the favorite_book() function and provide a book title as an argument.
# For example: favorite_book("Alice in Wonderland").


# Expected Output:

# One of my favorite books is Alice in Wonderland.

# 🌟 Exercise 3: Some Geography
# Goal: Create a function that describes a city and its country.

# Key Python Topics:

# Functions with multiple parameters
# Default parameter values
# String formatting



# Step 1: Define a Function with Parameters

# Define a function named describe_city().
# This function should accept two parameters: city and country.
# Give the country parameter a default value, such as “Unknown”.

def describe_city(city, country = "Unknown"):
    print(f"{city} is in {country}.")


describe_city("Jerusalem", "Israel")
describe_city("Paris")
# Step 2: Print a Message

# Inside the function, set up the code to display a sentence like <city> is in <country>.
# Replace <city> and <country> with the parameter values.


# Step 3: Call the Function

# Call the describe_city() function with different city and country combinations.
# Try calling it with and without providing the country argument to see the default value in action.
# Example: describe_city("Reykjavik", "Iceland") and describe_city("Paris").


# Expected Output:

# Reykjavik is in Iceland.
# Paris is in Unknown.


# Exercise 4: Random
# Goal: Create a function that generates random numbers and compares them.

# Key Python Topics:

# random module
# random.randint() function
# Conditional statements (if, else)






# Step 1: Import the random Module

# At the beginning of your script, use import random to access the random number generation functions.
import random

# Step 2: Define a Function with a Parameter

# Create a function that accepts a number between 1 and 100 as a parameter.
def compare_random_number(number):
    if not (1 <= number <= 100):
        raise ValueError("The limit must be an integer between 1 and 100.")
    random_number = random.randint(1, 100)
    if number == random_number:
        print("Success! The numbers match.")
    else:
        print(f"Fail! Your number: {number} is not the same as the random number: {random_number}")
# Step 3: Generate a Random Number

# Inside the function, use random.randint(1, 100) to generate a random integer between 1 and 100.

compare_random_number(50)  # Call the function with a number between 1 and 100
# Step 4: Compare the Numbers

# If they are the same, print a success message. Otherwise, print a fail message and display both numbers.


# Step 5: Call the Function

# Call the function with a number between 1 and 100.


# Expected Output:

# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)


# 🌟 Exercise 5: Let’s Create Some Personalized Shirts!
# Goal: Create a function to describe a shirt’s size and message, with default values.

# Key Python Topics:

# Functions with parameters and default values
# Keyword arguments


# Step 1: Define a Function with Parameters

# Define a function called make_shirt().
# This function should accept two parameters: size and text.

def make_shirt(size = "large", text = "I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")



make_shirt("large", "I love Python");
make_shirt("large")
make_shirt("medium")
make_shirt(text = "Custom message")  # Call the function with size and text

# Call make_shirt() to make a shirt of any size with a different message.


# Step 6 (Bonus): Keyword Arguments

# Call make_shirt() using keyword arguments (e.g., make_shirt(size="small", text="Hello!")).


# Expected Output:

# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.


# 🌟 Exercise 6: Magicians…
# Goal: Modify a list of magician names and display them in different ways.

# Key Python Topics:

# Lists
# for loops
# Modifying lists
# Functions that modify data structures


# Step 1: Create a List of Magician Names

# Create a list called magician_names with the given names:
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


# Step 2: Create a Function to Display Magicians

# Create a function called show_magicians() that takes the magician_names list as a parameter.
# Inside the function, iterate through the list and print each magician’s name.

def show_magicians(magicians_names):
    for magician in magicians_names:
        print(magician)


# Step 3: Create a Function to Modify the List
def make_great(magicians_names):
    for magician in range(len(magicians_names)):
        magicians_names[magician] = " the Great " + magicians_names[magician]
# Create a function called make_great() that takes the magician_names list as a parameter.
# Inside the function, use a for loop to iterate through the list and add “the Great” before each magician’s name.

make_great(magician_names)  # Call the function to modify the list
show_magicians(magician_names)  # Call the function to display the modified list
# Step 4: Call the Functions

# Call make_great() to modify the list.
# Call show_magicians() to display the modified list.


# Expected Output:

# Harry Houdini the Great
# David Blaine the Great
# Criss Angel the Great


# Here’s the updated format for Exercise 7: Temperature Advice to match the style of Exercise 6: Magicians:



# 🌟 Exercise 7: Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.

# Key Python Topics:

# Functions
# Conditionals (if / elif)
# Random numbers
# Floating-point numbers (Bonus)
# Handling seasons (Bonus)


# Step 1: Create the get_random_temp() Function

# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.

def get_random_temp():
    return random.randint(-10, 40)  # Return a random integer between -10 and 40
# Step 2: Create the main() Function

# Create a function called main(). Inside this function:
def main():
    temp = get_random_temp()  # Call get_random_temp() to get a random temperature
    print(f"The temperature right now is {temp} degrees Celsius.")  # Print the temperature

    # Provide advice based on the temperature
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("Nice weather.")
    elif 24 <= temp < 32:
        print("A bit warm, stay hydrated.")
    elif 32 <= temp < 40:
        print("It’s really hot! Stay cool.")
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”
# Step 3: Provide Temperature-Based Advice

# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”


# Step 4: Floating-Point Temperatures (Bonus)

# Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.
def get_random_temp_float():
    return random.uniform(-10, 40)  # Return a random floating-point number between -10 and 40

def main2():
    temp = get_random_temp_float()  # Call get_random_temp_float() to get a random temperature
    print(f"The temperature right now is {temp} degrees Celsius.")  # Print the temperature

    # Provide advice based on the temperature
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("Nice weather.")
    elif 24 <= temp < 32:
        print("A bit warm, stay hydrated.")
    elif 32 <= temp < 40:
        print("It’s really hot! Stay cool.")

# Step 5: Month-Based Seasons (Bonus)

# Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
# Modify get_random_temp() to return temperatures specific to each season.

month = int(input("Enter the month (1-12): "))

def main3():
    if month in [12, 1, 2]:  # Winter
        temp = random.randint(-10, 10)
    elif month in [3, 4, 5]:  # Spring
        temp = random.randint(10, 20)
    elif month in [6, 7, 8]:  # Summer
        temp = random.randint(20, 35)
    elif month in [9, 10, 11]:  # Autumn
        temp = random.randint(10, 25)
    else:
        print("Invalid month. Please enter a number between 1 and 12.")
        return
    # Provide advice based on the temperature
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat.")
    elif 16 <= temp < 23:
        print("Nice weather.")
    elif 24 <= temp < 32:
        print("A bit warm, stay hydrated.")
    elif 32 <= temp < 40:
        print("It’s really hot! Stay cool.")

main3()


# Expected Output:

# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.


