#Represent a basic Queue
class Queue:
    def __init__(self):
        self.items = []  #List to hold queue elements

    #Add an item to the end of the queue
    def enqueue(self, item):
        self.items.append(item)

    #Remove an item from the front of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  #Remove and return the front item
        return None

    #Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

#Simulate a ticketing system
def ticketing_system(customers):
    queue = Queue()
    #Enqueue all customers
    for customer in customers:
        queue.enqueue(customer)
        print(f"{customer} has joined the queue.")

    #Serve each customer in order
    print("\n----- Serving customers in order -----")
    while not queue.is_empty():
        current_customer = queue.dequeue()
        print(f"Serving {current_customer}")

#Example
customers_list = ["Ishan", "Dinuka", "Sagara", "Janith"]
ticketing_system(customers_list)
