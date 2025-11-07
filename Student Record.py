# Student Record System using Linked List

class Node:
    def __init__(self, rollno, name, marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_student(self, rollno, name, marks):
        new_node = Node(rollno, name, marks)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Student with Roll No {rollno} added.")

    def display(self):
        if not self.head:
            print("No student records found.")
            return
        current = self.head
        print("Student Records:")
        while current:
            print(f"[Roll: {current.rollno}, Name: {current.name}, Marks: {current.marks}]", end=" -> ")
            current = current.next
        print("None")

    def delete(self, rollno):
        if not self.head:
            print("No records to delete.")
            return

        if self.head.rollno == rollno:
            self.head = self.head.next
            print(f"Record with Roll No {rollno} deleted.")
            return

        prev = None
        current = self.head
        while current and current.rollno != rollno:
            prev = current
            current = current.next

        if not current:
            print("Roll number not found.")
        else:
            prev.next = current.next
            print(f"Record with Roll No {rollno} deleted.")

    def update(self, rollno, new_name, new_marks):
        current = self.head
        while current:
            if current.rollno == rollno:
                current.name = new_name
                current.marks = new_marks
                print(f"Record with Roll No {rollno} updated.")
                return
            current = current.next
        print("Roll number not found.")

    def search(self, rollno):
        current = self.head
        while current:
            if current.rollno == rollno:
                print(f"Record found: [Roll: {current.rollno}, Name: {current.name}, Marks: {current.marks}]")
                return
            current = current.next
        print("Roll number not found.")

    def sort(self):
        if not self.head:
            print("No records to sort.")
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current and current.next:
                if current.rollno > current.next.rollno:
                    # Swap all fields
                    current.rollno, current.next.rollno = current.next.rollno, current.rollno
                    current.name, current.next.name = current.next.name, current.name
                    current.marks, current.next.marks = current.next.marks, current.marks
                    swapped = True
                current = current.next
        print("Records sorted by Roll Number.")

def main():
    ll = LinkedList()
    
    while True:
        print("\nMenu")
        print("1. Add student details")
        print("2. Delete roll number")
        print("3. Update name and marks")
        print("4. Search roll number")
        print("5. Sort list")
        print("6. Display")
        print("7. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1-7.")
            continue

        if choice == 1:
            try:
                rollno = int(input("Enter roll number: "))
                name = input("Enter name: ")
                marks = int(input("Enter marks: "))
                ll.add_student(rollno, name, marks)
            except ValueError:
                print("Invalid input. Roll number and marks should be integers.")
        elif choice == 2:
            try:
                rollno = int(input("Enter the roll number to delete: "))
                ll.delete(rollno)
            except ValueError:
                print("Invalid input. Roll number should be an integer.")
        elif choice == 3:
            try:
                rollno = int(input("Enter the roll number to update: "))
                new_name = input("Enter new name: ")
                new_marks = int(input("Enter new marks: "))
                ll.update(rollno, new_name, new_marks)
            except ValueError:
                print("Invalid input. Roll number and marks should be integers.")
        elif choice == 4:
            try:
                rollno = int(input("Enter the roll number to search: "))
                ll.search(rollno)
            except ValueError:
                print("Invalid input. Roll number should be an integer.")
        elif choice == 5:
            ll.sort()
        elif choice == 6:
            ll.display()
        elif choice == 7:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select from 1-7.")

if __name__ == "__main__":
    main()
