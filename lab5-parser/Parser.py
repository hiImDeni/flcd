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

    def goto(self, state, symbol):
        for el in state:
            for values in state[el]:
                for i in range(len(values) - 1):
                    if values[i] == '.' and values[i + 1] == symbol:

                        aux = values[i]
                        values[i] = values[i + 1]
                        values[i + 1] = aux

                        if values[-1] != '.':
                            return self.closure((el, values))
                        else:
                            return {el: [values]}
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
                        gotoResult = self.goto(state, symbol)
                        if gotoResult != [] and gotoResult not in statesCopy:
                            states.append(gotoResult)
                            statesCopy.append(copy.deepcopy(gotoResult))

            if aux == statesCopy:
                return statesCopy

    def construct_table(self):
        c = self.ColCan()

    def action(self, state):
        keys = list(state.keys())

        if len(keys) == 1:
            if keys[0] == 'Z':
                if len(state['Z']) == 1:
                    if state['Z'][0][-1] == '.':
                        return "acc"

            first_key = state[keys[0]]
            if len(first_key) == 1:
                if first_key[0][-1] == '.':
                    prod_index = -1
                    for prod in self.grammar.productions:
                        for el in self.grammar.productions[prod]:
                            prod_index += 1

                            if prod == keys[0]:
                                if el == first_key[0][:-1]:
                                    return "reduce", prod_index

        return "shift"

    def buildTable(self, states):
        table = []

        for s in range(len(states)):
            action = self.action(states[s])
            goto = {}

            for symbol in self.grammar.non_terminals + self.grammar.terminals:
                gotoResult = self.goto(states[s], symbol)

                # gotoResultCopy = copy.deepcopy(gotoResult)
                # for el in gotoResultCopy:
                #    gotoResultCopy[el].sort()

                # statesCopy = copy.deepcopy(states)
                # for s in statesCopy:
                #    for el in s:
                #        s[el].sort()

                if gotoResultCopy in statesCopy:
                    goto[symbol] = states.index(gotoResult)

            table.append((s, action, goto))

        return table

    def parse(self, word):
        states = self.ColCan()
        print(states)

        table = self.buildTable(states)
        print(table)

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
