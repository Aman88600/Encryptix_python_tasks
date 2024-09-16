numbers = [i for i in range(1,11)]
for i in numbers:
    if i == 9:
        break
    if i == 3:
        continue
    if i == 5:
        pass
    print(i)