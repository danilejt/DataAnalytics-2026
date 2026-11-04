# 👩‍🏫 👩🏿‍🏫 What You’ll learn
# Python Basics
# Dictionaries
# Conditionals
# Loops


# Challenge 1: Letter Index Dictionary
# Goal: Create a dictionary that stores the indices (number of the position) of each letter in a word provided by the user(input()).



# Key Python Topics:

# User input (input())
# Dictionaries
# Loops (for loop)
# Conditional statements (if, else)
# String manipulation
# Lists


# Instructions:
# 1. User Input:
# Ask the user to enter a word.
# Store the input word in a variable.


# 2. Creating the Dictionary:
# Iterate through each character of the input word using a loop.
# And check if the character is already a key in the dictionary.


input_word = input("Please enter a word: ")
dict_characters_to_indices = {}

index = 0

for character in input_word:
    if character not in dict_characters_to_indices:
        # Create a new list with the current index
        dict_characters_to_indices[character] = [index]
    else:
        # Append the current index to the existing list
        dict_characters_to_indices[character].append(index)
    index += 1

print(dict_characters_to_indices)

#     * If it is, append the current index to the list associated with that key.
#     * If it is not, create a new key-value pair in the dictionary.
# Ensure that the characters (keys) are strings.
# Ensure that the indices (values) are stored in lists.
# 3. Expected Output:

# For the input “dodo”, the output should be: {"d": [0, 2], "o": [1, 3]}.
# For the input “froggy”, the output should be: {"f": [0], "r": [1], "o": [2], "g": [3, 4], "y": [5]}.
# For the input “grapes”, the output should be: {"g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5]}.


# Challenge 2: Affordable Items
# Goal: Create a program that prints a list of items that can be purchased with a given amount of money.



# Key Python Topics:

# Dictionaries
# Loops (for loop)
# Conditional statements (if, else)
# String manipulation (replace())
# Type conversion (int())
# Lists
# Sorting (sorted())


# Instructions:
# 1. Store Data:
# You will be provided with a dictionary (items_purchase) where the keys are the item names
#  and the values are their prices (as strings with a dollar sign). 
# The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
# You will also be given a string (wallet) representing the amount of money you have.

items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"

# 2. Data Cleaning:
wallet_amount = int(wallet.replace("$", "").replace(",", ""))

# You need to clean the dollar sign and the commas using python. Don’t hard code it.
for item, price in items_purchase.items():
    # Remove the dollar sign and commas from the price string
    cleaned_price = price.replace("$", "").replace(",", "")
    # Convert the cleaned price string to an integer
    items_purchase[item] = int(cleaned_price)

# 3. Determining Affordable Items:

basket = []
for item in items_purchase:
    item_price = items_purchase[item]

    if wallet_amount >= item_price:
        basket.append(item)
        wallet_amount = wallet_amount - item_price

if not basket:
        print("Nothing.")
else:
        basket.sort()
        print(basket)

print("Final state of the list:", basket)

# create a list called basket and add there the items that you can buy with the money you have on the wallet
# Don’t forget to update the wallet after buying an item.
# If the basket is empty (no items can be afforded), return the string “Nothing”.
# Otherwise, print the basket list in alphabetical order.
# 4. Examples:

# Given:
# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"


# The output should be: ["Bread", "Fertilizer", "Water"].

# Given:
# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"


# The output should be: ["Apple", "Bananas", "Fan", "Honey", "Spoon"].

# Given:
# items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
# wallet = "$1"


# The output should be: "Nothing".

