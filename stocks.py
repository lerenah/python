'''
Stock Price Class
'''

class StockPrices:

    def __init__(self):
        self.stocks = []

    def addPrice(self, stock, price):
        counter = 0
        if price <= 0:
            return 'Price must be a positive integer.'

        while counter < len(self.stocks):
            if stock == self.stocks[counter]['name']:
                self.stocks[counter]['price'].append(price)
                return
            counter += 1

        self.stocks.append({'name': stock, 'price': [price]})

    def getPrices(self, stock, n):
        if n <= 0:
            return 'The number of prices requested must be a positive integer.'
        for el in self.stocks:
            if stock == el['name']:
                total_stocks = len(el['price'])
                if n in range(total_stocks):
                    return el['price'][:n]
                elif n > len(el['price']):
                    return el['price']
            else:
                continue

        else:
            return 'This stock is not yet in our listing.'
