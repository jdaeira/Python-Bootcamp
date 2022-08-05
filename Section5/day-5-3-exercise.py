total_even = 0
for number in range(1, 101):
    if number % 2 == 0:
        total_even += number
print(total_even)

# Another solution
total = 0
for number in range(2, 101, 2):
    total += number
print(total)