'''
def dayUp(df):
	dayup=1
	for i in range(365):
		if i % 7 in [6,0]:
			dayup *= 0.99
		else:
			dayup *= (1+df)
	return dayup
dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
	dayfactor += 0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))

str = '123456789'
print(str[:3])
print(str[1:])
print(str[1:8:2])
print(str[::-1])
# \b 回退一格  \r 光标移动到本行首
# x in s x是s的子串返回True
weekStr = '星期一星期二星期三星期四星期五星期六星期日'
# weekId = eval(input('请输入星期数字1-7:'))
# pos = (weekId - 1) * 3
# print(weekStr[pos: pos+3])
print(weekStr+str)
len(weekStr)
x = 100
print(hex(x))
print(oct(x))
# chr(x) x为Unicode编码，返回其对应的字符
# ord(x) x为字符，返回其对应的Unicode编码
for i in range(12):
	print(chr(9800 + i), end='，\n')
# end可以用于将结果输出到同一行，或者在结尾添加不同的字符
# str.lower() str.upper()
Str = 'abcde'
print(Str.upper())
print(Str.lower())
# str.split(sep = None) 返回一个列表，由str根据sep被分割的部分组成
a = 'a,b,c'
print(a.split(','))
print(a.split())
print(a.count("a")) # 返回a字符串中“a”的个数
print(a.replace('a', 'A'))
print('python'.center(20, '*')) # 根据宽度20来居中，空余部分用‘*’代替
print('*-*--*python-*-*+*--*'.strip('*-+')) # 去掉在其左侧和右侧中出现的字符
print(','.join('12345')) # 在’12345‘除最后一个元素外每个字符后增加一个str’,‘

# {0:}引号后分别为填充(单个字符)、对齐(<左>右^居中)、宽度、千位分隔符<,>、精度、类型
print('{0:=^20}'.format('python'))
print('{0:*<20}'.format('python'))
print('{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}'.format(425))
print(chr(425))
print('{0:e},{0:E},{0:f},{0:%}'.format(3.14))
'''
