def lunar_rove(rover):
    if len(rover) == 1:
        return rover[1]
    farthest_distance = {}
    start = 0
    end = 0
    for loc, fuel in rover:
        end = start + 1
        if start == len(rover) - 1:
            end = 0
        next_loc = rover[end][0]
        if next_loc == 0:
            next_loc = 100
        curr_loc = start
        while fuel >= rover[end][0]:
            if loc not in farthest_distance:
                farthest_distance[loc] = abs(loc - next_loc) + rover[end][1]
            else:
                farthest_distance[loc] += rover[end][1]
            fuel = abs(next_loc - rover[curr_loc][0]) - fuel
            fuel += rover[end][1]
            end += 1
            next_loc = rover[end][0]
            # rotate the pointer back to start of array
            if curr_loc == len(rover) - 1:
                curr_loc = 0
            else:
                curr_loc += 1
        start += 1
    return max(list(farthest_distance.values()))
