# asking the user to inter the starting number
Depart = int(input("Enter a starting number: "))

print("The next ten numbers are:")

# Loop to print the next ten numbers
for i in range(1, 11):
    print(Depart + i)
