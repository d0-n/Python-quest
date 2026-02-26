secret_number = 8
guess = 0

print("Guess the secret number:")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    if guess != secret_number:
        print("Wrong guess, try again!")

print("Congratulations! You guessed it!")