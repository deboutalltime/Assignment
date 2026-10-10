count = 0

for k in range(26, 253):
    number = 396 * k
    digits = str(number)

    if len(set(digits)) == 5:
        count += 1

print(count)
