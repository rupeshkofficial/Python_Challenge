# Ask start number and end number from user and print all the numbers from start to end using dor loop

start_num = int(input("Enter Start Number: "))
end_num = int(input("Enter End Number: "))

for i in range(start_num,end_num+1):
    print(i,end=" ")