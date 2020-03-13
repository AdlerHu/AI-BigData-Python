# set

# ------------------------------------------------------

# empty_set = set()
# print(type(empty_set))
#
# even_set = {0, 2, 4, 6, 8, 10, 0, 2, 4}
# print(even_set)
#
# odd_set = {1, 3, 5, 7, 9}
# print(odd_set)

# ------------------------------------------------------

# set_a = set('letters')
# print(set_a)
#
# set_b = ([10, 15, 20, 20, 30, 40])
# print(set_b)
#
# set_c = set((10, 15, 20, 20, 30, 40))
# print(set_c)
#
# set_d = set({'a': 10, 'b': 20, 'c': 30})
# print(set_d)

# ------------------------------------------------------

# set_a = {2, 8, 10, 22, 11, 12}
#
# set_a.add(25)
# print(set_a)
#
# set_a.remove(2)
# print(set_a)
#
# set_a.discard(2)
# print(set_a)
#
# set_a.discard(8)
# print(set_a)
#
# # 不能 remove 不存在的元素
# set_a.remove(8)
# print(set_a)

# ------------------------------------------------------

# set_a = {2, 8, 10, 22, 11, 12}
# set_b = {6, 7, 10, 11, 15}
# set_c = {8, 12}
#
# print('set_a  交集 set_b', set_a.intersection(set_b))
# print('set_a  聯集 set_b', set_a.union(set_b))
# print('set_a  差集 set_b', set_a.difference(set_b))
# print('set_a  與 set_b 對稱差', set_a.symmetric_difference(set_b))
# print('set_c  是 set_a 的子集嗎', set_c.issubset(set_a))

# ------------------------------------------------------

# set_a = {2, 8, 10, 22, 11, 12}
# set_b = {6, 7, 10, 11, 15}
# set_c = {8, 12, 22}
#
# if set_c & set_b:
#     print(len(set_c & set_b))
# else:
#     print('0')
#
# if set_c & set_a:
#     print(len(set_c & set_a))
# else:
#     print('0')