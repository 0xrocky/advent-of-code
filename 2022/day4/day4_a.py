with open('input') as f:
# reading from the file without '\n'
	lines = [line.rstrip() for line in f]

pairs = [line.split(',') for line in lines]

sections_first_elf = [pair[0].split('-') for pair in pairs]
sections_second_elf = [pair[1].split('-') for pair in pairs]

if len(sections_first_elf) != len(sections_second_elf):
  raise Exception("Something wrongs with the section assignments")

fully_contained = 0
for cont in range(len(sections_first_elf)):
	if (int(sections_first_elf[cont][0]) <= int(sections_second_elf[cont][0]) and int(sections_first_elf[cont][1]) >= int(sections_second_elf[cont][1])) or (int(sections_second_elf[cont][0]) <= int(sections_first_elf[cont][0]) and int(sections_second_elf[cont][1]) >= int(sections_first_elf[cont][1])):
		fully_contained += 1
print(fully_contained)