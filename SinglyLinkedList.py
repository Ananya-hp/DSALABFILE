# Singly Linked List – Insert, Delete, Search

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    # Insert at end
    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    # Insert at position
    def insert_pos(self, data, pos):
        new = Node(data)
        if pos == 1:
            new.next = self.head
            self.head = new
            return

        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        new.next = temp.next
        temp.next = new

    # Delete from beginning
    def delete_begin(self):
        if self.head is None:
            print("List Empty")
            return
        self.head = self.head.next

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List Empty")
            return
        if self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    # Delete from position
    def delete_pos(self, pos):
        if self.head is None:
            print("Empty List")
            return

        if pos == 1:
            self.head = self.head.next
            return

        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid Position")
            return

        temp.next = temp.next.next

    # Search value
    def search(self, key):
        temp = self.head
        pos = 1

        while temp:
            if temp.data == key:
                print(f"Value {key} found at position {pos}")
                return
            temp = temp.next
            pos += 1

        print(f"Value {key} not found in the list")

    # Display list
    def display(self):
        temp = self.head
        if temp is None:
            print("List Empty")
            return
        while temp:
            print(temp.data, end=" → ")
            temp = temp.next
        print("NULL")


# ---------------- MAIN MENU ----------------

ll = LinkedList()

while True:
    print("\n1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete from Beginning")
    print("5. Delete from End")
    print("6. Delete from Position")
    print("7. Search an Element")
    print("8. Display")
    print("9. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        d = int(input("Enter value: "))
        ll.insert_begin(d)

    elif ch == 2:
        d = int(input("Enter value: "))
        ll.insert_end(d)

    elif ch == 3:
        d = int(input("Enter value: "))
        p = int(input("Enter position: "))
        ll.insert_pos(d, p)

    elif ch == 4:
        ll.delete_begin()

    elif ch == 5:
        ll.delete_end()

    elif ch == 6:
        p = int(input("Enter position: "))
        ll.delete_pos(p)

    elif ch == 7:
        key = int(input("Enter value to search: "))
        ll.search(key)

    elif ch == 8:
        ll.display()

    elif ch == 9:
        break

    else:
        print("Invalid Choice")
