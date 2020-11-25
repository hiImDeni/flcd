class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def closure(self, element):
        # element is a tuple of the form (start, productions[start])

        c = {element[0]: element[1]}
        while True:
            aux = c

            for i in c.keys():
                for j in c[i]:
                    if j in self.grammar.non_terminals:
                        for k in self.grammar.productions[j]:
                            if k not in c:
                                if j not in c.keys():
                                    c[j] = [k]
                                else:
                                    c[j].append(k)

            if aux == c:
                break

        return c

    def goto(self, state, symbol):
        for el in state:
            for i in range(len(el[1])):
                if i == len(el[1]) - 1:
                    if el[1][i] == '.' and el[1][i+1] == symbol:
                        aux = el[1][i]
                        el[1][i] = el[1][i+1]
                        el[1][i+1] = aux
                        
                        return self.closure(el)

        return []

    def ColCan(self):
        start = self.grammar.start
        c = set()

        self.grammar.productions[start].insert(0, '.')
        s0 = self.closure((start, self.grammar.productions[start]))

        c.add(s0)

        while True:
            aux = c

            for state in c:
                for symbol in self.grammar.terminals + self.grammar.non_terminals:
                    gotoResult = self.goto(state, symbol)
                    if gotoResult is not [] and gotoResult not in c:
                        c.add(gotoResult)

            if aux == c:
                break

        return c
