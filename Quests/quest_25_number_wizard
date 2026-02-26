# Quest 25: The Number Wizard

import random  

secret_number = random.randint(1, 20)  


print("🔮 Welcome, adventurer! I am the Number Wizard.")
print("I have chosen a number between 1 and 20.")
print("Can you guess it?")


while True:
    guess = int(input("Enter your guess: "))  
    
    if guess < secret_number:
        print("Too low! Try a higher number.")
    elif guess > secret_number:
        print("Too high! Try a lower number.")
    else:
        print(f"🎉 Correct! The Number Wizard chose {secret_number}. You win!")
        break  