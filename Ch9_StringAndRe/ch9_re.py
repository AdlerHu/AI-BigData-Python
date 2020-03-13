import re

# re.match
# -----------------------------------------------------------------------------------
# ret_match = re.match(r'^\d{4}-\d{2}-\d{2}$', '1988-07-25')
#
# # 未分組
# if ret_match:
#     print('ret_match:', ret_match)
#     print('ret_match:', ret_match.group())
# else:
#     print('ret_match:None')
#
# # 用()分組
# ret_match = re.match(r'^(\d\d\d\d)-(\d\d)-(\d\d)$', '1983-04-07')
#
# if ret_match:
#     print('ret_match:', ret_match.groups())
#     print('ret_match:', ret_match.group())
#     print('ret_match:', ret_match.group(1))
# else:
#     print('ret_match:None')

# re.search
# -----------------------------------------------------------------------------------

# input_str = 'Terry, 1983-04-04, Marry, 1985-07-22, Joe, 1978-05-22'
# ret_search = re.search(r'\d{4}-\d{2}-\d{2}', input_str)
#
# # 未分組
# if ret_search:
#     print(ret_search)
#     print(ret_search.group())
# else:
#     print('None')
#
# # 用 () 分組
# ret_search = re.search(r'(\d\d\d\d)-(\d\d)-(\d\d)', input_str)
#
# if ret_search:
#     print(ret_search.groups())
#     print(ret_search.group())
#     print(ret_search.group(1))
#     print(ret_search.group(2))
#     print(ret_search.group(3))
# else:
#     print('ret_search:None')

# re.findall
# -----------------------------------------------------------------------------------

# input_str = 'amy,amylee@yahoo.com,robert,robert_wang@gmail.com,martin,martin.chen@outlook.com'
# ret_match = re.findall(r'[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+', input_str)
#
# if ret_match:
#     print(ret_match)
# else:
#     print('None')