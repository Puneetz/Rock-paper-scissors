import random
computerScore = 0
p1Score = 0

def menu ():
    optionss = ["rock","paper","scissors"]
    options = random.choice(optionss)
    game = False
    global p1Score
    global computerScore
    print("Welcome to game") #rock paper scissors
    p1=input("choose from rock, paper and scissors: ")

    while game == False:
        if p1 == "rock" and options == "rock":
            print("Computer picked:",options)
            print("DRAW")
            print("Computer Score:",computerScore,"\nYour Score:",p1Score)
            ask()
        elif p1 == "rock" and options == "paper":
            print("Computer picked:",options)
            print("Computer Wins!")
            computerScore = computerScore + 1
            print("Computer Score:",computerScore,"\nYour Score:",p1Score)
            ask()
        elif p1 == "rock" and options == "scissors":
            print("Computer picked:",options)
            print("You Win!")
            p1Score = p1Score + 1
            print("Computer Score:",computerScore,"\nYour Score:",p1Score)
            ask()
        elif p1 == "scissors" and options == "scissors":
            print("Computer picked:",options)
            print("DRAW")
            print("Computer Score:",computerScore,"\nYour Score:",p1Score)
            ask()
        elif p1 == "scissors" and options == "paper":
            print("Computer picked:",options)
            print("You Win!")
            p1Score = p1Score + 1
            print("Computer Score:",computerScore,"\nYour Score:",p1Score)
            ask()
        elif p1 == "scissors" and options == "rock":
            print("Computer picked:",options)
            print("Computer Wins!")
            computerScore = computerScore + 1
            print("Computer Score:",computerScore,"\nYour Score:",p1Score)
            ask()
        elif p1 == "paper" and options == "paper":
            print("Computer picked:",options)
            print("DRAW")
            print("Computer Score:",computerScore,"\nYour Score:",p1Score)
            ask()
        elif p1 == "paper" and options == "scissors":
            print("Computer picked:",options)
            print("Computer Wins!")
            computerScore = computerScore+ 1
            print("Computer Score:",computerScore,"\nYour Score:",p1Score)
            ask()
        elif p1 == "paper" and options == "rock":
            print("Computer picked:",options)
            print("You Win!")
            p1Score = p1Score + 1
            print("Computer Score:",computerScore,"\nYour Score:",p1Score)
            ask()
        else:
            print("Invalid input")
            menu()

def ask():
    global p1Score
    global computerScore

    again = False
    if computerScore == 5:
        print("Computer Wins the game!")
        exit()
    if p1Score == 5:
        print("You Win the game!")
        exit()
    playAgain = input("Would you like to play again? (y or n): ")
    while again == False:
        if playAgain == "y":
            menu()
        elif playAgain == "n":
            print("Thank you, see you again soon!")
            exit()
        else:
            print("Invalid Input")
            ask()

menu()
