class Transitions:
    def __init__(self):
        self.__content = {}

    def add(self, start, end, value):
        if start in self.__content.keys():
            self.__content[start].append((end, value))
        else:
            self.__content[start] = [(end, value)]

    def get_transitions(self, start):
        return self.__content[start]

    def get_keys(self):
        return self.__content.keys()

    def __str__(self):
        res = ''
        for start in self.__content:
            for tup in self.__content[start]:
                res += start + ' -> ' + str(tup[0]) + ' : ' + str(tup[1]) + '\n'
        return res
