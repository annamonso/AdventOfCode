with open('input.txt', 'r') as file:
    data = [line.strip() for line in file]

totalNumberCode = 0

for line in data:
    best_value = -1
    for i in range(len(line) - 1):
        first = int(line[i])
        second = max(int(d) for d in line[i + 1:])
        value = first * 10 + second
        if value > best_value:
            best_value = value

    print(best_value)
    totalNumberCode += best_value

print(totalNumberCode)
