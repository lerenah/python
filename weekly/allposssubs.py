subs = []
def subSets(accum, curr):
  if curr == '':
    subs.append(list(accum))
    print(accum)
    return accum
  else:
    # include it
    subSets(accum + curr[0], curr[1:])
    # exclude it
    subSets(accum, curr[1:])


