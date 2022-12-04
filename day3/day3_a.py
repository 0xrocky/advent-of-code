with open('input') as f:
# reading from the file without '\n'
	lines = [line.rstrip() for line in f]

#utils - ASCII: 'A' = 65, 'a' = 97
ord_A = ord('A')
ord_Z = ord('Z')
ord_a = ord('a')
ord_z = ord('z')

# this list represent the item 'A..Za..z' in order to find the items in common in both compartments of each rucksack
# yep i waste a few positions in the list for the 7 ascii characters between the 'Z' and the 'a': i don't want to check if a char is upper or lower case
both_items = [0]*(ord_z - ord_A + 1)
# this variable represents the sum of the priorities of the item types
priorities = 0

# the function calculating the priority of an item: 'a' = 1, 'z' = 26, 'A' = 27, 'Z' = 52
def return_priority(ch):
	if ch.isupper():
		for i in range(ord_A, ord_Z + 1):
			if chr(i) == ch:
				return (i - ord_A + 27)
	else:
		for i in range(ord_a, ord_z + 1):
			if chr(i) == ch:
				return (i - ord_a + 1)

for line in lines:
	# first half line, where i add: set deletes duplicates
	for ch in "".join(set(line[:len(line) // 2])):
		both_items[ord(ch) - ord_A ] += 1
	# second half line, where i sub: set deletes duplicates
	for ch in "".join(set(line[len(line) // 2:])):
		both_items[ord(ch) - ord_A] -= 1
	# i expect that, for the chars occurred, the result is 0 otherwise the character is not there in both halves
	for ch in "".join(set(line)):
		if both_items[ord(ch)-ord_A] == 0:
			priorities += return_priority(ch)
	# clear the list of occurrencies
	for i in range(len(both_items)):
		both_items[i] = 0
print(priorities)	