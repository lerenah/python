class RSI:
    def __init__(self):
        self.prices = []
        self.avg = 0

    def add_price(self, price):
        self.prices.append(price)

    def get_rsi(self, n):
        gains = 0
        losses = 0
        total_gains = 0
        total_losses = 0
        index = len(self.prices) - n
        prices = self.prices[index:]
        for idx, price in enumerate(prices):
            if idx != len(self.prices) - 1:
                if price > prices[idx + 1]:
                    losses += abs(price - prices[idx + 1])
                    total_losses += 1
                elif price < prices[idx + 1]:
                    gains += abs(price - prices[idx + 1])
                    total_gains += 1
        avg_gains = gains/total_gains
        avg_losses = losses/total_losses
        rsi = 100 - (100 / (1 + (avg_gains/avg_losses)))
        return rsi
