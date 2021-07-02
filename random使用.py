from random import random
from time import perf_counter
DARTS = 10000*10000
hits = 0.0
start = perf_counter()
for i in range(DARTS):
	x, y = random(), random()
	dist = pow(x**2+y**2, 0.5)
	if dist < 1.0:
		hits += 1
pi = 4*hits/DARTS
print('圆周率是:{:.6f}'.format(pi))
print('运行时间:{:.3f}'.format(perf_counter()-start))
