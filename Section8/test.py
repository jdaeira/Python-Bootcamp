alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shift = int(input("Please enter the shift number: "))
first_shift = []
for num in range(shift):
    for char in alphabet[num]:
        first_shift += char
print(first_shift)

second_shift = []
for num in range(shift, len(alphabet)):
    for char in alphabet[num]:
        second_shift += char
print(second_shift)

new_alphabet = second_shift + first_shift

print(new_alphabet)

