# import time
'''
print(time.time())
print(time.ctime())
print(time.gmtime()) # 生成其他程序可读的时间
# 时间格式化
# 控制符 %Y年份 %m月份 %B月份名称 %b月份缩写 %d日期 %A星期
# %a星期缩写 %H小时（24） %h小时（12） %p 上/下午 %M分钟 %S秒
print(time.strftime('%Y-%m-%d %H:%M:%S %A', time.gmtime()))
timeStr = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
# print(timeStr)
# timeStr = str(timeStr)
print(time.strptime(timeStr, '%Y-%m-%d %H:%M:%S'))
start = time.perf_counter()
def wait():
	time.sleep(3.3)
wait()
time.sleep(3)
end = time.perf_counter()
print(end - start)
scale = 10
print('{:-^20}'.format('执行开始'))
for i in range(scale+1):
	a = i/scale*100
	b = i*'*'
	c = (scale-i)*'.'
	print('{:^3.0f}%[{}->{}]'.format(a, b, c))
	time.sleep(0.2)
print('{:-^20}'.format('执行结束'))

for i in range(101):
	print('\r{:3}%'.format(i), end=' ')
	time.sleep(1)

scale = 50
print('执行开始'.center(scale//2, '-'))
start = time.perf_counter()
for i in range(scale+1):
	a = i/scale*100
	b = i*'*'
	c = (scale-i)*'.'
	dur = time.perf_counter() - start
	print('\r{:^3.0f}%[{}->{}] {:.2f}s'.format(a, b, c, dur), end=' ')
	time.sleep(0.1)
print('\n'+'执行结束'.center(scale//2, '-'))
'''

# guess = eval(input())
# print('猜{}了'.format('对' if guess == 99 else "错"))
'''
try:
	num = eval(input('请输入一个整数:'))
	print(num**2)
except:
	print('输入不是整数')
# else: 如果不发生异常执行

# finally: 一定会执行
'''
height, weight = eval(input('输入'))
print(weight)
