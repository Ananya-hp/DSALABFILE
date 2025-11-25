class CircularQueue:
    
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

  
    def isFull(self):
        return (self.rear + 1) % self.size == self.front

  
    def isEmpty(self):
        return self.front == -1

   
    def enqueue(self, value):
        if self.isFull():
            print("Queue is Full!")
            return
        
        if self.front == -1:    
            self.front = 0
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued: {value}")

  
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        
        removed = self.queue[self.front]

       
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        print(f"Dequeued: {removed}")

  
    def display(self):
        if self.isEmpty():
            print("Queue is Empty!")
            return
        
        print("Queue Elements:", end=" ")
        i = self.front
        
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        
        print()



q = CircularQueue(5)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

q.display()

q.dequeue()
q.dequeue()

q.display()

q.enqueue(50)
q.enqueue(60)

q.display()
