# 多型

# class Juicer:
#
#     def open(self):
#         print('打開果汁機')
#
#     def run(self):
#         print('開始打果汁')
#
#
# class Washer:
#
#     def open(self):
#         print('打開洗衣機')
#
#     def run(self):
#         print('開始洗衣服')
#
#
# def auto_run(thing):
#     thing.open()
#     thing.run()
#
#
# def main():
#     machine = Juicer()
#     auto_run(machine)
#
#     machine = Washer()
#     auto_run(machine)
#
#
# if __name__ == '__main__':
#     main()

# --------------------------------------------------------------

# 運算子多載
# class Vector3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __add__(self, other):
#         v = Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
#         return v
#
#     def __sub__(self, other):
#         v = Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
#         return v
#
#     def __str__(self):
#         s = '(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'
#         return s
#
#
# def main():
#     v1 = Vector3D(1, 2, 3)
#     v2 = Vector3D(1, 1, 0)
#
#     print(v1-v2)
#     print(v1+v2)
#
#
# if __name__ == '__main__':
#     main()

# --------------------------------------------------------------

# 迭代器

# class GiveMeFive:
#
#     def __iter__(self):
#         self.a = 5
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 10
#         return x
#
#
# def main():
#     gm5 = iter(GiveMeFive())
#
#     print(next(gm5))
#     print(next(gm5))
#     print(next(gm5))
#     print(next(gm5))
#     print(next(gm5))
#     print(next(gm5))
#     print(next(gm5))
#
#
# if __name__ == '__main__':
#     main()
