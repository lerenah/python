import datetime

def last_three():
    count = 0
    timer = datetime.timedelta(seconds=1)
    ran = False
    if ran:
        if count <= 3:
            return False
        elif timer > 3 and count == 3:
            return True
        ran = False
    def called(a, b):
        ran = True
        count += 1
        return a + b
