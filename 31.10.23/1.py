s = input()
stack = []
k = 0
is_good = True
for i in s:
    k += 1
    if i in '({[':
        stack.append(i)
    elif i in ')}]':
        if not stack:
            is_good = False
            break
        open_bracket = stack.pop()
        if open_bracket == '(' and i == ')':
            continue
        if open_bracket == '{' and i == '}':
            continue
        if open_bracket == '[' and i == ']':
            continue
        is_good = False
        break
res = k
if is_good and len(stack) == 0:
    print('YES')
else:
    print('NO')
    print(res)
