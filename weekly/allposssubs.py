subs = []
def subSets(soFar, rest):
  if rest == '':
    subs.append(list(soFar))
    print(soFar)
    return soFar
  else:
    # include it
    subSets(soFar + rest[0], rest[1:])
    # exclude it
    subSets(soFar, rest[1:])


