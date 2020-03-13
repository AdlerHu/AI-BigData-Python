# class Member:
#
#     def __init__(self, name='', phone='', email=''):
#         self.__name = name
#         self.__phone = phone
#         self.__email = email
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def phone(self):
#         return self.__phone
#
#     @phone.setter
#     def phone(self, value):
#         self.__phone = value
#
#     @property
#     def email(self):
#         return self.__email
#
#     @email.setter
#     def email(self, value):
#         self.__email = value
#
#
# def main():
#     member0 = Member('Adler', '0910111111', 'huadlerben@qq.com')
#     print('Name:', member0.name)
#     print('Phone:', member0.phone)
#     print('Email:', member0.email)
#
#     member0.phone = '123456789'
#     print(member0.phone)
#
#
# if __name__ == '__main__':
#     main()

# ---------------------------------------------------------------------------


# class Fuck:
#
#     def __init__(self, a):
#         self.a = a
#
#     def __iter__(self):
#
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a = self.a ** 2
#         return x
#
#
# def main():
#
#     f = iter(Fuck(2))
#     print(next(f))
#     print(next(f))
#     print(next(f))
#     print(next(f))
#
#
# if __name__ == '__main__':
#     main()