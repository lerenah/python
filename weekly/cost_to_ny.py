def cost_to_fly(coders):
    to_ny = []
    to_sf = []
    total_ny = 0
    total_sf = 0
    for ny, sf in coders:
        if ny > sf:
            if len(to_sf) < (len(coders) // 2):
                to_sf.append(sf)
                total_sf += sum(to_sf)
            else:
                total_ny += sf
                total_sf += sf
                if total_ny > total_sf:
                    total_ny -= sf
                    to_sf.append(sf)
                    total_sf -= sf
        else:
            to_ny.append(ny)
            total_ny += sum(to_ny)

    total = sum(to_ny) + sum(to_sf)

    return total
