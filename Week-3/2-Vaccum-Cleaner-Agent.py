# Vacuum Cleaner Agent

def vacuum(location, A, B):
    while True:
        if location == 'A' and A == 'Dirty':
            action = 'SUCK'
            A = 'Clean'
        elif location == 'B' and B == 'Dirty':
            action = 'SUCK'
            B = 'Clean'
        elif A == 'Dirty':
            action = 'LEFT'
            location = 'A'
        elif B == 'Dirty':
            action = 'RIGHT'
            location = 'B'
        else:
            action = 'NO-OP'

        print("Action:", action)

        if action == 'NO-OP':
            break

        print("Location:", location, "| A:", A, "| B:", B)

    print("\nFinal Environment")
    print("Location:", location)
    print("Room A:", A)
    print("Room B:", B)

location = input("Initial Location (A/B): ").upper()
A = input("Room A (Clean/Dirty): ").capitalize()
B = input("Room B (Clean/Dirty): ").capitalize()

vacuum(location, A, B)
