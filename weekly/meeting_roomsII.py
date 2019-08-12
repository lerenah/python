def minMeetingRooms(self, intervals):
  """
  :type intervals: List[List[int]]
  :rtype: int
  """
  if len(intervals) == 0:
      return 0
  if len(intervals) == 1:
      return 1
  intervals.sort()
  meetings = [intervals[0][-1]]
  for start, end in intervals[1:]:
      if min(meetings) > start:
          meetings.append(end)
  return len(meetings)

# optimal solution
if len(intervals) == 0:
  return 0
intervals.sort(key=lambda x: x[0])
meetings = set()
rooms = 0
for start, end in intervals:
  if not len(meetings):
      rooms += 1
  else:
      if start < min(meetings):
          rooms += 1
      else:
          meetings.remove(min(meetings))
  meetings.add(end)
return rooms
