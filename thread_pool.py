def run():
    # never stops
    while True:
        lock()
        if len(jobs) == 0:
            wait()
        item = jobs.pop(0)
        # unlock - hold for a short time only
        unlock()
        item()


def enqueue(job):
    #call lock / obtain lock first
    lock()
    # append
    jobs.append(job)
    signal()
    # remember to unlock
    unlock()
