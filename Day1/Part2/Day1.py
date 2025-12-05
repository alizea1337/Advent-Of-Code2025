def solve_day1_part2():
    # read input file
    with open('../Part1/input.txt', 'r') as f:
        lines = f.readlines()
    
    # start position is 50
    position = 50
    count = 0
    
    # loop through all rotations
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # get direction and how far to rotate
        direction = line[0]
        distance = int(line[1:])
        
        # figure out when we hit 0 during this rotation
        if direction == 'L':
            # going left, find when we cross 0
            k0 = position % 100
            if k0 == 0:
                k0 = 100  # already at 0, so next one is after full turn
        else:  # going right
            # going right, find when we cross 0
            k0 = (-position) % 100
            if k0 == 0:
                k0 = 100  # already at 0, so next one is after full turn
        
        # count how many times we hit 0
        if distance >= k0:
            count += 1 + (distance - k0) // 100
        
        # actually move the dial
        if direction == 'L':
            position = (position - distance) % 100
        else:  # its R
            position = (position + distance) % 100
    
    return count

if __name__ == '__main__':
    result = solve_day1_part2()
    print(f"The password is: {result}")

