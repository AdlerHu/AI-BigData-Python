import logging

# flag = 10
#
#
# def main():
#     function_a()
#     print(flag)
#
#
# def function_a():
#     flag = 20
#
#     def set_flag():
#         flag = 30
#
#     set_flag()
#     print(flag)
#
#
# if __name__ == '__main__':
#     main()


# flag = 10
#
#
# def main():
#     function_a()
#     print(flag)
#
#
# def function_a():
#     flag = 20
#
#     def set_flag():
#         # 使用關鍵字 nonlocal , 指名flag不是區域變數,不會改到全局變數
#         nonlocal flag
#         flag = 30
#
#
#     set_flag()
#     print(flag)
#
#
# if __name__ == '__main__':
#     main()


# avg2 = lambda a, b: (a + b) / 2
#
# print(avg2(10, 30))

# yield
# def main():
#     print(list(my_range(8)))
#     g = my_range(8)
#     next(g)
#     next(g)
#     print(next(g))
#
#
# def my_range(n):
#     x = 0
#     while True:
#         yield x
#         x += 1
#         if x == n:
#             break
#
#
# if __name__ == '__main__':
#     main()

# Decorator : 要執行的函數前面有@...修飾，會先跳到裝飾器函數裡
# def use_logging(fun):
#
#     def wrapper():
#         logging.warning('%s is running' % fun.__name__)
#         return fun()
#     return wrapper
#
# @use_logging
# def function_a():
#     print('Function_a is called')
#
# @use_logging
# def function_b():
#     print('function_b is called')
#
#
# function_a()
# function_b()

# def my_deco(func):
#     def wrapper_func(*args):
#         print('### {} is going to run ###'.format(func.__name__))
#         func(*args)
#         print('### {} was executed ###'.format(func))
#     return wrapper_func
#
#
# @my_deco
# def function_a(s):
#     print(s)
#
#
# function_a("Hello~ I'm function A.")

# ---------------------------------------------------------------------

# def main():
#     L = [10, 20, 30, 40, 50, 60]
#     print(L[2:-1])
#     print(sum(L[2:-1]))
#
#
# if __name__ == '__main__':
#     main()