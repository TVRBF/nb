class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insertion
    def insert(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    # Inorder Display (sorted order)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    # Search
    def search(self, root, key):
        if root is None:
            return None
        if root.key == key:
            return root
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Deletion
    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            # Node with two children: get inorder successor
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
bst = BST()
root = None

while True:
    print("\n--- Binary Search Tree Menu ---")
    print("1. Insert")
    print("2. Display (Inorder Traversal)")
    print("3. Search")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        root = bst.insert(root, key)

    elif choice == 2:
        print("BST Inorder Traversal: ", end="")
        bst.inorder(root)
        print()

    elif choice == 3:
        key = int(input("Enter key to search: "))
        result = bst.search(root, key)
        if result:
            print(f"Key {key} found in BST")
        else:
            print(f"Key {key} not found")

    elif choice == 4:
        key = int(input("Enter key to delete: "))
        root = bst.delete(root, key)
        print(f"Key {key} deleted (if it existed)")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")
