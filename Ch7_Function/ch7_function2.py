# 使用 iter() 拜訪可迭代物件

# week_daty = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
#
# for day in iter(week_daty):
#     print(day)
#
# for i in range(len(week_daty)):
#     print(week_daty[i])
#
# for day in iter(list(reversed(week_daty))):
#     print(day)

# -----------------------------------------------------------------------

# 使用 map() 套用函式設定串列


# def add_ten(x):
#     x += 10
#
#
# def add_ten_r(x):
#     return x + 10
#
#
# def main():
#     L = [1, 2, 3, 4, 5, 6]
#     M = map(lambda x: x * 10, L)
#
#     print(M)
#     print(list(M))
#
#     N = list(map(add_ten, L))
#     print(N)
#
#     N = list(map(add_ten_r, L))
#     print(N)
#
#
# if __name__ == '__main__':
#     main()

# -----------------------------------------------------------------------

# def main():
#     L = []
#     M = [1, '', 2, 0]
#     print(any(L))
#     print(any(M))
#     print(all(M))
#
#
# if __name__ == '__main__':
#     main()

# -----------------------------------------------------------------------

# def main():
#     x = 10
#     s1 = 'x + 3'
#     s2 = 'pow(2, 3)'
#     s3 = '1, 2, 3, 4'
#
#     print(eval('3 * x'))
#     print(eval('pow(2, 2)'))
#     print(eval(s1))
#     print(eval(s2))
#     print(eval(s3))
#
#
# if __name__ == '__main__':
#     main()

# -----------------------------------------------------------------------

# def main():
#     # exec
#     exec('print("Hello World")')
#     exec("""for i in range(5): print("iter time:%d" %i)""")
#     print('\n')
#
#     # compile
#     str = "for i in range(5): print(\"iter time: %d\" % i)"
#     c = compile(str, '', 'exec')
#     exec(c)
#
#
# if __name__ == '__main__':
#     main()