print("Welcome to Adventure Time! Where do you want to go?")

def choose_location():
    print("1. Jungle\n2. Under the sea\n3. City")
    choice = int(input("Enter 1, 2, or 3: "))

    if choice == 1:
        jungle()
    elif choice == 2:
        under_the_sea()
    elif choice == 3:
        city()
    else:
        print("Invalid choice. Try again.")
        choose_location()

def jungle():
    print("You are in the jungle! Wild animals are chasing you!")
    print("1. Climb a tree\n2. Run across the river\n3. Hide behind rocks")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("You climb a tree and escape the wild animals. You are safe… for now!")
    elif choice == 2:
        print("You try to cross the river, but the current is too strong! Game over ")
    elif choice == 3:
        print("You hide behind rocks. The animals pass by. You survived!")
    else:
        print("Invalid choice. Try again.")
        jungle()


def under_the_sea():
    print("You dive into the deep sea, colorful fish swim around you.")
    print("1. Follow a glowing fish\n2. Explore a sunken ship\n3. Go into a dark cave")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("The glowing fish leads you to a hidden treasure! You win! ")
    elif choice == 2:
        print("The sunken ship collapses! You barely escape. Game over ")
    elif choice == 3:
        print("You find some precious pearls in the cave! Nice find!")
    else:
        print("Invalid choice. Try again.")
        under_the_sea()

def city():
    print("You arrive in a bustling city filled with people and mysteries.")
    print("1. Enter a mysterious alley\n2. Visit the market\n3. Go to a tall skyscraper")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("A thief tries to steal your bag! You barely escape! Game over ")
    elif choice == 2:
        print("You find a magical potion at the market. You feel lucky! ")
    elif choice == 3:
        print("You climb the skyscraper and enjoy the amazing view. You are safe!")
    else:
        print("Invalid choice. Try again.")
        city()

choose_location()