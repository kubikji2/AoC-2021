FN = "input.txt"

with open(FN,"r") as f:
    crabs = f.readline().split(",")
    crabs = [int(s) for s in crabs]
    #print(crabs)

    most_distant_crab = max(crabs)+1
    crabs_at_pos =[0 for _ in range(most_distant_crab)]

    # for each possible location...
    min_fuel = None
    opt_idx = 0
    for dist in range(most_distant_crab):
        # compute current fuel consumption
        _cur_fuel = 0
        for crab_idx in crabs:
            _cur_fuel += abs(crab_idx-dist)

        if min_fuel is None or _cur_fuel < min_fuel:
            min_fuel = _cur_fuel
            opt_idx = dist

    print(opt_idx, min_fuel)