

# Instructions:

# You are given a “Matrix” string:



MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''       


# This represents a grid of characters, and your task is to decode the hidden message within.



# Understanding the Matrix:

# Imagine this string arranged in rows and columns, forming a grid.
# To work with it in Python, you’ll need to transform this string into a 2D list (a list of lists), where each inner list represents a row.


# Step 1: Transforming the String into a 2D List

matrix = [list(row) for row in MATRIX_STR.strip().split('\n')]
print(matrix)  # Print the 2D list to verify the transformation

# Step 2: Processing Columns

# Neo reads the matrix column by column, from top to bottom, starting from the leftmost column.
for column in range(len(matrix[0])):
    for row in matrix:
        print(row[column], end='')  # Print characters column by column
    print()  # New line after each column

# You’ll need to write code that iterates through the columns of your 2D list.
# Think about how you can access the elements of a 2D list by column.


# Step 3: Filtering Alpha Characters
for column in range(len(matrix[0])):
    temp_string = ""
    for row in matrix:
        char = row[column]
        if char.isalpha():  # Check if the character is an alphabet letter
            temp_string += char
    print(temp_string)  # Print the filtered alpha characters for each column

# only select alpha characters (letters).
# For each character in a column, check if it’s an alpha character.
# If it is, add it to a temporary string.
# Think about how you can check if a character is an alphabet letter.


# Replace every group of symbols (non-alpha characters) between two alpha characters with a space.


# After you have gathered the alpha characters, you will need to iterate through them, and where there are non alpha characters between them, you will insert a space.
# Think about how you can keep track of when you encounter an alphabet character, and when you encounter a non alphabet character.

for column in range(len(matrix[0])):
    temp_string = ""
    for row in matrix:
        char = row[column]
        if char.isalpha():
            temp_string += char
        else:
            if temp_string and not temp_string.endswith(' '):
                temp_string += ' '  # Add a space if the last character is not already a space
    print(temp_string.strip())  # Print the filtered and processed string for each column

# Step 5: Constructing the Secret Message

# Combine the filtered and processed characters to form the decoded message.
# Print the decoded message.



