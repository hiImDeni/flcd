from finite_automaton import FiniteAutomaton
from symbols_table_hash import SymbolsTable
from validate_token import Token
from pif import PIF


class Scanner:
    def __init__(self, file):
        self.__symbols_table = SymbolsTable()
        self.__types = ['int', 'real', 'char', 'string', 'bool', 'array', 'none']
        self.__operators = ['<', '>', '=', '!', '+', '-', '/', '%', '*', ':=', '&', '|']
        self.__reserved_words = self.__types + ['if', 'else', 'while', 'then', 'do', 'print', 'read', 'return', 'main']
        self.__separators = ['[', ']', '(', ')', '.', '{', '}', ';', ':']
        self.__pif = PIF()
        self.__file = file
        self.__set_files()
        self.__errors = set()
        self.__check_integer = FiniteAutomaton('constants/integer_const.in')
        self.__check_bool = FiniteAutomaton('constants/bool_const.in')
        self.__check_char = FiniteAutomaton('constants/char_const.in')
        self.__check_string = FiniteAutomaton('constants/string_const.in')

    def __check_token(self, tok, line):
        tok = tok.strip()
        token = Token(tok)
        if tok in self.__reserved_words:
            self.__pif.add(0, tok)
            return True
        elif token.is_identifier() or token.is_constant():
            key = self.__symbols_table.add_symbol(token.token)
            self.__pif.add(key, 'id')
            return True
        return False

    def get_tokens(self):
        with open(self.__file, 'r') as file:
            for i, line in enumerate(file):
                statement = line.strip()

                tokens = statement.split(' ')
                for tok in tokens:
                    if tok == '':
                        continue
                    tok = tok.strip()
                    if tok in self.__reserved_words or tok in self.__operators or tok in self.__separators:
                        self.__pif.add(0, tok)

                    elif self.__check_token(tok, i):
                        continue
                    else:
                        symbol = ''
                        operands = []
                        for char in tok:
                            if char in self.__separators or char in self.__operators:
                                if symbol != '':
                                    operands.append(symbol)
                                symbol = ''
                                self.__pif.add(0, char)
                            else:
                                symbol += char
                        if symbol != '' and symbol not in operands:
                            operands.append(symbol)
                        for operand in operands:
                            if not self.__check_token(operand, i):
                                error = 'Line ' + str(line) + ': Lexical error: unknown token ' + operand
                                if error not in self.__errors:
                                    self.__errors.add(error)

    def __set_files(self):
        problem = self.__file.split('.')[0]
        self.__st_file = problem + '_st.out'
        self.__pif_file = problem + '_pif.out'
        self.__error_file = problem + '_errors.out'

    def write_files(self):
        with open(self.__st_file, 'w') as st:
            st.write(str(self.__symbols_table))
        with open(self.__pif_file, 'w') as pif:
            pif.write(str(self.__pif))
        with open(self.__error_file, 'w') as errors:
            for err in self.__errors:
                errors.write(err + '\n')

