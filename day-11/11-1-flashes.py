FN = "test-input.txt"
N_STEPS = 10
GRID_SIZE = 10

# eight neighborhood
def get_neighs(row_idx, col_idx):
    neighs = []
    for row_off in range(-1,2):
        for col_off in range(-1,2):
            if row_off != 0 or col_off != 0:
                _row = row_idx + row_off
                _col = col_idx + col_off
                if _row >= 0 and _row < GRID_SIZE and _col >= 0 and _col < GRID_SIZE:
                    neighs.append([_row,_col])
    return neighs

# expand given position
#def expand(row_idx, col_idx, world, flashed):
#    neighs = get_neighs(row_idx, col_idx)
#
#    pass

def bfs(world):
    open_list = []
    closed_list = []
    
    
with open(FN,"r") as f:
    # parse files
    # '-> inspired by ARiskova's approach
    world = []
    for line in f:
        line = line.strip()
        world.append(list(map(int,[c for c in line])))
    print(world)

    # iterate over simulation steps
    for _ in range(N_STEPS):
        # 1) increase energy by 1flashed = []
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                world[i][j] += 1
        # 2) create flashed array, a.k.a. closed data structure
        flashed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    neighs = get_neighs(9,1,1)
    print(neighs)
        
        
