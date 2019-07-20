key = [['A', "B", 'C', "D"],
['B' ,'C' ,'D'],
['C', 'D', 'E']]


def recommender(data, req):
    suggestions = {}
    for idx, val in enumerate(data):
        data[idx] = set(val)
    subset_songs = []
    for val in data:
        if all(r in val for r in req):
            subset_songs.append(val)
    for val in subset_songs:
        for song in val:
            count = suggestions.get(song, 0)
            suggestions[song] = count + 1
    most_popular = sorted(suggestions.keys(), key=lambda x: suggestions[x], reverse=True)

    most_popular = [x for x in suggestions if x not in req]
    print(most_popular)
    return most_popular

print(recommender(key, ('B', 'C')))
