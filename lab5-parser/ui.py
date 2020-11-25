from Parser import Parser
from grammar import Grammar


class UI:
    def __init__(self):
        self.__grammar = Grammar()
        self.__parser = Parser()

    @staticmethod
    def print_menu():
        print('Options are:')
        print('     0 - Exit')
        print('     1 - See non-terminals')
        print('     2 - See terminals')
        print('     3 - See productions')
        print('     4 - See start')

    def run(self):
        while True:
            UI.print_menu()
            option = input('Enter option: ')
            if option == '0':
                break
            elif option == '1':
                print(self.__grammar.get_non_terminals_string())
            elif option == '2':
                print(self.__grammar.get_terminals_string())
            elif option == '3':
                print(self.__grammar.get_productions_string())
            elif option == '4':
                print(self.__grammar.start)
            else:
                print('Incorrect option')


if __name__ == '__main__':
    ui = UI()
    ui.run()
