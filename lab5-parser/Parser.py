import copy

from grammar import Grammar


class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def closure(self, element, productions):
        # element is a tuple of the form (start, productions[start])

        c = {element[0]: element[1]}
        while True:
            aux = copy.deepcopy(c)

            for i in range(len(c.keys())):
                keys = list(c.keys())
                for j in keys[i]:
                    if j in self.grammar.non_terminals:
                        for k in productions[j]:
                            if len(k) == 1 and k[0] == '0':
                                pass
                            if j not in c.keys():
                                c[j] = []
                            if k not in c[j]:
                                c[j].append(k)

            for el in element[1]:
                index = el.index('.')

                for symbol in el:
                    if el.index(symbol) > index:
                        if symbol in self.grammar.non_terminals:
                            for k in productions[symbol]:
                                if len(k) == 1 and k[0] == '0':
                                    pass
                                if symbol not in c.keys():
                                    c[symbol] = []
                                if k not in c[symbol]:
                                    c[symbol].append(k)
            if aux == c:
                return c

    def goto(self, state, symbol, productions):
        for el in state:
            rhp = copy.deepcopy(state[el])

            for values in rhp:
                for i in range(len(values)):
                    if i != len(values) - 1:
                        if values[i] == '.' and values[i + 1] == symbol:

                            aux = values[i]
                            values[i] = values[i + 1]
                            values[i + 1] = aux

                            return self.closure((el, rhp), productions)
        return []

    def ColCan(self):
        start = self.grammar.start
        productionsCopy = copy.deepcopy(self.grammar.productions)

        states = []

        for nt in productionsCopy:
            for production in productionsCopy[nt]:
                production.insert(0, '.')

        s0 = self.closure((start, productionsCopy[start]), productionsCopy)

        states.append(s0)
        print(states)

        while True:
            aux = states
            nr = 0
            for state in states:
                stateCopy = copy.deepcopy(state)
                for symbol in self.grammar.non_terminals + self.grammar.terminals:
                    if symbol != self.grammar.start:
                        gotoResult = self.goto(state, symbol, productionsCopy)
                        if gotoResult:
                            print(symbol + " " + str(nr))
                            print(gotoResult)
                            print()
                        if gotoResult is not [] and gotoResult not in states:
                            states.append(gotoResult)
                nr += 1

            if aux == states:
                return states

    def construct_table(self):
        c = self.ColCan()

    def action(self, state):
        pass

    def parse(self, word):
        states = self.ColCan()

        print(states)
        print(self.grammar.productions)

        beta = list(word)
        index = 0
        alpha = [index]
        phi = []
        end = False

        # while not end:
        #    state = states[index]
        #    if self.action(state) == 'shift':
        #        a = beta.pop(0)
        #        state = self.goto(state, a)
        #        alpha.append(a)
        #        alpha.append(index)
        #    elif self.action(state) == 'accept':
        #       print('success')
        #        end = True
        #    elif self.action(state) == 'error':
        #       print('error')
        #        end = True
        # elif len(self.action(state)) == 2 and self.action(state)[0] == 'reduce':
        #    l = self.action(state)[1]
        #    self.search_production(l)
        #    state = self.goto()
        #    alpha.pop()
        #   alpha.pop()
        #    phi.append(l)

    def search_production(self, l):
        pass


grammar = Grammar()
parser = Parser(grammar)
# word = input("Enter a word: ")
parser.parse("a")
