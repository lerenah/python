def check_fraud(board):
    transactions = {}
    holds = []
    next = []
    for row in board:
        i = 0
        name = row[i]
        i += 1
        amt = row[i]
        if amt > 1000:
            holds.append(row)
            continue
        if name not in transactions.keys():
            transactions[name] = row
        else:
            next.append(row)
        i += 1
        time = row[i]
        i += 1
        loc = row[i]
        if len(next):
            for el in next:
                if transactions[name][0] == el[0]:
                    if abs(time - transactions[name][2]) <= 60:
                        if loc != transactions[name][3]:
                            holds.append(row)
                            holds.append(transactions[name])
                            next.remove(row)
                            del transactions[name]
                            break
                        else:
                            next.remove(row)
                            transactions[name] = row
                    else:
                        next.remove(row)
                        transactions[name] = row


    return holds
