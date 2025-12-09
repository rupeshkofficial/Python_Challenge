# Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50

sum = 0
i = 20

while i <= 50:
    if i % 4 == 0:
        sum = sum + i
    i = i + 1
print(f"sum of all the numbers divisible by 4 from 20 to 50 is:",sum)