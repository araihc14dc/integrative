def describe_room():
    print("\nYou find yourself in a small, dimly lit room. In front of you, there is: A dusty bookshelf, A locked drawer, A small window.")  # THIS IS WHERE THE CHOICES SHOW UP
    
def examine_bookshelf():
    print("\nThe bookshelf is covered in dust. As you examine it closely, you notice some of the books seemed odd.")
    choice = input("\nDo you want to inspect the books? (yes/no): ").strip().lower()
    if choice == "yes":
        print("\nYou pull out a book, and behind it, you find a small, shiny key hidden in a gap between the books!")
        return True
    else:
        print("\nYou decide to leave the bookshelf area.")
        return False

def open_drawer(has_key):
    if has_key:
        print("\nYou use the key to open the drawer. Inside, you find an exit key! You have escaped the room!")  # THIS IS THE PART WHERE YOU USE THE KEY TO ESCAPE
        return True 
    else:
        print("\nThe drawer is locked. You need to find a key.")
        return False  # THIS PART IS WHERE YOU HAVEN'T FOUND THE KEY

def look_out_window():
    print("\nThrough the window, you see a thick and tall grass with a thorn of a rose. It doesn't seem like you can escape this way.")

def main():
    has_key = False
    escaped = False
    attempts = 0
    max_attempts = 10  

    print("Welcome to 'Escape the Room'! Can you find your way out?")
    describe_room()  # THE INTRO TEXT
    
    while not escaped and attempts < max_attempts:
        action = input("\nWhat do you want to do? (examine bookshelf/open drawer/look out window/quit): ").strip().lower()  # THIS IS WHERE YOU TYPE YOUR CHOICES
        
        if action == "examine bookshelf":
            has_key = examine_bookshelf()
        elif action == "open drawer":
            escaped = open_drawer(has_key)
        elif action == "look out window":
            look_out_window()
        elif action == "quit":
            print("\nYou have given up. The room remains your prison.")
            break
        else:
            print("\nInvalid action. Try again.")
        
        attempts += 1
    
    if not escaped and attempts >= max_attempts:
        print("\nYou took too long! The room seems to close in on you... Game Over.")  # TOO MANY ESCAPE ATTEMPTS

# Corrected line below
if __name__ == "__main__":
    main()
