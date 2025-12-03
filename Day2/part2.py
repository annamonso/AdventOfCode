def is_invalid_id(n):
    s = str(n)
    L = len(s)

    for block in range(1, L):
        if L % block == 0:
            repeat = L // block
            if repeat >= 2:
                part = s[:block]
                if part * repeat == s:
                    return True

    return False

# main
if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        data = file.read().strip().split(',')

    totalID = 0 
    print(data)
    for item in data:
        start, end = map(int, item.split('-'))
        
        for n in range(start, end + 1):
            if is_invalid_id(n):
                totalID += n

    print("Invalid IDs:", totalID)
        
