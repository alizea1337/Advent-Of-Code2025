def solve_day1_part1():
    # read the input file
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    
    # start at position 50
    position = 50
    count = 0
    
    # go through each line
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # get the direction and distance
        direction = line[0]
        distance = int(line[1:])
        
        # move the dial
        if direction == 'L':
            position = (position - distance) % 100
        else:  # its R
            position = (position + distance) % 100
        
        # check if we're at 0 now
        if position == 0:
            count += 1
    
    return count

if __name__ == '__main__':
    result = solve_day1_part1()
    print(f"The password is: {result}")

