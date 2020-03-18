import random

# 一、
# 將撲克牌(52張)亂數分給n個人，n為大於零的整數，每個人都會拿到52/n張撲克牌，印出每一組撲克牌。(hint: random.randint(), List, Dictionary)

# import random
#
# suit = ["♠️", "♥️", "♦️", "♣️"]
# num = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# deck = []
# for i in suit:
#     for j in num:
#         deck.append(i + j)
# random.shuffle(deck)
# print(deck)
#
# n = int(input('請輸入人數'))
# cd_count = 52 // n
#
# pepo_get = [[0 for j in range(cd_count)] for i in range(n)]
# for i in range(n):
#     for j in range(cd_count):
#         pepo_get[i][j] = deck.pop()
#
# for x in range(n):
#     print('第{}人的牌:'.format(x+1))
#     print(pepo_get[x])
#
# if cd_count != 0:
#     print('未發出的牌為:', deck)

suit = ['♠', '♥', '♦', '♣']
num = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = []

# 生成撲克牌
for i in suit:
    for j in num:
        deck.append(i+j)

# 洗牌
random.shuffle(deck)

n = int(input('請輸入人數'))
# 要個人幾張牌
cd_count = 52 // n

people_init = [[0 for j in range(cd_count)] for i in range(n)]
print(people_init)



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
