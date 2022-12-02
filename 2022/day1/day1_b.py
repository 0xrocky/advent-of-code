# opening the file in read mode
with open('input') as f:
# reading from the file without '\n'
	lines = [line.rstrip() for line in f]

# a list of three elements, representing the sum of the calories carried by the top three elves carrying the most calories
max_calories_sum = [0]*3
# the sum of the calories carried by the current elf
curr_calories = 0

# iteration for each calories in the file
for line in lines:
	# here reading the calories of the current elf
	if line.isdigit():
		curr_calories += int(line)
	# here the current elf is going to change, so I compare the current calories accumulated with the max sum of calories
	else:
		# note that the list is sorted, so the first element of the list is always the min
		max_calories_sum.sort()
		# it is sufficient to compare the max sum only with the first element of the list
		max_calories_sum[0] = curr_calories if (curr_calories > max_calories_sum[0]) else max_calories_sum[0]
		# reset
		curr_calories = 0

print(sum(max_calories_sum))