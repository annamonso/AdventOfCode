

with open('input.txt', 'r') as file:
    data = file.readlines()

count = 0
position = 50
for line in data:
    direction = line[0]
    steps = int(line[1:-1])
    if direction == 'R':
        position = (position + steps) % 100
        if position == 0:
            count +=1
    elif direction == 'L':
        position = (position - steps) % 100
        if position == 0:
            count +=1
    
print(count)