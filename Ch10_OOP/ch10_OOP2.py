# 繼承


# class Car:
#
#     def __init__(self, year=1990, mpg=30000, speed=0):
#         self.year = year
#         self.mpg = mpg
#         self.speed = speed
#
#     def accelerate(self):
#         self.speed += 20
#         print('Speed Up:', self.speed)
#
#     def brake(self):
#         self.speed -= 10
#         print('Speed Down:', self.speed)
#
#
# class RaceCar(Car):
#
#     def __init__(self, color='', make='', engine='', year='', mpg=0, speed=0):
#         super(RaceCar, self).__init__(year, mpg, speed)
#         self.color = color
#         self.make = make
#         self.engine = engine
#
#     def turbo_start(self):
#         self.speed += 100
#         print('Turbo Mode Start Speed:', self.speed)
#
#     def brake(self):
#         super().brake()
#         print('ABS Mode Start')
#
#
# def main():
#     my_car = RaceCar('White', 'NISSAN GTR', 'V6', 2007, 3000, 0)
#     print(my_car.color, my_car.make, my_car.year)
#     my_car.accelerate()
#     my_car.turbo_start()
#     my_car.accelerate()
#     my_car.brake()
#
#     print('------------------------')
#     print('my_car is instance of RaceCar:', isinstance(my_car, RaceCar))
#     print('my_car is instance of Car:', isinstance(my_car, Car))
#     print('RaceCar is sub class of Car:', issubclass(RaceCar, Car))
#
#
# if __name__ == '__main__':
#     main()

# 多繼承
# -------------------------------------------------------------------------------------------

# class Base:
#     def __init__(self):
#         print("I'm base")
#
#
# class A(Base):
#     def __init__(self):
#         print("I'm A")
#         super().__init__()
#
#
# class B(Base):
#     def __init__(self):
#         print("I'm B")
#         super().__init__()
#
#
# class C(A, B):
#     def __init__(self):
#         super().__init__()
#
#
# def main():
#     c = C()
#
#
# if __name__ == '__main__':
#     main()