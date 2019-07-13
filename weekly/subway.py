from datetime import timedelta


class Subway:
    def __init__(self):
        self.info = {}
        self.pairs = {}

    def swipe_in(self, card, time, station):
        # datetime / collects data
        self.info[card] = (time, station)

    def swipe_out(self, card, time, station):
        # seconds
        start_time, start_station = self.info[card]
        diff = time - start_time
        total_time, count = self.pairs.get(
            (start_station, station), (timedelta(0), 0))
        total_time += diff
        count += 1
        self.pairs[(start_station, station)] = (total_time, count)

    def get_avg_between(self, A, B):
        if (A, B) not in self.pairs:
            raise Exception('No data available')
        total_time, count = self.pairs[(A, B)]
        return total_time.seconds / count
