# А)
present_list = [1, 2, 3, 4, 5, 5, 4, 5, 6, 7, 8, 10, 10, -1, -2, -1]
new_list = set(present_list)
print(new_list)
# Б)
next_list = []
for item in present_list:
	if present_list.count(item) == 1:
		next_list.append(item)
print(next_list)


