#!/usr/bin/python3

secret_code = 42
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input("Enter the secret code: "))
    attempts = attempts + 1
    
    if guess == secret_code:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong! {remaining} attempts remaining.")
        else:
            print("Access denied! No attempts left.")
