
MENU = """H-Hello
G-Goodbye
Q-Quit"""
name = input("Enter name:")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name:} ")

    elif choice == "G":
        print(f"Goodbye {name:} ")

    else:
        print("Invalid option")
    break
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
