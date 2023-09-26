import PMBackend

def main():
    password = {}
    pm = PMBackend.PasswordManager()

    print("""What do you want to do?
    (1) Create a new key
    (2) Load an existing key
    (3) Create a new password file
    (4) Load an existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit
    """)

    done = False

    while not done:
        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("What site do you want the password for: ")
            print(f"Password for {site} is {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print("Bye")
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
