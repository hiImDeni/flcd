class Transitions:
    def __init__(self):
        self.__content = {}

    def add(self, start, end, value):
        if start in self.__content.keys():
            self.__content[start].append((end, value))
        else:
            self.__content[start] = [(end, value)]

    def get_transitions(self, start):
        if start not in self.__content.keys():
            return []
        return self.__content[start]

    def get_transitions_to(self, start, value):
        transitions = []
        if start not in self.__content.keys():
            return []
        for transition in self.__content[start]:
            if transition[1] == value:
                transitions.append(transition)
        return transitions

    def get_keys(self):
        return self.__content.keys()

    def __str__(self):
        res = ''
        for start in self.__content:
            for tup in self.__content[start]:
                res += start + ' -> ' + str(tup[0]) + ' : ' + str(tup[1]) + '\n'
        return res
