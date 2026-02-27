# Ask the user for their age and gold amount
age = int(input("Enter your age: "))
gold = int(input("Enter how many gold coins you have: "))

# Check both conditions
if age >= 18 and gold >= 20:
    print("You may enter the club!")
else:
    print("You cannot enter.")
