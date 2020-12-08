import copy

from grammar import Grammar


class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def closure(self, element):
        # element is a tuple of the form (start, productions[start])

        productions = copy.deepcopy(self.grammar.productions)

        c = {element[0]: [element[1]]}

        while True:
            aux = copy.deepcopy(c)

            idx = element[1].index('.')

            for el in c[element[0]]:
                for symbol in el:
                    if el.index(symbol) > idx:
                        if symbol in self.grammar.non_terminals:
                            for k in productions[symbol]:
                                if len(k) == 1 and k[0] == '0':
                                    pass
                                if symbol not in c.keys():
                                    c[symbol] = []
                                if k not in c[symbol]:
                                    k.insert(0, '.')
                                    c[symbol].append(k)
            if aux == c:
                return c

    def goto(self, state, symbol, productions):
        for el in state:
            # rhp = copy.deepcopy(state[el])

            for values in state[el]:
                for i in range(len(values) - 1):
                    if values[i] == '.' and values[i + 1] == symbol:

                        aux = values[i]
                        values[i] = values[i + 1]
                        values[i + 1] = aux

                        if values[-1] != '.':
                            return self.closure((el, values))
                        else:
                            return {el: values}
        return []

    def ColCan(self):
        start = self.grammar.start
        productionsCopy = copy.deepcopy(self.grammar.productions)

        states = []
        statesCopy = []

        for nt in productionsCopy:
            for production in productionsCopy[nt]:
                production.insert(0, '.')

        s0 = self.closure((start, productionsCopy[start][0]))

        states.append(s0)
        statesCopy.append(copy.deepcopy(s0))

        while True:
            aux = statesCopy
            for state in states:
                for symbol in self.grammar.non_terminals + self.grammar.terminals:
                    if symbol != self.grammar.start:
                        gotoResult = self.goto(state, symbol, productionsCopy)
                        if gotoResult:
                            print(symbol)
                            print(gotoResult)
                            print()
                        if gotoResult != [] and gotoResult not in statesCopy:
                            states.append(gotoResult)
                            statesCopy.append(copy.deepcopy(gotoResult))

            if aux == statesCopy:
                return statesCopy

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
