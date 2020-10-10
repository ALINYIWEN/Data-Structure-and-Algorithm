# Simple Queue
class Queue:
    def __init__(self):
        self.Queue = []

    # Add an element
    def enqueue(self, item):
        self.Queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.Queue) < 1:
            return
        return self.Queue.pop()    

    # Display the Queue
    def display(self):
        print(self.Queue)

    def size(self):
        return len(self.Queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)      
q.enqueue(4)
q.enqueue(5)      
q.display()
q.dequeue()
q.display()
print("=====================================================")

# Circle Queue
class CircularQueue():
    def __init__(self, size):
        self.size = size
        self.Queue = [None]*size
        self.head = self.tail = -1

    # Insert an element into the circular Queue
    def enqueue(self, data):
        if ((self.tail + 1) % self.size == self.head):
            print("The circular queue is full\n")
        
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.Queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.size
            self.Queue[self.tail] = data   

    # Delete an element from the circular queue
    def dequeue(self):
        if(self.head == -1):
            print("The circular queue is empty\n")

        elif(self.head == self.tail):
            temp = self.Queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.Queue[self.head]
            self.head = (self.head + 1) % self.size

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.Queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.size):
                print(self.Queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.Queue[i], end=" ")
            print()

obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()
print("=====================================================")

# Priority Queue

# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Function to insert an element into the tree
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)


# Function to delete an element from the tree
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(size - 1)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)


arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
print("=====================================================")

# Deque
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)      # 在列表末尾添加元素

    def addRear(self, item):
        self.items.insert(0, item)   # insert()可在列表的任何位置添加新元素

    def removeFront(self):
        return self.items.pop()      # pop()可删除列表末尾的元素

    def removeRear(self):
        return self.items.pop(0)     # pop()只要知道其引索位置可弹出任何位置的元素

    def size(self):
        return len(self.items)

d = Deque()
print("初始Deque : "+str(d.items))
d.addRear(8)
d.addRear(5)
d.addFront(7)
d.addFront(10)

print("中途Deque : "+str(d.items))
d.addRear(11)
print("addRear(11) : "+str(d.items))
d.removeRear()
print("removeRear() : "+str(d.items))
d.removeFront()
print("removeFront() : "+str(d.items))
d.addFront(55)
print("d.addFront(55) : "+str(d.items))
d.addRear(45)
print("addRear(45) : "+str(d.items))