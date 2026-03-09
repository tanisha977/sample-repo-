print("Welcome to the Adventure Game!")

name = input("Enter your name: ")
print("Hello", name, "your mission is to find the hidden treasure!")

choice1 = input("You are at a cross road. Go 'left' or 'right'? ").lower()

if choice1 == "left":
    choice2 = input("You reach a river. Do you 'swim' or 'wait' for a boat? ").lower()
    
    if choice2 == "wait":
        choice3 = input("A boat arrives and takes you to an island. There are 3 doors: red, blue, yellow. Which one do you choose? ").lower()
        
        if choice3 == "yellow":
            print("🏆 Congratulations! You found the treasure!")
        elif choice3 == "red":
            print("🔥 Room full of fire. Game Over.")
        elif choice3 == "blue":
            print("🐍 Snakes everywhere. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    
    else:
        print("🌊 You were attacked by crocodiles. Game Over.")

else:
    print("🐻 A wild bear attacked you. Game Over.")

print("Thanks for playing!")