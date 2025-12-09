# Calculate how many numbers are divisible by 6 and 7 both between 1 to 200

count = 0
i = 1

while i <= 200:
    if i % 6 == 0 and i % 7 == 0:
        count = count + 1
    i = i + 1
print(f"The total numbers divisible by 6 and 7 both between 1 to 200 are:",count)