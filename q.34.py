print("Welcome to the Jungle Adventure!")

choice1 = input("Do you want to go 'left' or 'right'? ").strip().lower()

if choice1 == "right":
    print("Game Over")
elif choice1 == "left":
    choice2 = input("Do you want to 'climb a tree' or 'explore the cave'? ").strip().lower()
    
    if choice2 == "climb a tree":
        print("Game Over")
    elif choice2 == "explore the cave":
        choice3 = input("Choose between 'bear', 'tiger', or 'snake': ").strip().lower()
        
        if choice3 == "bear" or choice3 == "tiger":
            print("Game Over")
        elif choice3 == "snake":
            print("You Win! Congratulations!")
        else:
            print("Invalid choice. Game Over")
    else:
        print("Invalid choice. Game Over")