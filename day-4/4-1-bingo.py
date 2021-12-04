FN = "input.txt"

BINGO_GRID_SIZE = 5

def mark_the_number(bingo_table, marked_table, number):
    for row in range(BINGO_GRID_SIZE):
        for col in range(BINGO_GRID_SIZE):
            if bingo_table[row][col] == number:
                marked_table[row][col] = 1
                return row, col
    return -1, -1

def check_bingo(marked_table, row, col):
    if row == -1:
        return False
    else:
        # check row
        for _row in range(BINGO_GRID_SIZE):
            if marked_table[_row][col] == 1:
                if _row == (BINGO_GRID_SIZE - 1):
                    return True
            else:
                break
        # check col
        for _col in range(BINGO_GRID_SIZE):
            if marked_table[row][_col] == 1:
                if _col == (BINGO_GRID_SIZE - 1):
                    return True
            else:
                break
        return False

def sum_unmarked(bingo_table, marked_table):
    total_sum = 0
    for row in range(BINGO_GRID_SIZE):
        for col in range(BINGO_GRID_SIZE):
            if marked_table[row][col] == 0:
                total_sum += bingo_table[row][col]
    return total_sum

with open(FN, "r") as f:
    lines = f.readlines()
    # get total number of tables
    n_bingo_tables = (len(lines)-1)//(BINGO_GRID_SIZE + 1)
    # get drawn numbers
    drawn_numbers = [int(num) for num in lines[0].split(",")]
    
    # parse bingo tables
    bingo_tables = []
    marked_tables = []
    for bingo_table_idx in range(n_bingo_tables):
        _bingo_table = []
        _marked_table = []
        for row in range(BINGO_GRID_SIZE):
            _cur_idx = 1+bingo_table_idx*(BINGO_GRID_SIZE+1)+row+1
            _cur_row = [int(num) for num in lines[_cur_idx].split()]
            _bingo_table.append(_cur_row)
            _marked_table.append([0 for _ in range(BINGO_GRID_SIZE)])
        bingo_tables.append(_bingo_table)
        marked_tables.append(_marked_table)
    
    #print(marked_tables)

    # roll and check
    is_there_bingo = False
    for num in drawn_numbers:
        for table_idx in range(n_bingo_tables):
            # try to mark in marked tables
            row, col = mark_the_number(bingo_tables[table_idx], marked_tables[table_idx], num)
            # check for bingo
            is_there_bingo = check_bingo(marked_tables[table_idx], row, col)
            # if there is a bingo, just sum all unmarkd cells
            if is_there_bingo:
                res = sum_unmarked(bingo_tables[table_idx], marked_tables[table_idx])
                print(num*res)
                break
        if is_there_bingo:
            break

