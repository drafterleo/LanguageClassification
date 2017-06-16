import networkx as nx
import random


# [(n, n, p), (n, n, p) ...]
def makeGraphByGrammar(grammar):
    G = nx.Graph()
    for i in xrange(len(grammar)):
        n1 = grammar[i][0]
        n2 = grammar[i][1]
        p = grammar[i][2]
        G.add_edge(n1, n2)
        G[n1][n2] = p
    return G


def genWordByGraph(G, maxLen = 10):
    node = 'in'
    word = ''
    while node != 'out' and len(word) < maxLen:
        if node != 'in':
            word += node
        ways = G.neighbors(node)
        if len(ways) == 0:
            break
        node = ways[random.randint(0, len(ways) - 1)]
        print node

    return word


grammar1 = [('in', 'a',   1.0),
            ('a',  'b',   0.5),
            ('a',  'c',   0.5),
            ('b',  'out', 1.0),
            ('c',  'out', 1.0)]

G = makeGraphByGrammar(grammar1)
print G.nodes()
print G.edges()
print G.neighbors('a')
print G['a']['b']

print genWordByGraph(G)
