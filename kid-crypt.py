import os
import random
import re
import sys
import textwrap

class KidCrypt:
    clues = []
    crypt_dict = {}

    def __init__(self):
        used = {}
        random.seed(4) # https://xkcd.com/221/
        for c in range(ord('a'), ord('z') + 1):
            self.add_char(chr(c), used)
        for c in range(ord('0'), ord('9') + 1):
            self.add_char(chr(c), used)

        self.add_char('.', used)
        self.add_char(',', used)
        self.add_char('?', used)
        self.add_char('!', used)

        self.add_char(':', used)
        self.add_char(';', used)
        self.add_char('=', used)
        self.add_char('-', used)
        self.add_char('"', used)

    def add_char(self, ch, used):
        for attempts in range(20):
            value = random.randrange(10,80)
            if value in used:
                continue
            self.crypt_dict[ch] = value
            used[value] = 1
            return
        raise "Cannot add character"

    def add_clue(self, clue):
        self.clues.append(clue)

    def print_key(self):
        print("Secret key:")

        columns = []
        for column in range(0, 5):
            columns.append("  ")

        column = 0
        format_str = '{} {}    '
        for (ch, value) in sorted(self.crypt_dict.items(), key=lambda x: x[1]):
            columns[column] += format_str.format(value, ch)
            column += 1
            if column >= columns.__len__():
                column = 0

        for column in columns:
            print(column)
        print()

    def print_plaintext_clues(self):
        for index, clue in enumerate(self.clues, start=1):
            print("Clue {}:".format(index))
            self.print_wrapped(clue, space = ' ', end = '')
        print("\n")

    def print_encrypted_clues(self):
        for index, clue in enumerate(self.clues, start=1):
            print("Clue {}:".format(index))
            result = ""
            for ch in clue.lower():
                if ch in self.crypt_dict:
                    result += f'{self.crypt_dict[ch]}-'
                else:
                    result += "__ "
            self.print_wrapped(result, space = '  ', end = '\n\n')
            print()
        print()

    def print_wrapped(self, text, space, end):
        wrap = textwrap.wrap(text, width=40, initial_indent='  ', subsequent_indent='  ')
        for line in wrap:
            line = re.sub('-', ' ', line)
            line = re.sub(' ', space, line)
            print(line)
            print('', end = end) 


# Load the clues
path = os.path.join(sys.path[0], "clues.txt")
file = open(path, 'r')
clues = file.readlines()
file.close()

# Add clues to database
crypt = KidCrypt()
for clue in clues:
    clue = clue.strip()
    if not clue:
        continue
    clue = re.sub(' +', ' ', clue)
    crypt.add_clue(clue)

# Print key and clues
crypt.print_plaintext_clues()
crypt.print_encrypted_clues()
crypt.print_key()
