def find_show_addiction_number(data):
    # get last episode each user watched
    # count viewers
    shows = {}
    output = {}
    for entry in data:
        viewers = shows.setdefault(entry['shows'], dict())
        max_num_shows = max(viewers.get(entry['u_id'], 1), entry['episode'])
        viewers[entry['u_id']] = max_num_shows
    for show in shows:
        count = [0] * 10
        viewers = shows[show]
        # updating count with viewers max number
        for viewer in viewers:
            max_episode = viewers[viewer] - 1
            count[max_episode] += 1
        total_viewers = len(viewers)
        threshold = total_viewers * 0.3
        counter = 0
        for i in range(10):
            counter += count[i]
            if counter >= threshold:
                break
        output[show] = i + 1

    return output
