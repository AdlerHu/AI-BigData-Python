import time, subprocess

calcproc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')

# 監控subprocess是否正常開啟
while True:
    print(calcproc.poll())
    if calcproc.poll() is not None:
        print('小算盤開啟')
        break

time.sleep(5)

# 結束Windows小算盤程序
proc = subprocess.Popen('Taskkill /IM Calculator.exe /F')