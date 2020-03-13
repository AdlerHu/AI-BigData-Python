import re

# 1.
# 請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。

# odd = 0
# even = 0
# for i in range(1, 11):
#     n = int(input('請輸入第 {} 個整數:'.format(i)))
#     if n % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# print('奇數: {} 個'.format(odd))
# print('偶數: {} 個'.format(even))

# 2.
# 請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，然後判斷它是否為閏年（leapyear）或平年。
# 其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏。
# (假設此不定數迴圈輸入 - 9999 則會結束此迴圈。)

# ans = ''
# while True:
#     year = int(input('請輸入西元年分(輸入 -9999結束程式): '))
#
#     if year == -9999:
#         print('Bye')
#         break
#     elif (year % 400) == 0:
#         ans = '閏'
#     elif (year % 100) == 0:
#         ans = '平'
#     elif (year % 4) == 0:
#         ans = '閏'
#     else:
#         ans = '平'
#
#     print(ans)

# 3.
# 請撰寫一程式，讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。
# 提示：平均分數輸出到小數點後第二位。

# grade_list1 = []
# for i in range(0, 3):
#     grade_list2 = []
#
#     for j in range(0, 5):
#         grade_list2.append(int(input('請輸入第 {} 位學生第 {} 筆成績: '.format(i+1, j+1))))
#
#     grade_list1.append(grade_list2)
#
# for i in range(0, 3):
#     print('第 {} 位學生總分為 {} 分，平均為 {:.2f} 分'.format(i+1, sum(grade_list1[i]), sum(grade_list1[i])/5))

# 4.
# 請撰寫一程式，將使用者輸入的三個參數，變數名稱分別為
# a（代表字元character）、x（代表個數）、y（代表列數），作為參數傳遞給一個名為compute()的函式，
# 該函式功能為：一列印出x個a字元，總共印出y列。
# 提示：輸出的每一個字元後方有一空格。


# def compute(a, x, y):
#     for i in range(0, y+1):
#         print(str(a) * x)
#
#
# compute('@', 10, 5)

# 5.
# 請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，
# 此函式接收兩個參數a、b，並回傳從a連加到b的和。

# def compute(a, b):
#     total = 0
#     while a <= b:
#         total += a
#         a += 1
#
#     return total
#
#
# print(compute(3, 5))

# 6.
# 請撰寫一程式，為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），
# 再輸入一鍵值並檢視此鍵值是否存在於該詞典中。

# dict1 = {}
# while True:
#     key = input('請輸入key(輸入end結束程序): ')
#
#     if key == 'end':
#         break
#     else:
#         if key not in dict1:
#             dict1[key] = input('請輸入 {} 的值: '.format(key))
#
# print(dict1)

# 7.
# 請撰寫一程式，輸入X組和Y組各自的科目至集合中，以字串"end"
# 作為結束點（集合中不包含字串"end"）。
# 請依序分行顯示
# (1)X組和Y組的所有科目、
# (2)X組和Y組的共同科目、
# (3)Y組有但X組沒有的科目，
# 以及(4)X組和Y組彼此沒有的科目（不包含相同科目）

# set_x = set()
# set_y = set()
#
# while True:
#     value = input('請輸入X組的值(輸入end結束程序): ')
#     if value == 'end':
#         break
#     else:
#         set_x.add(value)
#
# while True:
#     value = input('請輸入Y組的值(輸入end結束程序): ')
#     if value == 'end':
#         break
#     else:
#         set_y.add(value)
#
# print('X組:', set_x)
# print('Y組:', set_y)
#
# print('X組和Y組的所有科目:', set_x.union(set_y))
# print('X組和Y組的共同科目:', set_x.intersection(set_y))
# print('Y組有X組沒有的科目:', set_y.difference(set_x))
# print('X組和Y組彼此沒有的科目:', set_x.symmetric_difference(set_y))

# 8.
# 請撰寫一程式，要求使用者輸入一個密碼（字串），檢查此密碼是否符合規則。密碼規則如下：
# a.必須至少八個字元。
# b.只包含英文字母和數字。
# c.至少要有一個大寫英文字母。
# d.若符合上述三項規則，程式將顯示檢查結果為【Validpassword】，否則顯示【Invalidpassword】。

# password = input('請輸入密碼: ')
# b = False
#
# for s in password:
#     if s.isupper():
#         b = True
#
# if (b is True) and len(password) >= 8 and password.isalnum():
#     print('【Validpassword】')
# else:
#     print('【Invalidpassword】')

# 9.
# 請撰寫一程式，提示使用者輸入一個社會安全碼
# SSN，格式為ddd - dd - dddd，
# d表示數字。若格式完全符合（正確的SSN）則顯示【ValidSSN】，否則顯示【InvalidSSN】。

# input_ssn = input('Your SSN: ')
#
# re_match = re.match(r'^\d{3} - \d{2} - \d{4}', input_ssn)
#
# if re_match:
#     print('【ValidSSN】')
# else:
#     print('【InvalidSSN】')

# 10.
# 請撰寫一程式，要求使用者輸入一個長度為6的字串
# 將此字串分別置於10個欄位的寬度的左邊、中間和右邊，並顯示這三個結果，左右皆以直線 |（Vertical bar）作為邊界。

# str_s = input('請輸入長度為 6 字元的字串: ')
#
# print('|' + str_s.ljust(10) + '|')
# print('|' + str_s.center(10) + '|')
# print('|' + str_s.rjust(10) + '|')

# 11.
# 請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，
# 再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 | (Vertical bar）作為邊界。

# a = input('請輸入第一個整數')
# b = input('請輸入第二個整數')
# c = input('請輸入第三個整數')
# d = input('請輸入第四個整數')

# print('|{:>5} {:>5}|'.format(a, b))
# print('|{:>5} {:>5}|'.format(c, d))
# print('|{:<5} {:<5}|'.format(a, b))
# print('|{:<5} {:<5}|'.format(c, d))

# 12.
# (1)請使用迴圈敘述撰寫一程式，要求使用者輸入一個正整數n（n < 10），顯示n * n乘法表。
# (2)每項運算式需進行格式化排列整齊，每個運算子及運算元輸出的欄寬為2，而每項乘積輸出的欄寬為4，皆靠左對齊不跳行。

# num = int(input('請輸入一個正整數: '))
#
# str1 = ''
# for i in range(1, num + 1):
#
#     for j in range(1, num + 1):
#         str1 = str1 + '{:<2}{:<2}{:<2}{:<2}{:<4d}'.format(j, '*', i, '=', i * j) + ' '
#
#     print(str1)
#     str1 = ''

# 13.
# 請撰寫一程式，計算費氏數列（Fibonacci numbers），使用者輸入一正整數
# num(num >= 2)，並將它傳遞給名為compute()的函式，此函式將輸出費氏數列前num個的數值。
# 提示：費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：
# F0 = 0 F1 = 1
# Fn = Fn−1 + Fn−2

# def compute(m):
#     n = 0
#     a, b = 0, 1
#     while n < m:
#         yield a
#         a, b = b, a + b
#         n = n + 1
#
#
# m = int(input('輸入>=2的整數: '))
# print(list(compute(m)))