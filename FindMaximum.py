num = int(input("Enter the number of elements in the list: "))
lst = []

for i in range(num):
    element = int(input("Enter element: "))
    lst.append(element)


print("Maximum element in the list is: ", max(lst))