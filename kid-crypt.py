import random

chars = {}
random.seed(1)
for c in range(ord('a'), ord('z')):
    value = random.randrange(10,99)
    while value in chars:
        value = random.randrange(10,99)
    chars[chr(c)] = value

def print_key():
    print("Decryption key:")
    format_str = '{} {}'
    for (ch, value) in sorted(chars.items(), key=lambda x: x[1]):
        print(format_str.format(value, ch))
    print("\n\n")

def encrypt(index, message):
    print(f'Clue #{index}')

    count = 0
    for ch in message.lower():
        if ch in chars:
            print(f' {chars[ch]} ', end = '')
        else:
            print(" _ ", end = '')
        count += 1
        if count % 16 == 0:
            print()
    print("\n\n")
        
    
print_key()
encrypt(1, "Look under the kitchen sink")
encrypt(2, "Inside the green chest")
encrypt(3, "Behind the play room couch")
