from collections import Counter

def number_needed(a, b):
    counter_a = Counter(a) # Count of letters in 'a'
    counter_b = Counter(b) # Count of letters in 'b'
    counter_a.subtract(counter_b)
    return sum(abs(count) for count in counter_a.values())

a = input().strip()
b = input().strip()

print(number_needed(a, b))
