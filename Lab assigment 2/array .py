array = [10, 20, 30, 40, 50,90, 100, 110, 120, 130, 140, 150]   

while True:
    print("\nCurrent Array:", array)
    print("\n1. Insert")
    print("2. Delete")
    print("3. Search")
    

    choice = int(input("Enter your choice: "))

    # Insert
    if choice == 1:
        index = int(input("Enter index to insert: "))
        value = int(input("Enter value: "))

        if 0 <= index <= len(array):
            array.insert(index, value)
            print("Element inserted successfully.")
        else:
            print("Invalid index.")

    # Delete
    elif choice == 2:
        value = int(input("Enter value to delete: "))

        if value in array:
            array.remove(value)
            print("Element deleted successfully.")
        else:
            print("Element not found.")

    # Search
    elif choice == 3:
        value = int(input("Enter value to search: "))

        if value in array:
            index = array.index(value)
            print("Element found at index:", index)
        else:
            print("Element not found.")

   