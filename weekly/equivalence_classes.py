def classify(input, equiv):
    output = []
    ins = input
    while len(ins) > 1:
        eq = []
        first = ins[0]
        i = 1
        while i in range(len(ins)):
            res = equiv(first, ins[i])
            if res and not len(eq):
                eq.append(first)
                eq.append(ins[i])
            elif res:
                eq.append(ins[i])
            elif not res and not len(eq):
                eq.append(first)
            elif not res:
                i += 1
                continue
            ins = [x for x in ins if x not in eq]
            i = 0
        output.append(eq)
    if len(ins):
        output.append(ins)

    return output
