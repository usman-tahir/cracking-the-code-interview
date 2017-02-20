
def shorter_word(a, b):
    if len(a) < len(b):
        return a
    return b

def longer_word(a, b):
    if len(a) >= len(b):
        return a
    return b

def letter_count(s):
    letter_counts = {}
    for letter in list(s):
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts

def number_needed(a, b):
    print(letter_count(a))
    print(letter_count(b))
    total = 0
    longer = longer_word(a, b)
    shorter = shorter_word(a, b)
    for letter in list(longer):
        if letter in list(shorter):
            total += 1
    return ((len(a) + len(b)) - (total * 2))

a = input().strip()
b = input().strip()

print(number_needed(a, b))
