FN = "input.txt"

depth = 0
distance = 0

with open(FN,"r") as f:
    lines = f.readlines()
    for line in lines:
        direction, value = line.split()
        value = int(value)
        if direction == "forward":
            distance += value
        if direction == "down":
            depth += value
        if direction == "up":
            depth -= value

    print(depth, distance, depth*distance)
