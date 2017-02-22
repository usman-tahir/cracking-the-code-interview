def is_matched(expression):
    if len(expression) % 2 != 0:
        return False
    else:
        pairs = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for e in expression:
            if e in pairs.keys():
                stack.append(pairs[e])
            elif len(stack) > 0 and e == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
