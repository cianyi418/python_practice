def print_times_table(n):
    for i in range(1, n+1):
        j = 1
        while j <= n:
            print(f"{j} x {i} = {i * j}", end="\t")
            j += 1
        print()

while True:
    try:
        n = int(input("Enter the maximum number for the times table: "))
        if n > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Please enter a valid number.")

print_times_table(n)

