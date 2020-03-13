# 1.
# 請撰寫一程式，讓使用者輸入 5個數字，計算並輸出這 5個數字之數值、總和及平均數。
# 提示：總和與平均數皆輸出到小數點後第1位。

# list1 = []
#
# for i in range(1, 6):
#     list1.append(float(input('請輸入第 %d 個數字: ' % i)))
#
# print(list1)
# total = sum(list1)
# print('總和: %5.1f 平均: %5.1f ' % (total, total / 5))

# 2.
# 假設一賽跑選手在 x分y秒的時間跑完z公里，請撰寫一程式，輸入x、y、z數值，最後顯示此選手每小時的平均英哩速度
# （1英哩等於1.6公里）。
# 提示：輸出浮點數到小數點後第一位。

# min = int(input('分: '))
# sec = int(input('秒: '))
# km = float(input('公里: '))
#
# print('時速: %5.1f' % ((km * 3600) / float(min*96 + sec*1.6)) + ' mile/hr')

# 3.
# 請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）。
# 提示：輸出浮點數到小數點後第二位。

# width = float(input('寬: '))
# height = float(input('高: '))
#
# print('高: %5.2f  寬: %5.2f' % (width, height))
# print('周長: %5.2f 面積: %5.2f' % ((width+height) * 2, (width * height)))

# 4.
# 請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，檢查這三個邊長是否可以組成一個三角形。若可以，則輸出該三角形之周長；否則顯示【Invalid】。
# 提示：檢查方法 = 任意兩個邊長之總和大於第三邊長。

# a = float(input('請輸入三角形三邊長: '))
# b = float(input('請輸入三角形三邊長: '))
# c = float(input('請輸入三角形三邊長: '))
#
# sum = a + b + c
#
# if (a + b > c) and (a + c > b) and (b + c > a):
#     print('周長: %5.2f' % (sum))
# else:
#     print('【Invalid】')

# 5.
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個十進位整數num(0 ≤ num ≤ 15)，將num轉換成十六進位值。
# 提示：轉換規則 = 十進位0~9的十六進位值為其本身，十進位10~15的十六進位值為A~F。

# dict1 ={10: 'A',11: 'B',12: 'C',13: 'D',14: 'E',15: 'F'}
#
# num = int(input('請輸入一個十進位整數: '))

# if num <= 9 :
#     print(num)
# else:
#     print(dict1[num])

# if (num % 16) <= 9:
#     print(num)
# else:
#     print(dict1[num % 16])

# 6.
# 請使用選擇敘述撰寫一程式，要求使用者輸入購物金額，購物金額需大於8, 000（含）以上，並顯示折扣優惠後的實付金額。購物金額折扣方案如下表所示：
# 金額折扣8, 000（含）以上9.5折18, 000（含）以上9折28, 000（含）以上8折38, 000（含）以上7折

# money = int(input('請輸入購物金額: '))
# rate = 1
#
# if money >= 38000:
#     rate = 0.7
# elif money >= 28000:
#     rate = 0.8
# elif money >= 18000:
#     rate = 0.9
# elif 18000 > money >= 8000:
#     rate = 0.95
#
# print(money * rate)

# 7.
# 請使用選擇敘述撰寫一程式，根據使用者輸入的分數顯示對應的等級。標準如下表所示：分數
# 等級80 ~ 100 A
# 70 ~ 79 B
# 60 ~ 69 C
# <= 59 F

# score = int(input('請輸入成績: '))
# grade_class = ''
#
# if 100 >= score >= 80:
#     grade_class = 'A'
# elif score >= 70:
#     grade_class = 'B'
# elif score >= 60:
#     grade_class = 'C'
# else:
#     grade_class = 'F'
#
# print(grade_class)

# 8.
# 請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是3或5的倍數，
# 顯示【x is a multiple of 3.】或【x is a multiple of 5.】；
# 若此數值同時為3與5的倍數，顯示【x is a multiple of 3 and 5.】；
# 如此數值皆不屬於 3 或 5的倍數，顯示【x is not a multiple of 3 or 5.】，將使用者輸入的數值代入 x。

# num = int(input('請輸入一個整數: '))
#
# if num % 3 ==0 and num % 5 ==0:
#     print('【x is a multiple of 3 and 5.】')
# elif num % 3 == 0:
#     print('【x is a multiple of 3.】')
# elif num % 5 == 0:
#     print('【x is a multiple of 5.】')
# else:
#     print('【x is not a multiple of 3 or 5.】')

# 9.
# 請使用迴圈敘述撰寫一程式，提示使用者輸入金額（如10, 000）、年收益率（如5.75），
# 以及經過的月份數（如5），接著顯示每個月的存款總額。
# 提示：四捨五入，輸出浮點數到小數點後第二位。
# 舉例：
# 假設您存款$10, 000，年收益為5.75 %。
# 過了一個月，存款會是：10000 + 10000 * 5.75 / 1200 = 10047.92
# 過了兩個月，存款會是：10047.92 + 10047.92 * 5.75 / 1200 =10096.06
# 過了三個月，存款將是：10096.06 + 10096.06 * 5.75 / 1200 =10144.44
# 以此類推。
# S = p * (1 + i) ^ n

# money = float(input('請輸入本金: '))
# rate = float(input('請輸入年利率: '))
# rate2 = 1 + rate/100
# months = int(input('請輸入月份數: '))
#
# for month in range(1,months+1):
#     print('第 %d 個月存款: %5.2f' % (month, money * rate2 ** month))

# 10.
# 請使用迴圈敘述撰寫一程式，讓使用者輸入一個正整數
# a，利用迴圈計算從1到a之間，所有5之倍數數字總和。

# a = int(input('請輸入一個正整數: '))
# sum = 0
#
# for i in range(1,a + 1):
#     if i % 5 == 0:
#         sum += i
#
# print(sum)