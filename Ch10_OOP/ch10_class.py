# class Car:
#     year = 2019
#     mpg = 30
#     speed = 0
#
#     def accelerate(self):
#         self.speed += 20
#
#     def brake(self):
#         self.speed -= 10
#
#
# def mian():
#     car1 = Car()
#     print('speed: ', car1.speed)
#     car1.accelerate()
#     car1.accelerate()
#     print('speed: ', car1.speed)
#     car1.brake()
#     print('speed: ', car1.speed)
#
#
# if __name__ == '__main__':
#     mian()

# -----------------------------------------------------------------------


# class Car:
#     year = 2019
#     mpg = 30
#     speed = 0
#
#     def __init__(self):
#         self.speed = 10
#
#     def accelerate(self):
#         self.speed += 20
#
#     def brake(self):
#         self.speed -= 10
#
#
# def main():
#     car1 = Car()
#     print('car1 speed', car1.speed)
#
#
# if __name__ == '__main__':
#     main()

# ------------------------------------------------------


# class Car:
#     year = 2019
#     mpg = 30
#     speed = 0
#
#     def __init__(self, speed):
#         self.speed = speed
#
#     def accelerate(self):
#         self.speed += 20
#
#     def brake(self):
#         self.speed -= 10
#
#
# def main():
#     car1 = Car(15)
#     print('car1 speed', car1.speed)
#
#
# if __name__ == '__main__':
#     main()

# ----------------------------------------------------------------

# class Box:
#     length = 1
#     width = 1
#     height = 1
#
#     def __init__(self, length=1, width=1, height=1):
#         self.length = length
#         self.width = width
#         self.height = height
#
#     def is_cube(self):
#         if self.length == self.width == self.height:
#             return True
#         else:
#             return False
#
#     def info(self):
#         return self.length, self.width, self.height
#
#     def volume(self):
#         return self.length * self.width * self.height
#
#
# def main():
#     box1 = Box(2, 2, 2)
#     box2 = Box(2, 3, 3)
#     print(box1.is_cube())
#     print(box1.info())
#     print(box1.volume())
#
#     print(box2.is_cube())
#     print(box2.info())
#     print(box2.volume())
#
#
# if __name__ == '__main__':
#     main()