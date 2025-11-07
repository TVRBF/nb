# ---------------- Search Functions ----------------

# Linear Search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # return index if found
    return -1       # return -1 if not found

# Binary Search (requires sorted list)
def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ---------------- Main Menu Program ----------------
def main():
    # Example customer account IDs
    customer_ids = [105, 210, 315, 420, 525, 630, 735]
    
    while True:
        print("\n----- Customer Search Menu -----")
        print("1. View Customer IDs")
        print("2. Linear Search")
        print("3. Binary Search")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print("Customer IDs:", customer_ids)
        
        elif choice == '2':
            try:
                key = int(input("Enter Customer ID to search: "))
                pos = linear_search(customer_ids, key)
                if pos != -1:
                    print(f"Linear Search: Customer ID {key} found at position {pos}")
                else:
                    print(f"Linear Search: Customer ID {key} not found")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '3':
            try:
                key = int(input("Enter Customer ID to search: "))
                sorted_ids = sorted(customer_ids)
                pos = binary_search(sorted_ids, key)
                if pos != -1:
                    print(f"Binary Search: Customer ID {key} found at position {pos}")
                else:
                    print(f"Binary Search: Customer ID {key} not found")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == '4':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-4.")

if __name__ == "__main__":
    main()
