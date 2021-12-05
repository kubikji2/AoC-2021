FN = "input.txt"

with open(FN, "r") as f:
    lines = f.readlines()
    segments = []
    for line in lines:
        _segment = line.replace("\n","").replace(","," ").replace("->"," ").split()
        _segment = [int(point) for point in _segment]
        # only cosider horizontal or vertical lines
        if (_segment[0] == _segment[2]) or (_segment[1] == _segment[3]):
            segments.append(_segment)
    
    # get maximim dimension
    x_size = max([_segment[0] for _segment in segments] + [_segment[2] for _segment in segments])+1
    y_size = max([_segment[1] for _segment in segments] + [_segment[3] for _segment in segments])+1
    
    # create array
    pipe_map = [[0 for _ in range(x_size)] for _ in range(y_size)]
    
    # draw lines
    for segment in segments:
        x1,y1,x2,y2 = segment
        if x1 == x2:
            #print(segment, "is horizontal")
            y = min(y1,y2)
            Y = max(y1,y2)+1
            for i in range(y,Y):
                pipe_map[x1][i] += 1
        if y1 == y2:
            #print(segment, "is vertical")
            x = min(x1,x2)
            X = max(x1,x2)+1
            for i in range(x,X):
                pipe_map[i][y1] += 1

    # get total number of crossings
    n_crossings = 0
    for x in range(x_size):
        for y in range(y_size):
            if pipe_map[x][y] >= 2:
                n_crossings += 1

    print(n_crossings)
