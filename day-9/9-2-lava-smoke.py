FN = "input.txt"

def get_neighbors(col_idx, row_idx, n_cols, n_rows):
    neighs = []
    if col_idx - 1 >= 0:
        neighs.append([row_idx,col_idx-1])
    if row_idx - 1 >= 0:
        neighs.append([row_idx-1,col_idx])
    if col_idx + 1 < n_cols:
        neighs.append([row_idx,col_idx+1])
    if row_idx + 1 < n_rows:
        neighs.append([row_idx+1,col_idx])
    return neighs

def is_lowest_risk(col_idx, row_idx, n_cols, n_rows, h_map):
    neighs = get_neighbors(col_idx,row_idx,n_cols,n_rows)
    neigh_values = [h_map[neigh[0]][neigh[1]] for neigh in neighs]
    return min(neigh_values) > h_map[row_idx][col_idx]

def expand(col_idx, row_idx, n_cols, n_rows, h_map, explored):
    # get all possible neighbors
    neighs = get_neighbors(col_idx,row_idx,n_cols,n_rows)
    # removes neight with value of 9
    neighs = [neigh for neigh in neighs if h_map[neigh[0]][neigh[1]] != 9]
    # removes all explored neighs
    neighs = [neigh for neigh in neighs if not explored[neigh[0]][neigh[1]]]
    return neighs

def bfs(col_start, row_start, n_cols, n_rows, h_map, explored):
    open_list = [[row_start,col_start]]
    explored_tiles = 0
    while len(open_list) != 0:
        # pop new location
        cur_location = open_list.pop()
        # if already visited, just skip
        if explored[cur_location[0]][cur_location[1]]:
            continue 
        # set current location as explored
        explored[cur_location[0]][cur_location[1]] = True
        # increase number of explored positions by 1
        explored_tiles += 1
        # get neighbors
        neighs = expand(cur_location[1],cur_location[0],n_cols,n_rows,h_map,explored)
        # add neighs to the open list
        for neigh in neighs:
            open_list.append(neigh)
    return explored_tiles

with open(FN,"r") as f:
    lines = f.readlines()
    n_cols = len(lines[0].strip())
    n_rows = len(lines)

    h_map = []
    explored = []
    for line in lines:
        map_line = []
        explored_line = []
        for num in line.strip():
            map_line.append(int(num))
            explored_line.append(False)
        h_map.append(map_line)
        explored.append(explored_line)

    # look for lowest risks
    basins = []
    for row_idx in range(n_rows):
        for col_idx in range(n_cols):
            if is_lowest_risk(col_idx,row_idx,n_cols,n_rows,h_map):
                explored_tiles = bfs(col_idx,row_idx,n_cols,n_rows,h_map,explored)
                basins.append(explored_tiles)
    
    # sort basing    
    basins.sort()
    
    # get last (biggest) basins
    print(basins[-1]*basins[-2]*basins[-3])

