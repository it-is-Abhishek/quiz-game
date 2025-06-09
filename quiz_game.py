"""
Quiz Game Project
-----------------
A simple interactive quiz game with multiple question types and scoring system.
"""

def main():
    print("Welcome to my Quiz Game!")
    print("------------------------")

if __name__ == "__main__":
    main()

import time

def display_welcome():
    print("\n"*50)
    print("****************************************************")
    print("*                                                   *")
    print("*           WELCOME TO THE QUIZ GAME!              *")
    print("*                                                   *")
    print("****************************************************")
    print("\n")

    print("Test your knowledge and win!")
    print("Here's how to play:")
    print("- You will be presented with multiple-choice questions")
    print("- Choose your answer by entering the corresponding number")
    print("- The game will keep track of your score")
    print("- You can play as many rounds as you want\n")

    user_name = input("please enter your name: ")

    print(f"\nWelcome {user_name}, let's get ready to begin!")
    time.sleep(3)

    print("\n"*50)

display_welcome()