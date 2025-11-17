# Ask N from from user. N means number of lines. Then print the following pattern

''''
Enter n = 6

6 6 6 6 6
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1

'''

n = int(input("Enter n = "))

for i in range(6,0,-1):
    for j in range(1,n+1):
        print(i,end = " ")
    print()