stack = []

def push():
    item = input("Enter item to push: ")
    stack.append(item)
    print(f"Pushed {item} onto stack.")

def pop():
    if not stack:
        print("Stack is empty. Nothing to pop.")
    else:
        removed = stack.pop()
        print(f"Popped: {removed}")

def peek():
    if not stack:
        print("Stack is empty. No top element.")
    else:
        print(f"Top element: {stack[-1]}")

def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack contents:", stack)

# ------------------ MAIN MENU ------------------

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        push()
    elif choice == "2":
        pop()
    elif choice == "3":
        peek()
    elif choice == "4":
        display()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
