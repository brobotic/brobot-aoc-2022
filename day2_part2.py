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

    if my_choice == 1:
        if them_choice == 1:
            my_choice = 3

        if them_choice == 2:
            my_choice = 1

        if  them_choice == 3:
            my_choice = 2
    elif my_choice == 2:
        my_choice = them_choice
        score += 3
    elif my_choice == 3:
        score += 6
        
        if them_choice == 1:
            my_choice = 2

        if them_choice == 2:
            my_choice = 3

        if them_choice == 3:
            my_choice = 1

    score += my_choice

print(f'Score: {score}')

