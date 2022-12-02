# opening the file of the calories in input in read mode
with open('input') as f:
# reading from the file without '\n'
	lines = [line.rstrip() for line in f]

# respectly, max sum of calories among all the elves, updated in the following loop, and sum of calories of the current elf
max_calories_sum = curr_calories = 0

# iteration for each calories in the file
for line in lines:
	# here reading the calories of the current elf
	if line.isdigit():
		curr_calories += int(line)
	# here the current elf is going to change, so I compare the current calories accumulated with the max sum of calories
	else:
		max_calories_sum = curr_calories if (curr_calories > max_calories_sum) else max_calories_sum
		curr_calories = 0

print(max_calories_sum)