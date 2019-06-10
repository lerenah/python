class Airport:
    def __init__(self):
        self.hashMap = {}
        self.possible_routes = []


    def add_routes(self, start, destination):
        if start not in self.hashMap.keys():
            self.hashMap[start] = [destination]
        else:
            self.hashMap[start].append(destination)

        if destination not in self.hashMap.keys():
            self.hashMap[destination] = [start]
        else:
            self.hashMap[destination].append(start)

    def print_all_routes(self, start, destination, visitedArr=[]):
        if len(visitedArr) == 0:
            visitedArr = [start]

        for idx, el in enumerate(self.hashMap[start]):

            current = self.hashMap[start][idx]

            if current not in visitedArr:
                visitedArr.append(current)
                if current == destination:
                    arrCopy = []
                    arrCopy.extend(visitedArr)
                    self.possible_routes.append(arrCopy)

                    visitedArr.pop()
                    visitedArr.pop()

                else:
                    self.print_all_routes(current, destination, visitedArr)

        return self.possible_routes
