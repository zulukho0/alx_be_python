def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            addItem = input("What would you like to add? ")
            if addItem not in shopping_list:
                shopping_list.append(addItem)
            else:
                print("Item already there") 
            pass
        elif choice == '2':
            # Prompt for and remove an item
            rmItem = input("What item would you like to remove? ")
            if rmItem in shopping_list:
                shopping_list.remove(rmItem)
            else:
                print("Item not found")
            
            pass
        elif choice == '3':
            # Display the shopping list
            for i in shopping_list:
                print(i)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()