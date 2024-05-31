def isValid(s: str):
    stack = []
    brakets = ['(', ')', '[', ']', '{', '}']
    dic = {')': '(', '{': '}', '[': ']'}

    for i in s:
        if i in brakets:
            if stack and i in dic:
                if dic[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
    return not stack

string = input()
if isValid(string):
    print('配对成功')
else:
    print('配对不成功')