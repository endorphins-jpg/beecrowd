numbers = []

for i in range(100):
    numbers.append(int(input()))

max_n = max(numbers)
max_index = numbers.index(max_n) + 1

print(max_n)
print(max_index)