# -------------------------------------------------------------------
# a = 100.05
# b = 20
# print(a + b)
# a = str(a)
#
# a = [10, 20, 30]
# print(str(a))
#
# a = (10, 20, 30)
# print(str(a))
#
# dict_a = {0: 'apple', 1: 'orange', 2: 'mango'}
# print(str(dict_a))
#
# set_a = {10, 20, 30}
# print(str(set_a))

# -------------------------------------------------------------------

# print('This is a ' + 'Python string.')
# print("It's important!! \n" * 3)
#
# a = 100.05
# b = 20
# print('a= ' + str(a) + ' b= ' + str(b))
#
# list_a = [10, 20, 30]
# str_a = ''
# for item in list_a:
#     str_a = str_a + ' ' + str(item)
# print(str_a)
#
# dict_a = {0: 'apple', 1: 'orange', 2: 'mongo'}
# for i in range(len(dict_a)):
#     print('Item', i, ':' + (' ' + dict_a[i]) * 3)

# -------------------------------------------------------------------

# str_t = "\' This is a Python string.\'"
# for i in range(len(str_t)):
#     print("str_t[", i, "] = ", str_t[i])
#
# print(str_t[1:])
# print(str_t[:10])
# print(str_t[10:17])
# print(str_t[17:])
# print(str_t[10:] + str_t[17:])
# print(str_t[::3])

# -------------------------------------------------------------------

# str_t = ' This is a Python string.'
# print(str_t.split())
#
# str_p = 'Alice , Joe , Bob , Kent , Zoey'
# print(str_p.split(','))
#
# print('/'.join(str_p.split(',')))
#
# str_a = '''Python can be easy to pick up whether
# you\'re a first time programmer
# or you\'re experienced with other languages.'''
# print(str_a.split('\n'))
#
# print('\t' + '\n\t'.join(str_a.split('\n')))

# -------------------------------------------------------------------

# str_p = 'alicE , joE , boB , kenT , zoeY'
# print(str_p.lower())
# print(str_p.upper())
# # 字首大寫,其他小寫
# print(str_p.title())
#
# # 句首大寫
# str_t = 'python is powerful and fast'
# print(str_t.capitalize())
#
# # 字串對齊方式
# str_s = 'Hello'
# print('\'' + str_s.rjust(20) + '\'')
# print('\'' + str_s.ljust(20) + '\'')
# print('\'' + str_s.center(20) + '\'')

# -------------------------------------------------------------------

# str_t = '         [Python is easy]     '
#
# # 刪除左右的空白
# print('\'' + str_t.lstrip() + '\'')
# print('\'' + str_t.rstrip() + '\'')
# print('\'' + str_t.strip() + '\'')
#
# # 沒有刪除空白,無法刪除左右特定字元
# print(str_t.strip('[').strip(']'))
#
# # 刪除特定字元
# str_m = str_t.strip().strip('[').strip(']')
# print(str_m)

# -------------------------------------------------------------------

# str_p = 'Python is easy to learn, and simple to use.'
#
# # 尋找特定字串
# print(str_p.find('to'))
# print(str_p.rfind('to'))
#
# # 取代特定字串
# str_m = str_p.replace('to', '', str_p.count('to'))
#
# # 特定字串是否存在在字串中
# print('to' in str_m)
# print(str_m)
# print('to' not in str_m)
#
# # 是否以特定字串開始或結束
# print(str_p.startswith('Python'))
# print(str_p.endswith('.'))

# -------------------------------------------------------------------


# def input_check(input_str):
#     print('\n')
#     print(input_str)
#     print('is space: ', input_str.isspace())
#     print('is a numeric or alpha : ', input_str.isalnum())
#     print('is numeric', input_str.isnumeric())
#     print('is decimal', input_str.isdecimal())
#     print('is digit', input_str.isdigit())
#     print('is alpha', input_str.isalpha())
#     print('is lower', input_str.islower())
#     print('is upper', input_str.isupper())
#     print('is title', input_str.istitle())
#     print('is ascii', input_str.isascii())
#
#
# input_check('ABC')
# input_check('123456')
# input_check('!!2344abc')
# input_check('100.01')
# input_check('')
# input_check(' ')