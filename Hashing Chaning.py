# Hash Table implementation using Chaining
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]   # list of lists for chaining

    def hash_function(self, key):
        return key % self.size   # division method

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists → update value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated key {key} with value {value}")
                return
        # Otherwise, append new key-value pair
        self.table[index].append([key, value])
        print(f"Inserted ({key}, {value}) at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Found key {key} with value {pair[1]}")
                return pair[1]
        print(f"Key {key} not found")
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print(f"Deleted key {key}")
                return
        print(f"Key {key} not found, cannot delete")

    def display(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")
ht = HashTable()

while True:
    print("\n--- Hash Table Menu ---")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key (integer): "))
        value = input("Enter value: ")
        ht.insert(key, value)

    elif choice == 2:
        key = int(input("Enter key to search: "))
        ht.search(key)

    elif choice == 3:
        key = int(input("Enter key to delete: "))
        ht.delete(key)

    elif choice == 4:
        ht.display()

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
