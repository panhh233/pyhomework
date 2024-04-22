class BMI(object):
    def __init__(self, height, weight) -> None:
        self.bmi = weight / height ** 2

    def printBMI(self):
        print('您的BMI指数是：{:.1f}'.format(self.bmi))

class ChinaBMI(BMI):
    
    def printBMI(self):
        print('您的BMI指数是：{:.1f}'.format(self.bmi))

        if self.bmi < 18.5:
            print('偏瘦，相关疾病发病的危险性：低')
        elif 18.5 <= self.bmi <= 23.9:
            print('正常，相关疾病发病的危险性：平均水平')
        elif 23.9 < self.bmi <= 26.9:
            print('偏胖，相关疾病发病的危险性：增加')
        elif 26.9 < self.bmi <= 29.9:
            print('肥胖，相关疾病发病的危险性：中度增加')
        else:
            print('重度肥胖，相关疾病发病的危险性：严重增加')

Height = eval(input())
Weight = eval(input())
person = ChinaBMI(Height, Weight)
person.printBMI()