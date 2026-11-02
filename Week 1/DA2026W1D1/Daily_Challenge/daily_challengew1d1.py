# Instructions:
# 1. Ask for User Input:

input_string = input("Please enter a string that is exactly 10 characters long: ")

# The string must be exactly 10 characters long.
# If the string is less than 10 characters, print: "String not long enough."
# If the string is more than 10 characters, print: "String too long."
# If the string is exactly 10 characters, print: "Perfect string" and proceed to the next steps.
# 2. Check the Length of the String:

#need to fix this so that it reverts back to the input prompt if the string is not exactly 10 characters long.

input_string = input("Please enter a string that is exactly 10 characters long: ")

while len(input_string) != 10:
    if len(input_string) < 10:
        print("String not long enough.")
    else:
        print("String too long.")
    input_string = input("Please enter a string that is exactly 10 characters long: ")

print("Perfect string.")

# 3. Print the First and Last Characters:
# Once the string is validated, print the first and last characters.

first_char = input_string[0]
last_char = input_string[-1]
print(f"First character: {first_char}")
print(f"Last character: {last_char}")

#     # 4. Build the String Character by Character:
print("Building the string character by character:")
for i in range(1, 11):
        print(input_string[:i])


#     # 5. Bonus: Jumble the String (Optional)
import random
jumbled_list = list(input_string)
random.shuffle(jumbled_list)
jumbled_string = ''.join(jumbled_list)
print(f"Jumbled string: {jumbled_string}")

