def isOpen(start, stop):
  open_hours = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 2, 3, 4, 5, 6]
  closed_hours = [21, 22, 23, 24, 1, 7, 8]
  for i in range(start, stop + 1):
      if i not in open_hours:
        print('FAILURE')
        return
      else:
        continue
  print('SUCCESS')


isOpen(4, 10)
