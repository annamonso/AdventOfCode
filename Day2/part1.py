with open('input.txt', 'r') as file:
    data = file.read().strip().split(',')
    
totalID = 0 
print(data)
for range in data:
    start, end = range.split('-')
    totalvalues = int(end) - int(start) + 1
    value = int(end) 
    while totalvalues > 0:
        value = str(value)
        lenght = len(value)
        if lenght % 2 == 0:
            first_half = value[:lenght//2]
            second_half = value[lenght//2:]
            if first_half == second_half:
                totalID += int(value)
                
        value = int(value) - 1
        totalvalues -= 1
        
print(totalID)
     
