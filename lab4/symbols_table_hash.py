import copy
import utils


class SymbolsTable:
    def __init__(self):
        self.__content = {}
        self.__capacity = 256

    def get_content(self):
        return self.__content

    def add_symbol(self, symbol):
        if len(self.__content) == self.__capacity:
            self.__rehash()
        tries = 0
        key = utils.hash_code(self.__capacity, symbol, 0)
        while tries < self.__capacity and key in self.__content:
            if self.__content[key] == symbol:
                return key
            tries += 1
            key = utils.hash_code(self.__capacity, symbol, tries)
        self.__content[key] = symbol
        return key

    def __rehash(self):
        self.__capacity *= 2
        oldContent = copy.deepcopy(self.__content)
        self.__content = {}
        print(oldContent)
        print(self.__content)
        for key in oldContent:
            self.add_symbol(oldContent[key])

    def search(self, symbol):
        tries = 0
        key = utils.hash_code(self.__capacity, symbol, 0)
        while tries < self.__capacity and key in self.__content:
            if self.__content[key] == symbol:
                return key
            tries += 1
            key = utils.hash_code(self.__capacity, symbol, tries)
        return None

    def __str__(self):
        res = ''
        for key in self.__content:
            res += 'pos: ' + str(key) + ' symbol: ' + self.__content[key] + '\n'
        return res

# if __name__ == '__main__':
#     table = SymbolsTable()
#
#     table.add_symbol(2)
#     table.add_symbol('bc')
#     table.add_symbol(2.3)
#     table.add_symbol('bc')
#     table.add_symbol('a')
#
#     print(table.search(3))
#     print(table.search('bc'))
#     print(table.get_content())
