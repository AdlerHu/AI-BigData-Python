import re

# 貪婪與非貪婪比對


# input_str = 'A running <div>dog</div> rams <div>cat</div> a walking <div>pig</div>.'
#
# # 貪婪比對
# re_match = re.findall(r'<div>(.*)</div>', input_str)
#
# if re_match:
#     print(re_match)
# else:
#     print('None')
#
# print('----------------')
#
# # 非貪婪比對
# re_match = re.findall(r'<div>(.*?)</div>', input_str)
# re_match = re.findall(r'<div>.*?</div>', input_str)
#
# if re_match:
#     print(re_match)
# else:
#     print('None')

# ----------------------------------------------------------------------------

# re.split()
# input_str = '(1) Jacky Wu (2) JayChou (3) JJ Lin'
#
# # 使用split()結合正規表示式
# re_match = re.split(r'\(\d\)', input_str)
#
# if re_match:
#     print(re_match)
# else:
#     print('None')

# ----------------------------------------------------------------------------

# re.sub()
# input_str = 'a001.jpg, b02.gif, aacc0908.jpg'
#
# re_match = re.sub(r'\.(gif|jpg)', '.png', input_str)
#
# if re_match:
#     print(re_match)
# else:
#     print('None')

# ----------------------------------------------------------------------------

# re.compile()

# input_str = 'amy,amylee@yahoo.com,robert,robert_wang@gmail.com,martin,martin.chen@outlook.com'
#
# email_regx = re.compile(r'[a-zA-z0-9\._]+@[a-zA-Z0-9\._]+')
# re_match = email_regx.findall(input_str)
#
# if re_match:
#     print(re_match)
# else:
#     print('None')