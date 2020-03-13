# class method


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
#     @classmethod
#     def get_volume(cls):
#         return cls.length * cls.width * cls.height
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
#     print(Box.get_volume())
#
#
# if __name__ == '__main__':
#     main()

# --------------------------------------------------------------------


# class A:
#     count = 0
#
#     def __init__(self):
#         A.count += 1
#
#     @classmethod
#     def get_count(cls):
#         print(cls.count)
#
#     def add_count(self):
#         self.count += 1
#
#
# def main():
#     A.get_count()
#     a1 = A()
#     A.get_count()
#
#     a1.add_count()
#     a1.add_count()
#     print(a1.count)
#
#     a2 = A()
#     a2.get_count()
#     a2.add_count()
#     a2.add_count()
#     print(a2.count)
#
#
# if __name__ == '__main__':
#     main()

# --------------------------------------------------------------------
# static method


# class A:
#     count = 0
#
#     def __init__(self):
#         A.count += 1
#
#     @classmethod
#     def get_count(cls):
#         print(cls.count)
#
#     def add_count(self):
#         self.count += 1
#
#     @staticmethod
#     def usage():
#         print('A is a class used to demo class method')
#
#
# def main():
#     A.usage()
#     A.get_count()
#     a1 = A()
#     A.get_count()
#     a2 = A()
#     A.get_count()
#
#
# if __name__ == '__main__':
#     main()

# --------------------------------------------------------------------


# class Car:
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
#     Car.color = 'black'
#     Car.brand = 'benz'
#     car1 = Car(15)
#     car1.type = 'SUV'
#
#     print('car1 speed', car1.speed)
#     print('car1 color', car1.color)
#     print('car1 brand', car1.brand)
#     print('car1 type', car1.type)
#
#
# if __name__ == '__main__':
#     main()