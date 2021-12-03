import copy

FN = "input.txt"

ones_cnt = []

with open(FN,"r") as f:
    lines = f.readlines()
    # total bit len, one removes newline character
    bit_len = len(lines[0])-1
    # total number of entries
    entries_cnt = len(lines)
   
    # 1) get oxygen rate
    oxy_rate_lines = copy.deepcopy(lines)
    for i in range(bit_len):
        one_cnt = 0
        for line in oxy_rate_lines:
            if line[i] == "1":
                one_cnt += 1
        
        oxy_entries_cnt = len(oxy_rate_lines)
        bit_to_keep = "1" if one_cnt >= oxy_entries_cnt/2 else "0"
        #print(one_cnt, bit_to_keep)
        
        _oxy_rate_lines = []
        for line in oxy_rate_lines:
            if line[i] == bit_to_keep:
                _oxy_rate_lines.append(line)

        oxy_rate_lines = _oxy_rate_lines
        #print(oxy_rate_lines)
        
        if len(oxy_rate_lines) == 1:
            break

    # 2) CO2 rate
    co2_rate_lines = copy.deepcopy(lines)
    for i in range(bit_len):
        one_cnt = 0
        for line in co2_rate_lines:
            if line[i] == "1":
                one_cnt += 1
        
        oxy_entries_cnt = len(co2_rate_lines)
        bit_to_keep = "0" if one_cnt >= oxy_entries_cnt/2 else "1"
        #print(one_cnt, bit_to_keep)
        
        _co2_rate_lines = []
        for line in co2_rate_lines:
            if line[i] == bit_to_keep:
                _co2_rate_lines.append(line)

        co2_rate_lines = _co2_rate_lines
        #print(co2_rate_lines)

        if len(co2_rate_lines) == 1:
            break

    # 3) convert to binary string
    oxy_str = oxy_rate_lines[0][:-1]
    co2_str = co2_rate_lines[0][:-1]
    print("oxy:", oxy_str, "CO2: ", co2_str)

    # 3) convert to decimal
    oxy_rate = int(oxy_str,2)
    co2_rate = int(co2_str,2)
    print("oxy:", oxy_rate, "CO2: ", co2_rate)

    # 4) print result
    print("result:", oxy_rate*co2_rate)
