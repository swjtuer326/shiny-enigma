from numpy import *
# from scipy import linalg
# from scipy import integrate
from pylab import *

'''
import timeit
def fun(x,y):
	return x**2+y**3
t_start = timeit.default_timer()
z = fun(109.2,367.1)
t_end = timeit.default_timer()
cost = t_end - t_start
print('Time cost of fun is %f' %cost)
'''
# a = np.arange(0,20,1)
# print(a)
# print(np.dot(a,np.transpose(a)))
# print(np.dot(np.transpose(a),a))
# print(np.transpose(a))
# print(np.dot(a,a))
# print(np.sin(a+1)/np.exp(a)*((a+1)/2))
# a=a.reshape([2,10])
# print(np.sin(a+1)/np.exp(a)*((a+1)/2))
# print(np.shape(a))
'''
A = np.random.randn(5,5)
b = np.random.randn(5)
x = linalg.solve(A,b)
print(x)
print(linalg.eig(A))
def fun(x):
	return np.log(x)
value, error = integrate.quad(fun,0,1)
print(value,error)
'''
x = linspace(0, 5, 10)
y = x ** 2

figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()


a=[1]

if list(range(10)) in a:
	print('aaa'+str(a))
print(list(range(10)))
print(a)
