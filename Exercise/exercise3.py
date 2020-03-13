# 一、
# 將撲克牌(52張)亂數分給n個人，n為大於零的整數，每個人都會拿到52/n張撲克牌，印出每一組撲克牌。(hint: random.randint(), List, Dictionary)





# 二、
# 假設一數列 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129, 189
# 請以Python在一行程式碼內定義一涵數Func(n)使得Func(0), Func(1), Func(2), ..., Func(15)之回傳值分別等於此數列。(hint: lambda, recursive)


# def computer(m):
#     n = 0
#     a, b, c = 1, 1, 1
#     while n < m:
#         yield a
#         a, b, c = b, c, a + c
#         n = n + 1
#
#
# print(list(computer(16)))