# assert 是宣告該如何如何,後面接違反時候的處置

# def box_print(symbol, width, height):
#
#     try:
#         assert len(symbol) == 1, 'Symbol must be a single char'
#         assert width > 2, 'Width must greater than 2'
#         assert height > 2, 'Height must greater than 2'
#
#     except AssertionError as err:
#         print(str(err))
#     else:
#
#         print(width * height)
#
#         for i in range(height - 2):
#             print(symbol + (' ' * (width - 2)) + symbol)
#         print(width * height)
#         print('-------------------------------------------------------')
#
#
# for sym, w, h in (('*', 3, 3), ('@', 6, 4), ('x', 1, 3), ('zz', 1, 3)):
#     box_print(sym, w, h)

# ------------------------------------------------------------------------------------------------

# str1 = ''
# text1 = ''''''
#
# with open('9x9.txt', 'w', encoding='utf-8') as f:
#     for i in range(1, 10):
#
#         for j in range(1, 10):
#             str1 = str1 + '{} * {} = {:<4d}'.format(j, i, i*j) + ''
#
#         text1 = text1 + str1 + '\n'
#         str1 = ''
#
#     f.write(text1)