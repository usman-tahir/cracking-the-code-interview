
def array_left_rotation(a, n, k):
    if (k == len(a)):
        return a
    else:
        for x in range(k):
            a.insert(len(a) - 1, a.pop(0))
        return a
        
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k)
print(*answer, sep = ' ')
