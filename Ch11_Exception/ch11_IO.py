import sys

# print(sys.argv)
# print('命令參數的數量', len(sys.argv))
# print('Python程式路徑', sys.argv[0])
#
# for i in sys.argv:
#     print(i)

# -----------------------------------------------------------------

# f = open('wiki.txt', 'w', encoding='utf-8')
#
# text = """Python（英國發音：/ˈpaɪθən/ 美國發音：/ˈpaɪθɑːn/）是一種廣泛使用的直譯式、進階程式、通用型程式語言，由吉多·范羅蘇姆創造，第一版釋出於1991年。可以視之為一種改良（加入一些其他程式語言的優點，如物件導向）的LISP。[來源請求]Python的設計哲學強調代碼的可讀性和簡潔的語法（尤其是使用空格縮排劃分代碼塊，而非使用大括號或者關鍵詞）。相比於C++或Java，Python讓開發者能夠用更少的代碼表達想法。不管是小型還是大型程式，該語言都試圖讓程式的結構清晰明瞭。
#
# 與Scheme、Ruby、Perl、Tcl等動態型別程式語言一樣，Python擁有動態型別系統和垃圾回收功能，能夠自動管理記憶體使用，並且支援多種程式範式，包括物件導向、命令式、函數式和程序式程式。其本身擁有一個巨大而廣泛的標準庫。
#
# Python 直譯器本身幾乎可以在所有的作業系統中執行。Python的其中一個直譯器CPython是用C語言編寫的、是一個由社群驅動的自由軟體，目前由Python軟體基金會管理。"""
#
# f.write(text)
# f.close()

# -----------------------------------------------------------------

# f = open('wiki.txt', 'a', encoding='utf-8')
# f.write('\n')
# my_text = """Python的創始人為吉多·范羅蘇姆。1989年的聖誕節期間，吉多·范羅蘇姆為了在阿姆斯特丹打發時間，決心開發一個新的指令碼解釋程式，作為ABC語言的一種繼承。之所以選中Python作為程式的名字，是因為他是BBC電視劇——蒙提·派森的飛行馬戲團的愛好者。ABC是由吉多參加設計的一種教學語言。就吉多本人看來，ABC這種語言非常優美和強大，是專門為非專業程式設計師設計的。但是ABC語言並沒有成功，究其原因，吉多認為是非開放造成的。吉多決心在Python中避免這一錯誤，並取得了非常好的效果，完美結合了C和其他一些語言。[3]
# 就這樣，Python在吉多手中誕生了。實際上，第一個實現是在Mac電腦上。可以說，Python是從ABC發展起來，主要受到了Modula-3（另一種相當優美且強大的語言，為小型團體所設計的）的影響。並且結合了Unix shell和C的習慣。
# """
#
# f.write(my_text)
# f.close()

# -----------------------------------------------------------------

# f = open('wiki.txt', 'r', encoding='utf-8')
# content = f.read()
# print(content)
# f.close()

# -----------------------------------------------------------------

# f = open('wiki.txt', 'r', encoding='utf-8')
# print('{:3d}'.format(f.tell()), end='')
# while True:
#     line = f.readline()
#     if not line:
#         break
#
#     print(line, end='')
#     print('{:3d}'.format(f.tell()), end='')
#
# f.close()

# -----------------------------------------------------------------

# f = open('data.txt', 'r', encoding='utf-8')
# empty_line = []
# while True:
#     line = f.readline()
#
#     if not line:
#         break
#
#     if len(str(line).strip()) == 0:
#         empty_line.append(f.tell())
#
# print('empty line:', empty_line)
# f = open('data.txt', 'r+', encoding='utf-8')
#
# for pos in empty_line:
#     f.seek(pos-2)
#     f.write('************\n')
#
# f.close()

# -----------------------------------------------------------------

# text = '''
# What is a PEP?
# ==============
#
# PEP stands for Python Enhancement Proposal.  A PEP is a design
# document providing information to the Python community, or describing
# a new feature for Python or its processes or environment.  The PEP
# should provide a concise technical specification of the feature and a
# rationale for the feature.
#
# '''
#
# print(text, end='', file=open('print_out.txt', 'w', encoding='utf-8'))
# print('ok')

# -----------------------------------------------------------------

# food_cal_list = [
#     ['種類', '單位', '重量(g)', '熱量(卡)'],
#     ['白米飯', '1碗', 205, 225],
#     ['義大利肉醬麵', '1份', 248, 330],
#     ['白吐司', '1片', 25, 75],
#     ['全麥吐司', '1片', 25, 65],
#     ['花生醬', '1湯匙', 16, 95],
#     ['果醬', '1湯匙', 18, 50]
# ]
#
# with open('food_cal.csv', mode='w', encoding='big5') as f:
#     for line in range(len(food_cal_list)):
#         text = str(food_cal_list[line]).replace('[', '').replace(']', '').replace('\'', '') +'\n'
#         f.write(text)
#
#     else:
#         print('OK')