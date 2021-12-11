FN = "input.txt"

# decides whether the location is lowest among its neighbors
def is_lowest_risk(col_idx, row_idx, n_cols, n_rows, h_map):
    neighs = []
    if col_idx - 1 >= 0:
        neighs.append(h_map[row_idx][col_idx-1])
    if row_idx - 1 >= 0:
        neighs.append(h_map[row_idx-1][col_idx])
    if col_idx + 1 < n_cols:
        neighs.append(h_map[row_idx][col_idx+1])
    if row_idx + 1 < n_rows:
        neighs.append(h_map[row_idx+1][col_idx])
    return min(neighs) > h_map[row_idx][col_idx]

with open(FN,"r") as f:
    lines = f.readlines()
    n_cols = len(lines[0].strip())
    n_rows = len(lines)

    h_map = []
    for line in lines:
        map_line = []
        for num in line.strip():
            map_line.append(int(num))
        h_map.append(map_line)

    # look for lowest risks
    total_risk = 0
    for row_idx in range(n_rows):
        for col_idx in range(n_cols):
            if is_lowest_risk(col_idx,row_idx,n_cols,n_rows,h_map):
                total_risk += h_map[row_idx][col_idx] + 1
            #print("X" if is_lowest_risk(col_idx,row_idx,n_cols,n_rows,h_map) else " ", end="")
        #print()   

    print(total_risk)

