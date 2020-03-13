import datetime

# int_num = 108
# money = 10.87654321

# 含小數點7位數字,太多前面會補空白
# print('$%*.2f' % (7, money))
# print('\n字元格式')
# print('%c' % 65)

# print('\n整數字串格式: ')
# print('%d' % int_num)
# print('%  d' % int_num)
# print('%8d' % int_num)
# print('%-8d' % int_num)
# print('%08d' % int_num)

# print('\n十六進位格式:')
# print('%x' % int_num)
# print('%X' % int_num)
# print('%#X' % int_num)
# print('%#x' % int_num)

# -----------------------------------------

# float_num = 9876543.43210
# num = 123

# print('\n浮點數與科學記號')
# print('%f' % float_num)
# print('%12.2f' % float_num)
# print('%E' % float_num)
# print('%e' % float_num)
# print('%g' % float_num)
# print('%G' % float_num)
# print('%e' % (11111111111111111111111))

# print('\n整數和字串輸出')
# print('%+d' % 4)
# print('%+d' % -4)
# print('we are at %d%%' % 100)
# print('your host is : %s' % 'earth')
# print('HOST: %s\tPort: %d' % ('Localhost', 80))
# print('dec: %d/oct: %#o/hex:%#X' % (num, num, num))
# print('MM/DD/YY = %02d/%02d/%d' % (3, 6, 2020))
# print('There are %(count)d %(lang)s' % {'lang': 'Python', 'count': 3})

# -----------------------------------------

# print('abc:{:.2f}'.format(3.1415926))
# print('{0}, {1}, {2}'.format('a', 'b', 'c'))
# print('{}, {}, {}'.format('a', 'b', 'c'))
# print('{2}, {1}, {0}'.format(*'abc'))
# print('{0}{1}{0}'.format('abra', 'cda'))

# print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
#
# coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
# print('Coordinates: {latitude},{longitude}'.format(**coord))

# c = 3-5j
# print('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.'.format(c))

# coord = (3, 5)
# print('X:{0[0]}; Y:{0[1]}'.format(coord))

# print("repr() show quotes: {!r};str() doesn't: {!s}".format('test1', 'test2'))

# print('{:<30}'.format('left aligned'))
# print('{:>30}'.format('right aligned'))
# print('{:^30}'.format('centered'))
# # ******cnetered******
# print('{:*^30}'.format('centered'))

# -----------------------------------------

# print('{:+f}; {:+f}'.format(3.14, -3.14))
# print('{:f}; {:f}'.format(3.14, -3.14))
# print('{:-f}; {:-f}'.format(3.14, -3.14))

# print('int: {0:d}; hex:{0:x}; oct{0:o}; bin:{0:b}'.format(42))
# print('int: {0:d}; hex:{0:#x}; oct{0:#o}; bin:{0:#b}'.format(42))

# print('{:,}'.format(1234567890))

# points = 19
# total = 22
# print('Correct answers: {:.2%}'.format(points/total))

# d = datetime.datetime(2010, 7, 4, 12, 15, 58)
# print('{:%Y-%m-%d %H:%M:%S}'.format(d))