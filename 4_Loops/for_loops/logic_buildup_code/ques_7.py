# Calculate how many numbers are divisible by 6 and 7 from 1 to 200

count = 0

for i in range(1,201):
    if i%6 == 0 and i % 7 == 0:
        count = count + 1
print(f"The total numbers divisible by 6 and 7 from 1 to 200 is",count)