"""
ID: dotekin1
LANG: PYTHON3
TASK: namenum
"""
def make_trie(words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict['*'] = '*'
    return root

def find_words(trie, number):
    if number == '':
        return [''] if '*' in trie else []
    
    words = []
    digit = number[0]
    
    if digit == '7':
        options = 'PRS'
    elif digit == '8':
        options = 'TUV'
    elif digit == '9':
        options = 'WXY'
    else:
        letter = ord('A') + (int(digit) - 2)*3
        options = chr(letter) + chr(letter+1) + chr(letter+2)
    
    for option in options:
        if option in trie:
            words_from_rest = find_words(trie[option], number[1:])
            words.extend([option + word for word in words_from_rest])
    
    return words

with open("namenum.in") as fin:
    number = fin.read().strip()

with open('dict.txt') as fin:
    names = fin.read().splitlines()

trie = make_trie(names)
words = find_words(trie, number)

if not words:
    words = ['NONE']

with open("namenum.out", "w") as fout:
    for word in words:
        fout.write(f"{word}\n")
