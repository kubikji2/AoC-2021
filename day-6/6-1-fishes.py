FN = "test-input.txt"

N_CYCLES = 18

with open(FN,"r") as f:
    init_state_s = f.readline().split(",")
    sea = []
    for age in init_state_s:
        sea.append(int(age))
    
    #print("init state:", sea)

    for i in range(N_CYCLES):
        new_sea = []
        spawned = []
        for fish in sea:
            if fish == 0:
                fish = 7
                spawned.append(8)
            fish -= 1
            new_sea.append(fish)
        new_sea += spawned
        sea = new_sea
        print("After {} cycle: {}".format(i+1, len(sea)))

    print(len(sea))

