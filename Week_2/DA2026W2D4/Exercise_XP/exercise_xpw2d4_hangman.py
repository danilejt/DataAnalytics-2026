# Mini-Project #2: Python Hangman Project: The objective of our project is to implement the
# hangman game using Python. It doesn’t require any specific modules other than random and time. 
# Python loops and functions are enough to build this game here.

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']

hangman_displays = {
                    0: (
                     "**********",
                     "   ------",
                     "   |     |",
                     "         |",
                     "         |",
                     "         |",
                     "         |",
                     "_________|",
                     "**********"   
                    ),
                    1: ( 
                     "   ------ ",
                     "   |     |",
                     "   O     |",
                     "         |",
                     "         |",
                     "         |",
                     "_________|",
                     "**********"  
                    ),
                    2: (
                     "   ------ ",
                     "   |     |",
                     "   O     |",
                     "   |     |",
                     "         |",
                     "         |",
                     "_________|",
                     "**********"  
                    ),
                    3: (
                    "   ------ ",
                    "   |     |",
                    "   O     |",
                    "  /|     |",
                    "         |",
                    "         |",
                    "_________|",
                    "**********"    
                    ),
                    4: (
                    "   ------ ",
                    "   |     |",
                    "   O     |",
                    "  /|\\    |",
                    "         |",
                    "         |",
                    "_________|",
                    "**********" 
                    ),
                    5: (
                    "   ------ ",
                    "   |     |",
                    "   O     |",
                    "  /|\\    |",
                    "  /      |",
                    "         |",
                    "_________|",
                    "**********" 
                    ),
                    6: (
                    "   ------ ",
                    "   |     |",
                    "   O     |",
                    "  /|\\    |",
                    "  / \\    |",
                    "         |",
                    "_________|",
                    "**********" 
                    ),
                    7: (
                    "   ------ ",
                    "   |     |",
                    "   O     |",
                    "  /|\\    |",
                    "  / \\    |",
                    " d       |",
                    "_________|",
                    "**********" 
                    ),
                    8: (
                    "   ------ ",
                    "   |     |",
                    "   O     |",
                    "  /|\\    |",
                    "  / \\    |",
                    " d   b   |",
                    "_________|",
                    "**********" 
                   )
}

def show_picture(num_of_wrong_guesses):
    for picture in hangman_displays[num_of_wrong_guesses]:
        print(picture)
    pass

def show_word_so_far(word_so_far):
    print(" ".join(word_so_far))

def show_final_answer(word):
    print("".join(word))


def main():
    word = random.choice(wordslist) 
    word_so_far = ["_"]*len(word)
    num_of_wrong_guesses = 0
    guessed_letters = set()
    game_is_running = True
    
    while game_is_running:
        show_picture(num_of_wrong_guesses)      
        show_word_so_far(word_so_far) 
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1: 
            print("You can only type one letter at a time. Try again.")
            continue
                
        if not guess.isalpha():
            print("You can't type numbers; you can only type letters. Try again.")
            continue   

        if guess in guessed_letters:
            print(f"You have already guessed the letter {guess}. Try something new!")
            continue 

        guessed_letters.add(guess) 

        if guess in word:
            for index in range (len(word)):
                if word[index] == guess:
                    word_so_far[index] = guess;
        else:
           num_of_wrong_guesses = num_of_wrong_guesses + 1
                            
        if "_" not in word_so_far:
            show_picture(num_of_wrong_guesses)
            show_final_answer(word)
            print("You won...time to go outside :)")
            game_is_running = False;
        elif num_of_wrong_guesses >= len(hangman_displays) -1:
            show_picture(num_of_wrong_guesses)
            show_final_answer(f"The word was {word}")
            game_is_running = False;
            

if __name__ == "__main__":
    main()