# ---------------- STACK APPLICATIONS (ALL IN ONE) ----------------

# 1. Reverse a String
def reverse_string():
    text = input("Enter string to reverse: ")
    stack = []

    for ch in text:
        stack.append(ch)

    reversed_text = ""
    while stack:
        reversed_text += stack.pop()

    print("Reversed String =", reversed_text)


# 2. Check Balanced Parentheses
def is_balanced():
    expr = input("Enter expression: ")
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for ch in expr:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack:
                print("Not Balanced")
                return
            if stack.pop() != pairs[ch]:
                print("Not Balanced")
                return

    if len(stack) == 0:
        print("Balanced")
    else:
        print("Not Balanced")


# 3. Undo Operation (Text Editor Simulation)
def undo_operation():
    stack = []
    while True:
        print("\n--- Undo Operation Menu ---")
        print("1. Type Character")
        print("2. Undo")
        print("3. Show Text")
        print("4. Exit Undo Module")

        ch = input("Enter choice: ")

        if ch == "1":
            c = input("Enter character: ")
            stack.append(c)
            print("Added:", c)

        elif ch == "2":
            if stack:
                removed = stack.pop()
                print("Undo → removed:", removed)
            else:
                print("Nothing to undo.")

        elif ch == "3":
            print("Current Text:", "".join(stack))

        elif ch == "4":
            print("Exiting Undo Module.")
            break

        else:
            print("Invalid choice.")



# ---------------- MAIN MENU ----------------

while True:
    print("\n============================")
    print("   STACK APPLICATION MENU   ")
    print("============================")
    print("1. Reverse a String")
    print("2. Check Balanced Parentheses")
    print("3. Undo Operation (Text Editor)")
    print("4. Exit Program")

    choice = input("Enter your choice: ")

    if choice == "1":
        reverse_string()

    elif choice == "2":
        is_balanced()

    elif choice == "3":
        undo_operation()

    elif choice == "4":
        print("Exiting Program.")
        break

    else:
        print("Invalid choice. Try again.")
