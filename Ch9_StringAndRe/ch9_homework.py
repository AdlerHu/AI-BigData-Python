import re

# str_t = "alice , joe , bob , kent , zoey"
#
# str_r = ''
# for item in str_t.split(' , '):
#     str_r += item[0:-1] + item[-1].upper() + ' '
#
# print(' , '.join(str_r.split()))

# # --------------------------------------------------------------------

# str1 = 'Python is easy to learn, easy to write and simple to use.'
#
# found = []
# for i in range(len(str1)):
#     index = str1.find('to', i, len(str1))
#     if index > 0 and index not in found:
#         found.append(index)
#
# print(found)

# ----------------------------------------------------------------------------

# re_match = re.match(r'[A-Z]\d{9}', 'A123456789')
#
# if re_match:
#     print("ret_match:", re_match)
#     print("ret_match:", re_match.group())
# else:
#     print('None')
