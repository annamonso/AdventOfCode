TOTAL_DIGITS = 12

def best_joltage(line):
    digits = [int(c) for c in line.strip()]
    n = len(digits)
    remove = n - TOTAL_DIGITS
    stack = []

    for d in digits:
        while stack and remove > 0 and stack[-1] < d:
            stack.pop()
            remove -= 1
        stack.append(d)

    # si todavía quedan por eliminar, los quitamos del final
    if remove > 0:
        stack = stack[:-remove]

    # nos quedamos con los primeros 12 dígitos
    result_digits = stack[:TOTAL_DIGITS]
    return int("".join(str(x) for x in result_digits))


with open('input.txt', 'r') as file:
    data = [line.strip() for line in file]

total = 0
for line in data:
    val = best_joltage(line)
    print(val)
    total += val

print("Total joltage:", total)
