with open('input.txt', 'r') as file:
    data = file.readlines()

count = 0
position = 50

for line in data:
    direction = line[0]
    steps = int(line[1:-1])
    
    if direction == 'R': 
        count += (position + steps) // 100
        position = (position + steps) % 100
    
    elif direction == 'L':
        if position == 0:
            count += steps // 100
            
        else:  
            if steps >= position:
                count += 1 + (steps - position) // 100

        position = (position - steps) % 100
        
print(count)

