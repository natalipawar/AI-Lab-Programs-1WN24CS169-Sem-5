# Implement Vacuum Cleaner Agent using concept of Simple Reflex Agent and Goal-Based Architecture.


rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

location = 'A'

print("Initial State:", rooms)

while True:
    print("\nCurrent Location:", location)
    print("Room Status:", rooms[location])

    print("\n1. Simple Reflex Agent")
    print("2. Goal-Based Agent")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        # Simple Reflex Agent
        if rooms[location] == 'Dirty':
            print("Action: Suck")
            rooms[location] = 'Clean'
        else:
            print("Action: Move")

            if location == 'A':
                location = 'B'
            else:
                location = 'A'

    elif choice == '2':
        # Goal-Based Agent
        print("Goal: Clean both rooms")

        if rooms['A'] == 'Dirty':
            location = 'A'
            print("Moving to Room A")
            rooms['A'] = 'Clean'
            print("Room A cleaned")

        if rooms['B'] == 'Dirty':
            location = 'B'
            print("Moving to Room B")
            rooms['B'] = 'Clean'
            print("Room B cleaned")

        if rooms['A'] == 'Clean' and rooms['B'] == 'Clean':
            print("Goal Achieved: Both rooms are clean!")

    elif choice == '3':
        print("Exiting Vacuum Cleaner Agent")
        break

    else:
        print("Invalid choice")

    print("Current Room Status:", rooms)
