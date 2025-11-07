event_queue = []

def add_event(eventname):
    event_queue.append(eventname)
    print(f"Event '{eventname}' added successfully")

def process_event():
    if event_queue:
        event = event_queue.pop(0)
        print(f"Processing Event '{event}'")
    else:
        print("No Event To Process")

def display_event():
    if event_queue:
        print("\nCurrent events in the queue:")
        for i, name in enumerate(event_queue, 1):
            print(f"{i}. {name}")
    else:
        print("No Event In The Queue")

def cancel_event(eventname):
    if eventname in event_queue:
        event_queue.remove(eventname)
        print(f"Event '{eventname}' has been cancelled from the queue")
    else:
        print("No Such Event Found In Queue Or It Might Have Been Processed")

# Menu-driven program
while True:
    print("\n-----------MENU-------------")
    print("1. Add Event")
    print("2. Process Event")
    print("3. Display Events")
    print("4. Cancel Event")
    print("5. Exit")
    
    choice = input("Enter The Choice (1-5): ")
    
    if choice == '1':
        name = input("Enter Event name: ")
        add_event(name)
    elif choice == '2':
        process_event()
    elif choice == '3':
        display_event()
    elif choice == '4':
        name = input("Enter event name to cancel: ")
        cancel_event(name)
    elif choice == '5':
        print("Exiting Program")
        break
    else:
        print("Enter valid choice")
