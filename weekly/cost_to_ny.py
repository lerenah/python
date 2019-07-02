def cost_to_fly(coders):
    to_ny = []
    to_sf = []
    for ny, sf in coders:
        if ny > sf:
            if len(to_sf) < (len(coders) // 2):
                to_sf.append(sf)
        else:
            to_ny.append(ny)

    return sum(to_ny) + sum(to_sf)
