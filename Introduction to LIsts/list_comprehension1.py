start = int(input("Enter Start Number: "))  # start_number = 1
end = int(input("Enter End Number: "))      # end_number = 30

my_list = [i for i in range(start, end + 1) if i % 2 == 0 and i % 3 == 0]
print(my_list) # O/P : [6, 12, 18, 24, 30]
