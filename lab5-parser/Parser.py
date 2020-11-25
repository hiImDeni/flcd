import copy

from grammar import Grammar


class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def closure(self, element):
        # element is a tuple of the form (start, productions[start])

        c = {element[0]: element[1]}
        while True:
            aux = copy.deepcopy(c)

            i = 0
            for i in range (len(c.keys())):
                keys = list(c.keys())
                for j in keys[i]:
                    if j in self.grammar.non_terminals:
                        for k in self.grammar.productions[j]:
                            if len(k) == 1 and k[0] == '0':
                                pass
                            if j not in c.keys():
                                c[j] = []
                            if k not in c[j]:
                                c[j].append(k)
            if aux == c:
                return c

    def goto(self, state, symbol):
        for el in state:
            list = state[el]
            for values in list:
                for i in range(len(values)):
                    if i != len(values) - 1:
                        if values[i] == '.' and values[i+1] == symbol:
                            aux = values[i]
                            values[i] = values[i+1]
                            values[i+1] = aux

                            return self.closure((el, self.grammar.productions[el]))
        return []

    def ColCan(self):
        start = self.grammar.start
        c = []

        # self.grammar.productions[start][0].insert(0, '.')
        for nt in self.grammar.productions:
            for production in self.grammar.productions[nt]:
                production.insert(0, '.')
        s0 = self.closure((start, self.grammar.productions[start]))
        print(s0)

        c.append(s0)

        while True:
            aux = c

            for state in c:
                for symbol in self.grammar.non_terminals + self.grammar.terminals:
                    gotoResult = self.goto(state, symbol)
                    print(symbol)
                    print(gotoResult)
                    print()
                    if gotoResult is not [] and gotoResult not in c:
                        c.append(gotoResult)

            if aux == c:
                break
        return c

    def parse(self):
        c = self.ColCan()

grammar = Grammar()
parser = Parser(grammar)
parser.parse()