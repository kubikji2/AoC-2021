FN = "input.txt"

with open(FN,"r") as f:
    lines = f.readlines()
    msgs = []
    for line in lines:
        _cur_digits, _cur_msg = line.strip().split("|")
        msgs.append(_cur_msg.split(" ")[1:])

    selected_digits_cnt = 0
    for msg in msgs:
        for i in range(4):
            if len(msg[i]) in [2,3,4,7]:
                selected_digits_cnt+=1
    print(selected_digits_cnt)

