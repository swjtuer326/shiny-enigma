# 元组和列表属于序列

# 相当于广义数组
# 和字符串数组操作类似
ls = ['python', 123]
print(ls[::-1])
print(len(ls))
# min()
# max() 可比较时才有意义
# s.index(x) 或 s.index(x,i,j)返回序列s第一次出现元素x的位置
# s.count(x) 返回序列s中x出现的次数


# 元组是序列类型的扩展，一旦创建就不能被修改
# 类似于一个大容炉
creature = 'cat', 'dog', 'tiger'
print(creature)
color = creature, ls
print(color)
a = (123, creature)
print(a)
print(a[1])

l = [1,2,3,4,5,6,7,8,9]
lt = [11,10,9,8,7,6,5,4,3,2,1,0]
l[0:4:2] = lt[1:3]
print(l)
del l[1:3:1]
print(l)
print(l)
del l[::3]
print(l)
# ls.append(x) 在列表后增加一个元素x
# ls.clear()  删除列表ls所有元素
# ls.copy()  生成一个新列表，赋值ls中所有元素
# ls.insert(i,x) 在列表的第i位置添加一个元素x
# ls.pop(i) 取出并删除第i位置元素
# ls.remove(x)将列表中出现的第一个元素x删除
# ls.reverse()将列表中元素反转
l[0:2] = []
print(l)
