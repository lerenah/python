def helper(i, rover, circumference):
    distance = 0
    # wraps around trip - keeps track of where you are in the list
    j = (i + 1) % len(rover)
    fuel = 0
    while j != i:
        fuel += rover[j - 1][1]
        next_loc = rover[j][0]
        curr_loc = rover[j - 1][0]
        if next_loc > curr_loc:
            travel_dist = next_loc - curr_loc
        else:
            travel_dist = (circumference - curr_loc) + next_loc
        if fuel < travel_dist:
            # not enough fuel to get there
            distance += fuel
            fuel = 0
            break
        else:
            # enough fuel to get there
            distance += travel_dist
            fuel -= travel_dist
            j = (j + 1) % len(rover)
    # consume remaining fuel
    if j == i:
        distance += rover[j - 1][1]
    return distance


def lunar_rove(circumference, rover):
    if len(rover) == 1:
        return rover[1]
    # go through all of the indexes in the list and get the maximum and pair up the index with the max
    return max((helper(i, rover, circumference), i) for i in range(len(rover)))
