rps = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

score = 0

with open('day2_input.txt', 'r') as f:
    data = f.readlines()

for line in data:
    them_choice = rps[line.strip().split(' ')[0]]
    my_choice = rps[line.strip().split(' ')[1]]

    round_points = 0
    round_points += my_choice

    if them_choice == my_choice:
        round_points += 3
    elif them_choice == 1:
        if my_choice == 2:
            round_points += 6
    elif them_choice == 2:
        if my_choice == 3:
            round_points += 6
    elif them_choice == 3:
        if my_choice == 1:
            round_points += 6

    score += round_points

print(f'Score: {score}')

