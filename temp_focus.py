def main():
    while True:
        print("1. Start a temperature focus session")
        print("2. Show today's temperature summary")
        print("3. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Starting a temperature focus session... (placeholder)")
        elif choice == "2":
            print("Showing today's temperature summary... (placeholder)")
        elif choice == "3":
            print("Quitting... (placeholder)")
            break
        else:
            print("Not a valid choice")


if __name__ == "__main__":
    main()