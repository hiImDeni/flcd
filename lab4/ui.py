from finite_automaton import FiniteAutomaton


class UI:
    def __init__(self):
        self.__fa = FiniteAutomaton()

    @staticmethod
    def print_menu():
        print("Options: ")
        print("     Exit - 0")
        print("     Print states - 1")
        print("     Print alphabet - 2")
        print("     Print transitions - 3")
        print("     Print final states - 4")

    def run(self):
        while True:
            UI.print_menu()
            option = int(input("Choose option: "))
            if option == 0:
                break
            elif option == 1:
                for i in self.__fa.q:
                    print(i)
            elif option == 2:
                for i in self.__fa.alphabet:
                    print(i)
            elif option == 3:
                print(self.__fa.transitions)
            elif option == 4:
                for i in self.__fa.F:
                    print(i)
            else:
                print("Incorrect option")


if __name__ == '__main__':
    ui = UI()
    ui.run()
