def tournament(n):
    q1 = []
    q2 = []
    teams = []
    # sets up first round
    for i in range(n):
        if i >= (n / 2):
            q2.append(i+1)
            teams.append([q1[i - len(q1)], q2[i - len(q1)]])
        else:
            q1.append(i+1)
    rounds = []
    rounds.append(teams)

    # start shifting for rounds
    j = 0
    while j < (n - 2):
        # look at second el in q1
        q2.insert(0, q1.pop(1))
        q1.append(q2.pop())
        teams = []
        i = 0
        while i in range(len(q1)):
            teams.append([q1[i], q2[i]])
            i += 1
        rounds.append(teams)
        j += 1


    return rounds
