class Team:

    def __init__(self, name):
        self.name = name
        self.favorites = []

    def favorite(self, emp):
        self.favorites.append(emp)
        return self.favorites

    def top_choice(self):
        return self.favorites[0]

class Employee:

    def __init__(self, name):
        self.name = name
        self.favorites = []

    def favorite(self, team):
        self.favorites.append(team)
        return self.favorites

    def top_choice(self):
        return self.favorites[0]

matches = {}

def match_score(class1, class2):
    score = 0
    if class1 == class2.top_choice() and class2 == class1.top_choice():
        if class1.name not in matches.keys() and class2.name not in matches.values():
            matches[class1.name] = class2.name
            matches[class2.name] = class1.name
        score = 1
    elif class1 in class2.favorites or class2 in class1.favorites:
        score = 2
        if class1.name not in matches.keys() and class2.name not in matches.values():
            matches[class1.name] = class2.name
            matches[class2.name] = class1.name

    return score, matches
