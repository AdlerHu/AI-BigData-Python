# Tuple
# ------------------------------------------------------

# city_name_tuple = ()
# print(city_name_tuple)
# print(type(city_name_tuple))
#
# city_name_tuple = 'Taoyuan'
# print(city_name_tuple)
# print(type(city_name_tuple))
#
# city_name_tuple = ('Taoyuan')
# print(city_name_tuple)
# print(type(city_name_tuple))
#
# city_name_tuple = 'Taoyuan', 'Tokyo', 'New York', 'London'
# print(city_name_tuple)
# print(type(city_name_tuple))
#
# city_name_tuple = ('Taoyuan', 'Tokyo', 'New York', 'London')
# print(city_name_tuple)
# print(type(city_name_tuple))

# ------------------------------------------------------

# number_tuple = 10, 30, 20, 40, 50, 10, 20, 30
# print('值組中20的數量:', number_tuple.count(20))
#
# for number in number_tuple:
#     print(number, 'index:', number_tuple.index(number))
#
# value_tuple = 1, 2, 3, 4
# a, b, c, d = value_tuple
#
# print('a= ', a, 'b= ', b, 'c= ', c, 'd= ', d)

# ------------------------------------------------------
# Dict
# ------------------------------------------------------

# custom_dict = {
#     'Alice': '0913001002',
#     'Amy': '0910123456',
#     'John': '0970033586',
#     'Bob': '0918845100'}
#
# print(custom_dict)
#
# char_dict = {ch_index: chr(ch_index) for ch_index in range(80, 90)}
# print(char_dict)
# print()

# ------------------------------------------------------

# list_a = [[0, 0], [1, 1], [2, 2]]
# dict_a = dict(list_a)
# print(dict_a)
#
# list_b = [['a1', 'b1'], ['a2', 'b2'], ['a3', 'b3']]
# dict_b = dict(list_b)
# print(dict_b)
#
# list_c = ['ab', 'cd', 'ef']
# dict_c = dict(list_c)
# print(dict_c)
#
# list_d = 'ab', 'cd', 'ef'
# dict_d = dict(list_d)
# print(dict_d)

# ------------------------------------------------------

# fruits = ['Apple', 'Orange', 'Banana']
# fruits_zh = ['蘋果', '橘子', '香蕉']
#
# fruits_dict = dict(zip(fruits, fruits_zh))
# print(fruits_dict)

# ------------------------------------------------------

# custom_dict = {
#     'Alice': '0913001002',
#     'Amy': '0910123456',
#     'John': '0970033586',
#     'Bob': '0918845100'}
#
# print(custom_dict['Bob'])
# print(custom_dict.get('Alice'))
# print(custom_dict.keys())
# print(custom_dict.values())
# print(custom_dict.items())

# ------------------------------------------------------

# custom_dict = {
#     'Alice': '0913001002',
#     'Amy': '0910123456',
#     'John': '0970033586',
#     'Bob': '0918845100'}
#
# print(custom_dict)
#
# custom_dict['Amy'] = '0910123123'
# custom_dict['Amber'] = '0910123456'
# print(custom_dict)

# ------------------------------------------------------

# custom_dict_1 = {
#     'Alice': '0913001002',
#     'Amy': '0910123456',
#     'John': '0970033586',
#     'Bob': '0918845100'}
#
# print('custom_dict_1 筆數: ', len(custom_dict_1))
#
# custom_dict_2 = {
#     'Alex': '0910001002',
#     'Bally': '0917123455',
#     'Frank': '0980233586',
#     'Bob': '0917844200'}
#
# print('custom_dict_2 筆數: ', len(custom_dict_2))
#
# custom_dict_1.update(custom_dict_2)
# print('custom_dict_1 更新後: ', custom_dict_1)
# print('custom_dict_1 更新後筆數: ', len(custom_dict_1))

# ------------------------------------------------------

# custom_dict = {
#     'Alice': '0913001002',
#     'Amy': '0910123456',
#     'John': '0970033586',
#     'Bob': '0918845100',
#     'Jason': '0911885743'}
#
# print(custom_dict)
#
# del custom_dict['John']
# print('del John')
# print(custom_dict)
#
# print('pop: ', custom_dict.pop('Amy'))
# print(custom_dict)
#
# print('popitem: ', custom_dict.popitem())
# print(custom_dict)
#
# custom_dict.clear()
# print(custom_dict)

# ------------------------------------------------------

# custom_dict = {
#     'Alice': '0913001002',
#     'Amy': '0910123456',
#     'John': '0970033586',
#     'Bob': '0918845100'}
#
# if 'Amy' in custom_dict:
#     print(custom_dict['Amy'])

# ------------------------------------------------------

# custom_dict = {
#     'Alice': '0913001002',
#     'Amy': '0910123456',
#     'John': '0970033586',
#     'Bob': '0918845100'}
#
# dict_a = custom_dict
# dict_b = custom_dict.copy()
#
# dict_a['Bob'] = ''
# dict_b['Amy'] = ''
#
# print('custom_dict', custom_dict)
# print('dict_a', dict_a)
# print('dict_b', dict_b)