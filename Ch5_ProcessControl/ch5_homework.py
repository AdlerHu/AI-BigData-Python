# a = []
#
# for i in range(100):
#     if i % 2 == 0:
#         a.append(i)
#
# print(a)
#
# dict1 = {'台北市中正區': '100',
#          '台北市大同區': '103',
#          '台北市中山區': '104',
#          '台北市松山區': '105',
#          '台北市大安區': '106',
#          '台北市萬華區': '108',
#          '台北市信義區': '110'}
#
# key = input('請輸入區名: ')
# print('郵遞區號: ', dict1[key])

L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(0, 3):
    for j in range(0, 3):
        print(L[i][j])

