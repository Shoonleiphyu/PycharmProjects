def main():
    print('*' * len(password))

def get_password(p_len=1):
        password = input("Enter a password: ")
        while len(password) < p_len:
            print("No password entered. Try again")
            password = input("Enter a password: ")
        return password
password = get_password(p_len=1)

main()

