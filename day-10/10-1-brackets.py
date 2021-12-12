FN = "input.txt"

def process_line(line):
    penalty = 0
    # opening brackets
    o_brackets = "([{<"
    # closing brackets
    c_brackets = ")]}>"
    # penalties for each bracket
    penalties = [3,57,1197,25137]
    # stack of opened bracket
    open_stack = []
    cur_line = ""
    for c in line:
        cur_line += c
        # if bracket is opening one...
        if c in o_brackets:
            # ... push its index to open stack
            open_stack.append(o_brackets.index(c))
        # if bracket is closing one...
        if c in c_brackets:
            # ... check whether the last open bracket on the stack matches
            stacked_b_idx = open_stack[-1]
            if stacked_b_idx == c_brackets.index(c):
                open_stack.pop()
            # ... otherwise compute penalty based on the wrong bracket
            else:
                penalty = penalties[c_brackets.index(c)]
                break
    return penalty

with open(FN, "r") as f:
    lines = f.readlines()
    penalty = 0
    for line in lines:
        penalty += process_line(line.strip())
    print(penalty)