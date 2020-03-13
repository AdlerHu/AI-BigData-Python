# List
# ------------------------------------------------------

# animals = ['Bat', 'Rat', 'Elephant', 'Cat']
# print(animals)
#
# words = list('ABCDEFGH')
# print(words)
#
# pairs = ['(' + str(i) + ',' + str(j) + ')' for i in range(0, 3) for j in range(0, 4)]
# print(pairs)

# ------------------------------------------------------

# words = list('CAT')
# print(words)
#
# # tuple to list
# a_tuple = ('a', 'b', 'c')
# print(list(a_tuple))
#
# # string to list
# birthday = '1/6/1952'
# blist = birthday.split('/')
# print(blist)
#
# # string to list
# splitstr = 'a/b//c//d///e'
# splitlist = splitstr.split('//')
# print(splitlist)

# ------------------------------------------------------

# animals = ['Bat', 'Rat', 'Elephant', 'Cat']
# print(animals[0])
# print(animals[1])
# print(animals[2])
# print(animals[-1])
# print(animals[-2])
#
# numbers = [10, 11, 12, 13, 14, 15, 16, 17]
#
# print(numbers[0:3])
# print(numbers[::2])
# print(numbers[::-1])

# ------------------------------------------------------

# numbers = [[10, 11], [12, 13], [14, 15], [16, 17]]
# print(numbers[0])
# print(numbers[1])
# print(numbers[0][1])
#
# print(numbers[::2][1])
# print(numbers[::2][1][0])

# ------------------------------------------------------

# animals = ['Bat', 'Rat', 'Elephant', 'Cat']
#
# animals[0] = 'Bull'
# animals[2] = 'Eagle'
#
# animals[0:2] = ['', '']
# print(animals)

# ------------------------------------------------------

# animals = ['Bat', 'Rat', 'Elephant', 'Cat']
#
# animals.append('Dog')
# print(animals)
#
# animals.insert(1, 'Tiger')
# print(animals)

# ------------------------------------------------------

# animals = ['Bat', 'Rat', 'Elephant', 'Cat']
# others = ['There', 'are']
#
# others.extend(animals)
#
# others += '.'
# print(others)

# ------------------------------------------------------

# animals = ['Bat', 'Rat', 'Elephant', 'Cat']
#
# for item in animals:
#     print(animals.index(item))
#
# print(animals.index('Rat'))

# ------------------------------------------------------

# animals = ['Bat', 'Rat', 'Elephant', 'Cat', 'Dog', 'Lion']
# print(animals)
#
# animals.remove('Elephant')
# print(animals)
#
# del animals[-1]
# print(animals)
#
# print('pop:' + animals.pop())
# print(animals)
#
# print('pop:' + animals.pop(1))
# print(animals)

# ------------------------------------------------------

# animals = ['Bat', 'Rat', 'Elephant', 'Cat']
# seprator = ' , '
#
# join_str = seprator.join(animals)
# print(join_str)
#
# splitlist = join_str.split(',')
# print(splitlist)

# ------------------------------------------------------

# char_list = ['A', 'A', 'B', 'C', 'B', 'A', 'B', 'A']
#
# if 'A' in char_list:
#     print('A Count:' + str(char_list.count('A')))
#
# if 'B' in char_list:
#     print('B Count:' + str(char_list.count('B')))
#
# if 'C' in char_list:
#     print('C Count:' + str(char_list.count('C')))
#
# print('length of char_list:' + str(len(char_list)))

# ------------------------------------------------------

# a_list = [6, 2, 5, 4, 3, 1]
# print(a_list)
#
# a_list.sort()
# print(a_list)
#
# a_list.sort(reverse=True)
# print(a_list)
#
# b_list = ['b', 'd', 'e', 'a', 'c', 'f']
# b_list_sorted = b_list.copy()
# b_list_sorted.sort()
# print(b_list)
# print(b_list_sorted)

# ------------------------------------------------------

# a_list = [1, 2, 4, 5, 6]
# b_list = a_list
#
# print(a_list)
# print(b_list)
#
# b_list[2] = 8
# print(b_list)
# print(a_list)
#
# print('a_list id:' + str(id(a_list)))
# print('b_list id:' + str(id(b_list)))

# ------------------------------------------------------

# a_list = [1, 2, 4, 5, 6]
# b_list = a_list.copy()
# c_list = list(a_list)
# d_list = a_list[:]
#
# print(a_list)
# print(b_list)
# print(c_list)
# print(d_list)
#
# print('----------------------------')
#
# b_list[2] = 10
# c_list[2] = 20
# d_list[2] = 30
#
# print(a_list)
# print(b_list)
# print(c_list)
# print(d_list)
#
# print('----------------------------')
#
# print('a_list id:' + str(id(a_list)))
# print('b_list id:' + str(id(b_list)))
# print('c_list id:' + str(id(c_list)))
# print('d_list id:' + str(id(d_list)))