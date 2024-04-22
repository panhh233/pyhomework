class Vehicle(object):
    def __init__(self, speed, size, time, acceleration) -> None:
        self.speed = speed
        self.size = size
        self.time = time
        self.acceleration = acceleration

    def setSpeed(self, setspeed):
        self.speed = setspeed
        print('设置的初速度为:{}'.format(self.speed))

    def speedUp(self, time):
        self.speed += time * self.acceleration
        print('加速完后速度是:{}'.format(self.speed))

    def speedDown(self, time):
        self.speed -= time * self.acceleration

        if self.speed > 0:
            print('减速完后速度是:{}'.format(self.speed))
        else:
            print('减速完后速度是:0')

    def move(self):
        Upendspeed = self.speed + self.time * self.acceleration
        Downendspeed = self.speed - self.time * self.acceleration

        print('初速度:{} 加速度:{} 体积:{}'.format(self.speed, self.acceleration, self.size))
        print('设置的初速度为:{}'.format(self.speed))
        print('加速完后速度是:{}'.format(Upendspeed))

        if Downendspeed > 0:
            print('减速完后速度是:{}'.format(Downendspeed))
        else:
            print('减速完后速度是:0')

Speed = eval(input())
Size = eval(input())
Time = eval(input())
Acceleration = eval(input())

p = Vehicle(Speed, Size, Time, Acceleration)
p.move()