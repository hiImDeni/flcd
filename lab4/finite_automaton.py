from transitions import Transitions


class FiniteAutomaton:
    def __init__(self, file):
        self.q = set()  # states
        self.alphabet = set()  # sigma
        self.transitions = Transitions()
        self.F = set()  # final states
        self.__file = file
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
                if line[0] not in self.q or line[1] not in self.q:
                    raise ValueError("State does not exist")
                for i in range(2, len(line)):
                    if line[i] not in self.alphabet:
                        raise ValueError("Symbol " + line[i] + " is not in the alphabet")
                    self.transitions.add(line[0], line[1], line[i])
                line = file.readline().strip()

    def is_deterministic(self):
        keys = self.transitions.get_keys()
        for start in keys:
            for letter in self.alphabet:
                if len(self.transitions.get_transitions_to(start, letter)) > 1:
                    return False
        return True

    def is_accepted(self, word):
        if not self.is_deterministic():
            return None
        currentState = self.__q0
        for char in word:
            nextTransitions = self.transitions.get_transitions_to(currentState, char)
            if len(nextTransitions) == 0:
                return False
            nextTransition = nextTransitions[0]
            currentState = nextTransition[0]
        if currentState not in self.F:
            return False
        return True
