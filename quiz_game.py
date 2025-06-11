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


play_game = True
while play_game:
    current_score  = 0
    current_question = 0

    for question in questions:
        display_question(question)

        user_ans = input("Please enter your answer (or type 'quit' to exit): ")
        if user_ans.lower() == "quit":
            play_game = False
            break

        current_score, feedback = check_ans(question, username, current_score)

        print(feedback)
        current_question += 1
    
    if play_game:
        print(f"\nRound completed! Your final score is {current_score}")
        play_again = input("would you like to play again? (yes/no):")
        
        if play_game.lower() != "yes":
            play_game = Flase

print("Thankyou for playing!")


score = 0
current_question = 0
total_question = len(questions)


questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct": 0
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Saturn"],
        "correct": 1
    }
]

while game_activities():