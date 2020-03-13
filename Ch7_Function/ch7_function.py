# def function_return_multiple(a, b, c, d):
#     e = a + b + c + d
#
#     a = 'Hello'
#     b = 10
#     c = 20
#     d = 30
#
#     return a, b, c, d, e
#
#
# print(function_return_multiple(1, 2, 3, 4))


# def main():
#     b = '我是B'
#     function_change_value(b)
#     print(b)
#
#     b = function_change_value2(b)
#     print(b)
#
#
# def function_change_value(a):
#     a = '我是A'
#
#
# def function_change_value2(a):
#     a = '我是回傳的A'
#     return a
#
#
# if __name__ == '__main__':
#     main()

# def function_change_value(a):
#     a[0] = '換'
#     a[1] = '成'
#     a[2] = 'A'
#
#
# def main():
#     b = ['我', '是', 'B']
#     print(b)
#
#     function_change_value(b)
#     print(b)
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     print_info(10, 20, 30, 40)
#
#
# def print_info(para1, *var_tuple):
#     print(para1)
#     print(var_tuple)
#     print(var_tuple[-1])
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     print_info(10, a=10, b=20)
#
#
# def print_info(para1, **var_dict):
#     print(para1)
#     print(var_dict)
#
#
# if __name__ == '__main__':
#     main()


# def main():
#     print_info(5, b=10)
#
#
# def print_info(a, *, b):
#     print(a + b)
#
#
# if __name__ == '__main__':
#     main()


# var_global = 'global'
#
#
# def main():
#     function_level1()
#
#
# def function_level1():
#     level_1_str = 'level 1'
#
#     def function_level_0():
#         level_0_str = 'level 0'
#         print(level_0_str)
#         print(level_1_str)
#         print(var_global)
#
#     function_level_0()
#
#
# if __name__ == '__main__':
#     main()




















