# Ask start number and end number from user. Print all the numbers from start to end using while loop

start_n = int(input("Enter Start Number: "))
end_n = int(input("Enter End Number: "))

i = start_n

while i <= end_n:
    print(i,end= " ")
    i = i + 1