import random

def hang_man(word):
    num_tries = len(word)
    print(f"Tries left: {num_tries}")
    print("-" * 8)
    print("|      |")
    for _ in range(4):
        print("|")
    print("_")

    num_of_tries = len(word)
    i = 0
    hangman_parts = [
        """
        --------
        |      |
        |
        |
        |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |
        |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |      |
        |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|
        |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |
        -
        """,
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        -
        """
    ]

    guessed_letters = ["_"] * len(word)

    while i < num_of_tries:
        user_input = input("Enter a letter: ")

        if user_input in word:
            for index, letter in enumerate(word):
                if letter == user_input:
                    guessed_letters[index] = user_input
            print("Good guess!")
        else:
            print(hangman_parts[i])
            i += 1

        num_tries -= 1
        print(f"Tries left: {num_tries}")
        print(" ".join(guessed_letters)) 
        print("_")

        
        if "_" not in guessed_letters:
            print("Congratulations! You guessed the word correctly!")
            return

    print("You lost!") 

word_list = ["python", "hangman", "game", "great", "babel"]  

random_word = random.choice(word_list) 

hang_man(random_word)

#compare the user input to the condition
# if the user input is equal to the condition then we don't print anything to to the terminal 
# else if the answer is not a match then we print a part of the hangman
# if the user guesses the word before the max attempts are exausted then we print you win!
# else we print you lost!
