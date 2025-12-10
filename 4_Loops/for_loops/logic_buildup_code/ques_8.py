# Calculate sum of all numbers are divisible by 4 from 20 to 50

sum = 0

for i in range(20,51):
    if i%4 == 0:
        sum = sum + i
print(f"The sum of all numbers divisible by 4 from 20 to 50 is",sum)