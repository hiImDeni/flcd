class PIF:
    def __init__(self):
        self.__content = []

    def add(self, pos, value):
        self.__content.append((pos, value))

    def __str__(self):
        res = ''
        for tup in self.__content:
            res += 'pos: ' + str(tup[0]) + " value: " + str(tup[1]) + '\n'
        return res
