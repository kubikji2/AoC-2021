FN = "input.txt"

def process_data(lines, time_window):
    processed = []
    for i in range(len(lines)-time_window+1):
        data_entry = 0
        for j in range(time_window):
            data_entry += int(lines[i+j])
        processed.append(data_entry)
    return processed

last_measurement = None
increment_cnt = 0

with open(FN,"r") as file:
    lines = file.readlines()
    processed = process_data(lines,3)
    for cur_measurement in processed:
        if last_measurement is not None:
            increment_cnt = increment_cnt + 1 if last_measurement < cur_measurement else increment_cnt 
        last_measurement = cur_measurement

    print(increment_cnt)
