class Grammar:
    def __init__(self):
        self.non_terminals = []
        self.terminals = []
        self.productions = {}
        self.__file = "g1.txt"
        self.start = ""
        self.read_file()

    def read_file(self):
        with open(self.__file, 'r') as file:
            non_terminals = file.readline().strip().split(' ')
            for n in non_terminals:
                if n in self.non_terminals:
                    raise ValueError('Non terminal ' + n + ' already exists')
                else:
                    self.non_terminals.append(n)

            terminals = file.readline().strip().split(' ')
            for t in terminals:
                if t in self.terminals:
                    raise ValueError('Terminal ' + t + ' already exists')
                else:
                    self.terminals.append(t)

            self.start = self.non_terminals[0]
            line = file.readline().strip()
            while line:
                line = line.split(' ')
                if line[0] not in self.non_terminals:
                    raise ValueError("Non-terminal does not exist")
                self.productions[line[0]] = []
                for i in range(1, len(line)):
                    for char in line[i]:
                        if char not in self.terminals and char not in self.non_terminals:
                            raise ValueError("Symbol " + line[i] + " is not defined")
                    self.productions[line[0]].append(line[i])
                line = file.readline().strip()

    def get_non_terminals_string(self):
        res = ''
        for i in self.non_terminals:
            res += i + ' '
        return res

    def get_terminals_string(self):
        res = ''
        for i in self.terminals:
            res += i + ' '
        return res

    def get_productions_string(self):
        res = ''
        for i in self.productions:
            res += i + ' -> '
            for symbol in self.productions[i]:
                res += symbol + ' | '
            res = res[:-2]
            res += '\n'
        return res
