import mobile

while True:

    print("\n===== MOBILE STORE =====")
    print("1. Add Mobile")
    print("2. Display Mobile")
    print("3. Search Mobile")
    print("4. Update Price")
    print("5. Delete Mobile")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        mobile.add_mobile()

    elif choice == 2:
        mobile.display_mobile()

    elif choice == 3:
        mobile.search_mobile()

    elif choice == 4:
        mobile.update_price()

    elif choice == 5:
        mobile.delete_mobile()

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")