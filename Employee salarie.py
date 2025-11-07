# ---------------- Sorting Functions ----------------

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Display Top 5 Salaries
def display_top_five(arr):
    print("Top 5 highest salaries:")
    top_five = arr[-5:][::-1]  # last 5 elements, reversed for descending order
    for idx, salary in enumerate(top_five, start=1):
        print(f"{idx}. {salary}")

# ---------------- Main Menu Program ----------------
def main():
    salaries = [45000.50, 32000.75, 60000.00, 52000.25, 75000.80,
                48000.10, 39000.90, 81000.00, 67000.45, 56000.60]
    
    while True:
        print("\n----- Salary Management Menu -----")
        print("1. View Original Salaries")
        print("2. Sort Salaries using Selection Sort")
        print("3. Sort Salaries using Bubble Sort")
        print("4. Display Top 5 Salaries")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("Original Salaries:", salaries)
        
        elif choice == '2':
            s1 = salaries.copy()
            selection_sort(s1)
            print("Salaries after Selection Sort:", s1)
        
        elif choice == '3':
            s2 = salaries.copy()
            bubble_sort(s2)
            print("Salaries after Bubble Sort:", s2)
        
        elif choice == '4':
            sorted_salaries = sorted(salaries)  # sort ascending for top 5
            display_top_five(sorted_salaries)
        
        elif choice == '5':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
