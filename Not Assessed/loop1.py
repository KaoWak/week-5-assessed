divisible_by_6 = []
for num in range(0, 100):
    if num % 6 == 0:
        divisible_by_6.append(num)
    else:
        False

print("Numbers divisible by 6 between 0 and 100:", divisible_by_6)