f = open('Iris.txt','w+')
f.writelines('TEnCEnt')
f.write('hello,world!')
print(f.readline())
print(f.readline())
f.close()
f = open('Iris.txt','r')
print(f.readline())
f.close()
with open('Iris.txt') as f:
	p1 = f.read(5)
	p2 = f.read()
	print(p1)
