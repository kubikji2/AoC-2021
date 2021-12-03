FN = "input.txt"

ones_cnt = []

with open(FN,"r") as f:
    lines = f.readlines()
    # total bit len, one removes newline character
    bit_len = len(lines[0])-1
    # total number of entries
    entries_cnt = len(lines)
    # 1) count ones in each place
    for i in range(bit_len):
        one_cnt = 0
        for line in lines:
            if line[i] == "1":
                one_cnt += 1
        ones_cnt.append(one_cnt)
    
    # 2) compose binary string
    gamma_str = ""
    epsilon_str = ""
    for i in range(bit_len):
        if ones_cnt[i] > entries_cnt/2:
            gamma_str += "1"
            epsilon_str += "0"
        else:
            epsilon_str += "1"
            gamma_str += "0"
    print("gamma:", gamma_str, "eps: ", epsilon_str)

    # 3) convert to decimal
    gamma = int(gamma_str,2)
    epsilon = int(epsilon_str,2)
    print("gamma:", gamma, "eps: ", epsilon)

    # 4) print result
    print("result:", gamma*epsilon)
