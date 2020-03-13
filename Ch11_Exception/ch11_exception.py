import traceback

# try:
#     10 * (1/0)
#     print(a)
#     b = [1, 2, 3]
#     print(b[5])
#     c = 1
#     print('c = ' + c)
#     print(1 + 1)
#
# except ZeroDivisionError:
#     print('除以0錯誤')
# except NameError:
#     print('使用未宣告變數')
# except IndexError:
#     print('List index out of range')
# except Exception as err:
#     print('其他錯誤')
#     print(err)
#     print(traceback.print_exc())
#
# else:
#     print('都沒有例外,會進到這裡')
# finally:
#     print('最後會到這裡')

# ---------------------------------------------------------------

# try:
#     raise NameError('引起例外')
#
# except NameError:
#     print('引起NameError例外')
#     # raise
#
# print("AAAAAA")

# ---------------------------------------------------------------
# 函式的前置條件檢查


# def box_print(symbol, width, height):
#
#     if len(symbol) != 1:
#         raise Exception('Symbol must be a single char')
#     if width <= 2:
#         raise Exception('Width must greater than 2')
#     if height <= 2:
#         raise Exception('Height must greater than 2')
#
#     print(width * height)
#
#     for i in range(height - 2):
#         print(symbol + (' ' * (width - 2)) + symbol)
#     print(width * height)
#     print('-------------------------------------------------------')
#
#
# for sym, w, h in (('*', 3, 3), ('@', 6, 4), ('x', 1, 3), ('zz', 1, 3)):
#     try:
#         box_print(sym, w, h)
#     except Exception as err:
#         print(str(err))

# ---------------------------------------------------------------
# 自訂例外

# class MyError(Exception):
#
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
#
# try:
#     my_month_buget = 6000
#     cost_of_month = 7000
#
#     if cost_of_month > my_month_buget:
#         raise MyError('Out Of My Buget')
# except MyError as e:
#     print('My exception occurred, value:', e.value)

# ---------------------------------------------------------------

# try:
#     buget = 6000
#     while True:
#         cost_of_month = input('請輸入每月花費: ')
#
#         if cost_of_month.strip() == '':
#             break
#         assert int(cost_of_month) <= buget, 'The cost is over buget!'
#
# except AssertionError as err:
#     print('Assertion Error: ' + str(err))