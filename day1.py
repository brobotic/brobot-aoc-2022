import json
import os
from operator import itemgetter

with open('day1_input.txt', 'r') as f:
    data = f.readlines()

elf_number = 0
caloric_data = {}

for line in data:
    if line.strip():
        if elf_number not in caloric_data:
            caloric_data[elf_number] = 0

        caloric_data[elf_number] += int(line)
    else:
        elf_number = elf_number + 1

#print(json.dumps(caloric_data, sort_keys=True, indent=4))
print('Elf with the highest caloric intake: ', max(caloric_data.values()))

top_3_elves = dict(sorted(caloric_data.items(), key = itemgetter(1), reverse = True)[:3])
print('Sum of the top 3 elves\' caloric intake:', sum(top_3_elves.values()))
