FN = "input.txt"

N_CYCLES = 256

with open(FN,"r") as f:
    init_state_s = f.readline().split(",")
    sea = [0 for _ in range(9)]
    for age in init_state_s:
        sea[int(age)]+= 1
    
    print("init state:", sea)

    for i in range(N_CYCLES):
        new_sea = [sea[j+1] for j in range(8)]
        new_sea = new_sea + [sea[0]]
        new_sea[6] += sea[0]
        sea = new_sea
        #print("After {} cycle: {} = {}".format(i+1, sea, sum(sea)))


    print(sum(sea))
