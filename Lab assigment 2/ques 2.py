array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,202,101, 303, 404, 505, 606, 707, 808, 909]
print("Initial array:", array)
index = -1
for i in range(len(array)):
    if array[i] == input:
        index = i
        break

#searching for the input number in the array
input = int(input("Enter a number to search in the array: "))
found = False
for i in range(len(array)):
    if array[i] == input:
        found = True
        print("Number found at index:", i)
        break

if not found:
    print("Number not found in the array.")
    
#deleting the input number from the array
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,202,101, 303, 404, 505, 606, 707, 808, 909]
print("Initial array:", array)
input = input(int("Enter a number to delete from the array: "))
index = input(int("enter a  index to delete the number: "))

for i in range(len(array)):
    if array[i] == input:
        index = i
        break
    
if input in array:
    array.remove(input)
    print("Number deleted from the array.")
else:
    print("Number not found in the array. Cannot delete.")

#inserting the input numer at the end of the array:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,202,101, 303, 404, 505, 606, 707, 808, 909]
print("Initial array:", array)
input = int(input("Enter a number to insert at the end of the array: "))
index = int(input("enter a  index to insert the number: "))

for i in range(len(array)):
    if array[i] == input:
        index = i
        break
    
if input not in array:
    array.append(input)
    print("Number inserted at the end of the array.")   
