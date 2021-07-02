A = {'p', 'y', 123}
B = set('pypy123')
print(A-B)
print(A&B)
print(B-A)
print(A|B)
print(A^B)
A.add('x')
print(A)
A.discard('x')
print(A)
A.remove('y')
print(A)
A.pop()
print(A)
A.clear()
print(A)
print(len(A))
print('x' not in A)
for i in B:
	print(i, end=' ')
try:
	print('\n')
	while True:
		print(B.pop(), end=' ')
except:
	pass
ls = ['p', 'p', 'y', 'y', 123]
s = set(ls)
print(list(s))
