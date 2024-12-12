import queue

class CustomerServiceQueue:
    def __init__(self):
        self.customer_queue = queue.Queue()
        self.ticket_number = 1

    def add_customer(self):
        # Add a new customer to the queue with a ticket number
        customer = self.ticket_number
        self.customer_queue.put(customer)
        print(f"Customer {customer} added to the queue with ticket number {customer}.")
        self.ticket_number += 1

    def serve_customer(self):
        # Serve the next customer in the queue
        if not self.customer_queue.empty():
            served_customer = self.customer_queue.get()
            print(f"Serving customer {served_customer}.")
        else:
            print("No customers in the queue to serve.")

    def show_queue(self):
        # Show the current queue of customers
        if not self.customer_queue.empty():
            print("Current customers in the queue:", list(self.customer_queue.queue))
        else:
            print("No customers in the queue.")

def customer_service_system():
    service_queue = CustomerServiceQueue()

    while True:
        print("\nCustomer Service Menu:")
        print("1. Add new customer")
        print("2. Serve customer")
        print("3. Show queue")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            service_queue.add_customer()
        elif choice == '2':
            service_queue.serve_customer()
        elif choice == '3':
            service_queue.show_queue()
        elif choice == '0':
            print("Exiting the customer service system.")
            break
        else:
            print("Invalid option. Please try again.")

# Start the customer service system
customer_service_system()
