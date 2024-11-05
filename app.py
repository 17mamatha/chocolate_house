from database import initialize_db, add_flavor, get_flavors

def main():
    initialize_db()
    while True:
        print("1. Add Flavor")
        print("2. View Flavors")
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Flavor name: ")
            is_seasonal = input("Is it seasonal (yes/no): ").lower() == 'yes'
            add_flavor(name, is_seasonal)
            print("Flavor added successfully.")
        elif choice == "2":
            flavors = get_flavors()
            for flavor in flavors:
                print(flavor)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
