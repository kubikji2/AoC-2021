FN = "input.txt"

aim = 0
depth = 0
distance = 0

with open(FN,"r") as f:
    lines = f.readlines()
    for line in lines:
        direction, value = line.split()
        value = int(value)
        if direction == "forward":
            distance += value
            depth += value*aim
        if direction == "down":
            aim += value
        if direction == "up":
            aim -= value

    print(depth, distance, depth*distance)
