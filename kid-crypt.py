import random


class KidCrypt:
    clues = []
    crypt_dict = {}

    def __init__(self):
        random.seed(1)
        for c in range(ord('a'), ord('z')):
            self.add_char(c)
        for c in range(ord('0'), ord('9')):
            self.add_char(c)

    def add_char(self, ch):
        for attempts in range(20):
            value = random.randrange(10,99)
            if value in self.crypt_dict:
                continue
            self.crypt_dict[chr(ch)] = value
            return
        raise "Cannot add character"

    def add_clue(self, clue):
        self.clues.append(clue)

    def print_key(self):
        print("Decryption key:")
        format_str = '{} {}'
        for (ch, value) in sorted(self.crypt_dict.items(), key=lambda x: x[1]):
            print(format_str.format(value, ch))
        print("\n\n")

    def print_plaintext_clues(self):
        for index, clue in enumerate(self.clues, start=1):
            print("Clue {}:\n{}\n".format(index, clue))
        print("\n\n")

    def print_encrypted_clues(self):
        for index, clue in enumerate(self.clues, start=1):
            print("Clue {}:".format(index))
            count = 0
            for ch in clue.lower():
                if ch in self.crypt_dict:
                    print(f' {self.crypt_dict[ch]} ', end = '')
                else:
                    print(" _ ", end = '')
                count += 1
                if count % 16 == 0:
                    print()
            print("\n\n")

crypt = KidCrypt()

crypt.add_clue("Look under the kitchen sink")
crypt.add_clue("Inside the green chest")
crypt.add_clue("Behind the play room couch")

crypt.print_plaintext_clues()
crypt.print_key()
crypt.print_encrypted_clues()
