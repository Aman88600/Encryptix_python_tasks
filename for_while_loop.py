numbers = [i for i in range(1,11)]

for i in numbers:
    print(i)

i = 0
while i < len(numbers):
    print(f"i = {i} and num = {numbers[i]}")
    i += 1