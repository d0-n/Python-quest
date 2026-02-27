direction = input("Do you go left or right? ").lower()

if direction == "left":
    action = input("You see a river. Do you swim or wait? ").lower()
    
    if action == "swim":
        print("You swim across and find a hidden treasure! 🏆")
    else:
        print("You wait too long. The opportunity passes.")
        
else:
    print("You fall into a trap. Game over!")
