# 封裝


# class Book():
#
#     def __init__(self, name='', author='', price=0):
#         self.name = name
#         self.author = author
#         self.__price = price
#
#     @property  # getter
#     def price(self):
#         return self.__price
#
#     @price.setter
#     def price(self, value):
#         self.__price = value
#
#     def info(self):
#         return self.name, self.author, self.__price
#
#
# def main():
#     book1 = Book('哈利波特神秘的魔法石', 'JK羅琳', 350)
#
#     print(book1.info())
#
#
# if __name__ == '__main__':
#     main()

# ----------------------------------------------------------------------------------

# class Book:
#
#     def __init__(self, name='', author='', price=0):
#         self.name = name
#         self.author = author
#         self.__price = price
#
#     def __str__(self):
#         return 'name,' + self.name + ',author,' + self.author + ',price' + str(self.__price)
#
#     def __del__(self):
#         print(self.name + '已移除')
#
#     def __call__(self, name='', author='', price=0):
#         if len(name.strip()) > 0:
#             self.name = name
#         if len(author.strip()) > 0:
#             self.author = author
#         if price >= 0:
#             self.__price = price
#
#
# def main():
#     book1 = Book('哈利波特神秘的魔法石', 'JK羅琳', 350)
#     book1('哈利波特-消失的密室', '', 320)
#     print(book1)
#
#
# if __name__ == '__main__':
#     main()