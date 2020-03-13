# a = int(input("請輸入一個整數:"))
#
# if a > 100:
#     print("您輸入的整數超過100")
# print("您輸入的是: " + str(a))

# ---------------------------------------------------------------------

# a = int(input("請輸入一個整數:"))
#
# if a % 2 == 0:
#     print(str(a), '是偶數')
# else:
#     print(str(a), '是奇數')

# ---------------------------------------------------------------------

# a = int(input("請輸入一個整數a:"))
# b = int(input("請輸入一個整數b:"))
#
# if a == b:
#     print('a = b')
# elif a > b:
#     print('a > b')
# else:
#     print('a < b')

# ---------------------------------------------------------------------

# sites = ['Facebook', 'Google', 'Amazon', 'Twitter', 'Youtube', 'Yahoo']
#
# for index, element in enumerate(sites):
#     print('編號 %d 站台 %s' % (index, element))

# for site in sites:
#     print('編號:', sites.index(site), '站台' + site)
# print('完成 python for loop')

# ---------------------------------------------------------------------

# sites = ['Facebook', 'Google', 'Amazon', 'Twitter', 'Youtube', 'Yahoo']
#
# print('串列長度: ', len(sites))
# print('串列範圍: ', range(len(sites)))
#
# for index, element in enumerate(sites):
#     print('%d.%s' % (index, element))
# print('\n')
#
# print('列出第二筆到第四筆')
# for i in range(2,5):
#     print('編號', i, '站台' + sites[i])

# ---------------------------------------------------------------------

# sites = ['Facebook', 'Google', 'Amazon', 'Twitter', 'Youtube', 'Yahoo']
#
# for index, element in enumerate(sites):
#     print('%d.%s' % (index, element))
#     if sites[index] == 'Twitter':
#         break
# print('\n')

# ---------------------------------------------------------------------

# L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print('使用continue')
# for item in L:
#     if item == 7 :
#         continue
#     print(item)
#
# print('使用pass')
# for item in L:
#     if item == 7 :
#         pass
#     print(item)

# ---------------------------------------------------------------------

# for n in range(2, 20):
#     for x in range(2, n):
#         if n % x == 0:
#             print('%d 可被 %d 整除' % (n, x))
#             break
#     else:
#         print(n, '是質數')

# ---------------------------------------------------------------------

# print([x * 2 + 10 for x in range(20)])
# print([x for x in range(20) if x % 3 == 0])

# ---------------------------------------------------------------------

# sum = 0
# counter = 1
# while counter <= 100:
#     sum = sum + counter
#     counter += 1
#
# print('1 到 100 加總:', sum)

# ---------------------------------------------------------------------

birthdays = {'Alice': 'Apr 1',
             'Bob': 'Dec 12',
             'Carol': 'Mar 4'}

while True:
    print('Enter a name:(key in exit to quit)')
    name = input()
    if name == 'exit':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print("I don't have birthday information for " + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday data updated.')

# ---------------------------------------------------------------------
