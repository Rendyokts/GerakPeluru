total = 0
for i in range(101):
    total += i
print(total)

total_odd = 0
total_even = 0
for i in range(101):
    if i % 2 == 0:
        total_even += i
    else:
        total_odd += i
print(total_even)
print(total_odd)

