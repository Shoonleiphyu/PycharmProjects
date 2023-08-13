def user_name(email):
    return email.split('@')[0].title()


def main():
    user_data = {}
    email = input("Email: ")
    while email != "":
        name = user_name(email)
        confirm_name = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirm_name == 'n':
            name = input("Name: ").title()

        user_data[email] = name
        email = input("Email: ")

    for email, name in user_data.items():
        print(f"{name} ({email})")


main()
# hex codes for colors 
