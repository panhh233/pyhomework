def huiwen(String):
    if String == String[::-1]:
        print('{}是回文数'.format(String))
    else:
        print('{}不是回文数'.format(String))

M = input()
huiwen(M)