first_numbers = [0, 10, 11, 22, 33, 44, 155, 267, 456, 643, 654, 214, 151]
new_numbers = []
final_numbers = len(first_numbers)
for i in range(final_numbers):
	if first_numbers[i] % 2 == 0:
		new_numbers.append(first_numbers[i] / 4)
	else:
		new_numbers.append(first_numbers[i] * 2)
print(new_numbers)