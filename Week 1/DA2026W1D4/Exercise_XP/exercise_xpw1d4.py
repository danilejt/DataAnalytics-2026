
# 🌟 Exercise 1: Favorite Numbers
# Key Python Topics:

# Sets
# Adding/removing items in a set
# Set concatenation (using union)


# Instructions:

# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.


from operator import index


my_fav_numbers = {3, 7, 21}
my_fav_numbers.add(42)
my_fav_numbers.add(99)
my_fav_numbers.remove(99)

friend_fav_numbers = {5, 12, 31, 7}

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("All of our favorite numbers are:", our_fav_numbers)


# 🌟 Exercise 2: Tuple
# Key Python Topics:

# Tuples (immutability)


# Instructions:

# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.

my_tuple = (1, 2, 3, 4, 5)
#my_tuple.add(6) # This will raise an AttributeError because tuples do not have an 'add' method.



# 🌟 Exercise 3: List Manipulation
# Key Python Topics:

# Lists
# List methods: append, remove, insert, count, clear


# Instructions:

# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
# Remove "Banana" from the list.
# Remove "Blueberries" from the list.
# Add "Kiwi" to the end of the list.
# Add "Apples" to the beginning of the list.
# Count how many times "Apples" appear in the list.
# Empty the list.
# Print the final state of the list.

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
apples_count = basket.count("Apples")
print("Number of 'Apples' in the list:", apples_count)  
basket.clear()
print("Final state of the list:", basket)

# 🌟 Exercise 4: Floats
# Key Python Topics:

# Lists
# Floats and integers
# Range generation


# Instructions:

# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?

#a float is a number that has a decimal point, while an integer is a whole number without a decimal point.
mixed_list = []
current = 1.5
while current <= 5.0:
    if current.is_integer():
        mixed_list.append(int(current))
    else:
        mixed_list.append(current)
    current += 0.5

print("List of mixed types (floats and integers):", mixed_list)

# 🌟 Exercise 5: For Loop
# Key Python Topics:

# Loops (for)
# Range and indexing


# Instructions:

# Write a for loop to print all numbers from 1 to 20, inclusive.
# Write another for loop that prints every number from 1 to 20 where the index is even.

list_of_numbers = list(range(1, 21))
print("All numbers from 1 to 20:" + str(list_of_numbers))
for number in list_of_numbers:
    if list_of_numbers.index(number) % 2 == 0:
        print(number)
    else: 
        continue   

# 🌟 Exercise 6: While Loop
# Key Python Topics:

# Loops (while)
# Conditionals


# Instructions:

# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop
# Example:

# Alt text


user_name = input("Please enter your name: ")
while True:
    if user_name.isdigit() or len(user_name) < 3:
        user_name = input("Invalid input. Please enter a proper name (at least 3 letters long and not digits): ")
    else:
        print("Thank you!")
        break


# 🌟 Exercise 7: Favorite Fruits
# Key Python Topics:

# Input/output
# Strings and lists
# Conditionals


# Instructions:

# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

favorite_fruits_input = input("Please enter your favorite fruits (separated by spaces): ")
favorite_fruits_list = favorite_fruits_input.split()
print("Your favorite fruits are:", favorite_fruits_list)

# 🌟 Exercise 8: Pizza Toppings
# Key Python Topics:

# Loops
# Lists
# String formatting


# Instructions:

# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.


pizza_topping = input("Please enter pizza toppings one by one (type 'quit' to finish): ")
toppings_list = []
while pizza_topping.lower() != 'quit':
    toppings_list.append(pizza_topping)
    print(f"Adding {pizza_topping} to your pizza.")
    pizza_topping = input("Please enter another pizza topping (type 'quit' to finish): ")
base_price = 10
topping_price = 2.50
total_cost = base_price + (len(toppings_list) * topping_price)
print("Your pizza toppings are:", toppings_list)
print("The total cost of your pizza is: $" + str(total_cost))


# 🌟 Exercise 9: Cinemax Tickets
# Key Python Topics:

# Conditionals
# Lists
# Loops


# Instructions:

# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.


# Bonus:

# Imagine a group of teenagers wants to see a restricted movie (only for ages 16–21).
# Write a program to:
# Ask for each person’s age.
# Remove anyone who isn’t allowed to watch.
# Print the final list of attendees.


