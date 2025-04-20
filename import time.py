import time

def strategy_game():
    print("Welcome to the Strategy Choice Game!")
    time.sleep(1)
    print("You are a leader making choices to survive and thrive.")
    time.sleep(2)
    
    choice1 = input("A disaster is coming! Do you (1) Gather resources or (2) Build defenses? Enter 1 or 2: ")
    
    if choice1 == "1":
        print("You gather resources, but your defenses are weak!")
        time.sleep(2)
        choice2 = input("The enemy is approaching! Do you (1) Negotiate or (2) Fight? Enter 1 or 2: ")
        if choice2 == "1":
            print("You successfully negotiate peace! You win!")
        else:
            print("You fight bravely, but without defenses, you lose!")
    elif choice1 == "2":
        print("You build strong defenses, but food is running out!")
        time.sleep(2)
        choice2 = input("Do you (1) Trade for food or (2) Ration supplies? Enter 1 or 2: ")
        if choice2 == "1":
            print("You secure food and survive! You win!")
        else:
            print("Your people starve, and you lose!")
    else:
        print("Invalid choice! You hesitated and lost the game!")

strategy_game()
