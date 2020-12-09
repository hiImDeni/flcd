import collections
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
        statesCopy = copy.deepcopy(states)
        for s in range(len(statesCopy)):
            action = self.action(states[s])
            goto = {}

            for symbol in self.grammar.non_terminals + self.grammar.terminals:
                gotoResult = self.goto(statesCopy[s], symbol)

                if gotoResult in states:
                    goto[symbol] = states.index(gotoResult)
            table.append((s, action, goto))

        return table

    def parse(self, word):
        states = self.ColCan()
        print(states)

        table = self.buildTable(states)
        print(table)

        beta = list(word)

        phi = []
        end = False

        statesCopy = copy.deepcopy(states)
        state = statesCopy[0]
        index = 0
        alpha = [index]

        while not end:
            action = self.action(statesCopy[index])
            if  action == 'shift':
                symbol = beta.pop(0)
                state = self.goto(statesCopy[index], symbol)
                # if new_state in states:
                index = states.index(state)
                alpha.append(symbol)
                alpha.append(index)
            elif action == 'acc':
                print('Success')
                end = True
            else:
                production = []
                key = ''
                production_index = action[1]
                i = 0
                while i < production_index:
                    for symbol in self.grammar.productions:
                        for prod in self.grammar.productions[symbol]:
                            i += 1
                            if i == production_index:
                                production = copy.deepcopy(prod)
                                key = symbol
                for _ in range(len(production)):
                    alpha.pop()
                    alpha.pop()
                alpha.append(key)

                state = self.goto(statesCopy[index], key)
                for j in range(len(alpha)-1, 0, -1):
                    if alpha[j] is int:
                        index = alpha[j]
                        break
                alpha.append(states.index(state))

    def search_production(self, l):
        pass


grammar = Grammar()
parser = Parser(grammar)
# word = input("Enter a word: ")
parser.parse("abbc")
