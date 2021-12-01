FN = "input.txt"

last_measurement = None
increment_cnt = 0

with open("input.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        cur_measurement = int(line)
        if last_measurement is not None:
            increment_cnt = increment_cnt + 1 if last_measurement < cur_measurement else increment_cnt 
        last_measurement = cur_measurement

    print(increment_cnt)
