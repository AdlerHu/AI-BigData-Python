import time
import csv
import pickle
import json

# print(time.time())
#
# print(time.localtime())
#
# print(time.asctime(time.localtime(time.time())))
#
# print(time.asctime(time.gmtime(time.time())))
#
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#
# print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))

# -------------------------------------------------------------------------------------

# food_cal_list = [
#     ['種類', '單位', '重量(g)', '熱量(卡)'],
#     ['白米飯', '1碗', 205, 225],
#     ['義大利肉醬麵', '1份', 248, 330],
#     ['白吐司', '1片', 25, 75],
#     ['全麥吐司', '1片', 25, 65],
#     ['花生醬', '1湯匙', 16, 95],
#     ['果醬', '1湯匙', 18, 50]
# ]
# print(food_cal_list)
#
# # 寫出CSV檔案
# with open('food_cal.csv', mode='w', newline='', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerows(food_cal_list)
#     writer.writerow(['果醬', '1湯匙', 18, 50])
#     print('write csv ok')
#
# # 讀取CSV檔案
# with open('food_cal.csv', mode='r', newline='', encoding='utf-8') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     read_csv_list = [row for row in rows]
#     print(read_csv_list)

# -------------------------------------------------------------------------------------

# dict_store_info = [
#     {'門市': '民復門市', '電話': '02 2514 0673', '地址': '105台北市松山區民生東路四段130號'},
#     {'門市': '延壽門市', '電話': '02 2762 2884', '地址': '105台北市松山區延壽街422號'},
#     {'門市': '東鑫門市', '電話': '02 2719 6327', '地址': '105台北市松山區民生東路四段55巷10號'}
# ]
#
# dictrow = {'門市': '東吉門市', '電話': '02 2762 2908', '地址': '105台北市松山區民生東路五段100號'}
#
# field_list = list(dict_store_info[0].keys())
#
# with open('dict_out.csv', 'wt', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_list)
#     writer.writeheader()
#     writer.writerows(dict_store_info)
#     writer.writerow(dictrow)
#
# dict_read_info = []
#
# with open('dict_out.csv', 'r', newline='', encoding='utf-8') as csvfile:
#     rows = csv.DictReader(csvfile)
#
#     for row in rows:
#         # field_list = list(row.keys())
#         #
#         # dict_read = {}
#         #
#         # for field in field_list:
#         #     dict_read[field] = row[field]
#
#         # dict_read_info.append(dict_read)
#
#         dict_read_info.append(dict(row))
#
# for item in dict_read_info:
#     print(item)

# -------------------------------------------------------------------------------------

# data = [12345, 'Hello', '你好', {'臉書': 'Facebook', 'Google': '谷歌'}]
#
# bytes_str = pickle.dumps(data)
# print(bytes_str)
#
# data_load = pickle.loads(bytes_str)
# print(data_load)

# -------------------------------------------------------------------------------------

# data = [12345, 'Hello', '你好', {'臉書': 'Facebook', 'Google': '谷歌'}]
#
# with open('out.pk', 'wb') as f:
#     pickle.dump(data, f)
#
# with open('out.pk', 'rb') as f:
#     load_data = pickle.load(f)
#
# print(load_data)

# -------------------------------------------------------------------------------------

# dict_data = {
#     '產品編號': 'PN100023',
#     '產品名稱': 'IPhoneX 掀蓋手機殼',
#     '產品規格': ['質感黑', '海軍藍', '櫻花粉'],
#     '產品價格': 599
# }
#
# print(dict_data)
#
# # 轉換成JSON字串
# json_str = json.dumps(dict_data)
#
# # unicode 字串
# print(json_str)
#
# # 把unicode字串轉回
# print(json_str.encode('utf-8').decode('unicode_escape'))
#
# # 轉JSON回字典
# data_load = json.loads(json_str)
# print(dict(data_load))
#
# # Writting JSON data
# with open('data.json', 'w', encoding='utf-8') as f:
#     json.dump(dict_data, f)

# # Reading data back
# with open('data.json', 'r', encoding='utf-8') as f:
#     data_load = json.load(f)
#     print(dict(data_load))

# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
