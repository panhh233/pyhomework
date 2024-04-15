Score = int(input())

def passed(score):
    if 0 <= score < 60:
        print('该同学成绩不合格，需继续努力！')
    elif 60 <= score <= 100:
        print('该同学成绩合格啦！')
    else:
        print('输入的成绩错误！')
    
passed(Score)