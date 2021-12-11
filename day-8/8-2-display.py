FN = "input.txt"

def my_segment_filter(digits, seg_cnt):
    result = [digit for digit in digits if len(digit)==seg_cnt]
    assert len(result) == 1
    return result[0]

def letter_in_string(letters, string_to_search):
    for letter in letters:
        if letter not in string_to_search:
            return False
    return True

def same_letters(s1,s2):
    if len(s1) != len(s2):
        return False
    
    for letter in s1:
        if letter not in s2:
            return False
    return True

with open(FN,"r") as f:
    lines = f.readlines()
    msgs = []
    digits = []
    for line in lines:
        _cur_digits, _cur_msg = line.strip().split("|")
        msgs.append(_cur_msg.split(" ")[1:])
        digits.append(_cur_digits.split(" ")[:-1])

    total_sum = 0
    for i in range(len(msgs)):
        _cur_msg = msgs[i]
        _cur_digits = digits[i]
        # 1) identify unique digits based on segments
        one = my_segment_filter(_cur_digits,2)
        four = my_segment_filter(_cur_digits,4)
        seven = my_segment_filter(_cur_digits,3)
        eight = my_segment_filter(_cur_digits,7)
        identified = [None,one,None,None,four,None,None,seven,eight,None]
        # 2) create segment contained in 4 digit, but not in 1
        four_m_one = "".join([seg for seg in four if seg not in one])
        # 3) use conditions for 5-segment and 6-segment digits
        for _cur_digit in _cur_digits:
            # 5-segment
            if len(_cur_digit) == 5:
                #print(_cur_digit)
                if letter_in_string(seven, _cur_digit):
                    # three
                    identified[3]=_cur_digit
                elif letter_in_string(four_m_one, _cur_digit):
                    # five
                    identified[5]=_cur_digit
                else:
                    # two
                    identified[2]=_cur_digit
            # 6-segment
            if len(_cur_digit) == 6:
                if letter_in_string(four, _cur_digit):
                    # nine
                    identified[9]=_cur_digit
                elif not letter_in_string(four,_cur_digit) and letter_in_string(seven,_cur_digit):
                    # zero
                    identified[0]=_cur_digit
                else:
                    # six
                    identified[6]=_cur_digit
        #print("check", not None in identified)
        
        code = ""
        for j in range(4):
            for s_idx in range(10):
                if same_letters(identified[s_idx],_cur_msg[j]):
                    code+=str(s_idx)
        total_sum += int(code)
    print(total_sum)
