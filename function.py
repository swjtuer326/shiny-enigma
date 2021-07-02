def fact(n, m=2):
	s = 1
	for i in range(1, n+1):
		s *= i
	return s/m
print(fact(3,2))
# 可以使用global保留字在函数中使用全局变量
# 局部变量为组合数据类型且未创建，等同于全局变量
ls = ['F', 'f']
def func(a):

	ls.append(a)
	return
func('C')
print(ls)

def fun(a):
	ls = []
	ls.append(a)
	return
fun("A")
print(ls)

# lambda函数
# <函数名> = lambda <参数> : <表达式>
f = lambda x, y: x+y
print(f(10, 15))
