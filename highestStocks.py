class Stocks:
    def __init__(self):
        self.trades = {}

    def add_trade(self, stock, price):
        if stock not in self.trades.keys():
            self.trades[stock] = price
        else:
            self.trades[stock] += price

    def get_top_stocks(self):
        trades = []
        for key, val in self.trades.items():
            trades.append((key, val))
        trades = sorted(trades, key=lambda tup: (-tup[1], tup[0]))
        return trades[:4]
