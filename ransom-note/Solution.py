
def word_count(string):
    word_counts = {}
    for word in list(string):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def ransom_note(magazine, ransom):
    wc_magazine = word_count(magazine)
    wc_ransom = word_count(ransom)
    for key in wc_ransom:
        if wc_ransom[key] > wc_magazine[key] and key in wc_magazine:
            return False
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if answer:
    print("Yes")
else:
    print("No")
