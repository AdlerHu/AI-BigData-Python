import os
import shutil
import glob
import math
import random

# with open('test.txt', 'wt')as f:
#     print('for test', file=f)
#
# # 檔案存在嗎
# print(os.path.exists('test.txt'))
#
# # 這是檔案嗎
# print(os.path.isfile('test.txt'))
#
# # 這是目錄嗎
# print(os.path.isdir('.'))
#
# # 目前的工作目錄
# print(os.getcwd())
#
# # 是絕對路徑嗎
# print(os.path.isabs('E:\\AIBigData\\AIBigData\\Python\\worspace\\Ch12_Module\\test.txt'))
#
# # 列出某個目錄
# print(os.listdir('E:\\AIBigData\AIBigData\\'))

# ------------------------------------------------------------------------------------------------------

# if os.path.exists('test_dir'):
#     shutil.rmtree('test_dir')
#
# os.mkdir('test_dir')
#
# os.chdir('test_dir')
#
# print(os.path.abspath('.'))
#
# shutil.copy('../test.txt', 'test_copy.txt')
#
# print(os.listdir('.'))
#
# print(glob.glob('te*'))

# ------------------------------------------------------------------------------------------------------

# # 捨去小數
# num = 1.2345
# print(math.trunc(num))
#
# # 開根號
# num = 9
# print(math.sqrt(num))
#
# # x^2 + y^2 再開根號
# print(math.hypot(3, 4))
#
# # 取絕對值
# print(math.fabs(-10))

# ------------------------------------------------------------------------------------------------------

# # 機率模型種子 7
# print(random.seed(7))
#
# # 機率
# print(random.random())
#
# # 1-10 隨機整數
# print(random.randrange(10))
#
# # 隨機偶數
# print(random.randrange(0, 101, 2))
#
# # 隨機挑一個
# print(random.choice(['剪刀', '石頭', '布']))
#
# # 權重
# print(random.choices(['頭', '字'], cum_weights=(0.8, 1.0), k=10))
#
# # 洗牌
# num = ['A', 'J', 'Q', 'K', '10']
# random.shuffle(num)
# print(num)
#
# # 抽樣3個
# print(random.sample([10, 20, 30, 40, 50], k=3))