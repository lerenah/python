class Node:
    def __init__(self, value):
        self.value = value
        self.highest_seen = value

import random
nodes = [Node(9), Node(4), Node(27), Node(13)]

def gossip(nodes):
    highest_set = False
    num_rounds = 0
    while not highest_set:
        for node in nodes:
            k = random.randint(0, len(nodes) - 1)
            if node.highest_seen > nodes[k].highest_seen:
                nodes[k].highest_seen = node.highest_seen
        num_rounds += 1
        i = 0
        for node in nodes:
            if i in range(len(nodes)):
                if node[i].highest_seen != node[i + 1].highest_seen:
                    highest_seen = False
            break
        else:
            i += 1
        if i == len(nodes):
            highest_set = True
