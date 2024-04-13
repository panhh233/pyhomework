def huiwen(String):
    if String == String[::-1]:
        return '{}是回文数'.format(String)
    else:
        return '{}不是回文数'.format(String)

M = input()
print(huiwen(M))