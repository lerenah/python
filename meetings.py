meetings = [(2,5), (4,7), (3,9), (1,5), (10, 20)]


def min_rooms_needed(arr):
    overlap = 0
    arr = sorted(arr, key=lambda x: x[0])
    for idx, time in enumerate(arr):
      if (idx + 1) in range(len(meetings)):
        next_meeting = arr[idx + 1]
        if time[1] > next_meeting[0]:
          overlap += 1
        elif time[1] == next_meeting[1]:
          overlap += 1
        elif time[0] > next_meeting[0] and time[1] > next_meeting[1]:
          overlap += 1
    return overlap + 1

print(min_rooms_needed(meetings))
