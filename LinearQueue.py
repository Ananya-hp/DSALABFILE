

MAX = 5
queue = [None] * MAX
front = -1
rear = -1

def enqueue(data):
    global front, rear
    if rear == MAX - 1:
        print("Queue is Full")
        return

    if front == -1:      
        front = 0
    rear += 1
    queue[rear] = data
    print("Inserted:", data)

def dequeue():
    global front, rear
    if front == -1:
        print("Queue is Empty")
        return

    removed = queue[front]
    print("Removed:", removed)

    if front == rear:     # Last element removed
        front = rear = -1
    else:
        front += 1

def size():
    if front == -1:
        return 0
    return rear - front + 1

def isFull():
    return rear == MAX - 1

def display():
    if front == -1:
        print("Queue is Empty")
        return
    print("Queue:", queue[front:rear+1])


# ---------------- MAIN MENU ----------------

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Size")
    print("4. IsFull")
    print("5. Display")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        val = int(input("Enter value to insert: "))
        enqueue(val)

    elif ch == 2:
        dequeue()

    elif ch == 3:
        print("Current Size:", size())

    elif ch == 4:
        print("Is Full?", isFull())

    elif ch == 5:
        display()

    elif ch == 6:
        break

    else:
        print("Invalid Choice")
