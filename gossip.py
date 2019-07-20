class Node:
    def __init__(self, value):
        self.value = value
        self.highest_seen = value

list_of_nodes = [Node(36), Node(10), Node(46), Node(54), Node(19), Node(42)]

import random

nodes = [Node(9), Node(4), Node(27), Node(13)]

def gossip(nodes):
    highest_set = False
    num_rounds = 0
    while not highest_set:
        for node in nodes:
            n = len(nodes) - 1
            k = random.randint(0, n)
            if node.highest_seen > nodes[k].highest_seen:
                nodes[k].highest_seen = node.highest_seen
            elif nodes[k].highest_seen > node.highest_seen:
                node.highest_seen = nodes[k].highest_seen
        num_rounds += 1
        i = 0
        while i + 1 in range(len(nodes)):
            if nodes[i].highest_seen != nodes[i + 1].highest_seen:
                highest_seen = False
                break
            else:
                i += 1
        if i == len(nodes) - 1:
            highest_set = True


    return nodes[0].highest_seen, num_rounds

# each node reads the next node and stores highest value so far

print(gossip(list_of_nodes))
