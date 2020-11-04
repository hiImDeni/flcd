from transitions import Transitions


class FiniteAutomaton:
    def __init__(self):
        self.q = set()  # states
        self.alphabet = set()  # sigma
        self.transitions = Transitions()
        self.F = set()  # final states
        self.__file = "fa.in"
        self.__read_file()

    def __read_file(self):
        with open(self.__file, 'r') as file:
            self.q = file.readline().strip().split(' ')
            self.alphabet = file.readline().strip().split(' ')
            self.__q0 = self.q[0]
            self.F = file.readline().strip().split(' ')
            line = file.readline().strip()
            while line:
                line = line.split(' ')
                for i in range(2, len(line)):
                    self.transitions.add(line[0], line[1], line[i])
                line = file.readline().strip()

    def is_deterministic(self):
        keys = self.transitions.get_keys()
        for start in keys:
            if len(self.transitions.get_transitions(start) > 1):
                return False
        return True
