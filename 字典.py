# 字典类型是映射的体现
# {}  或  dict{}创建
# 键值对：键是数据索引的扩展
# 字典是键值对的集合，键值对之间无序
# del d[k]删除字典d中键k对应的数据值
# k in d 判断键k是否在字典中
# d.keys() 返回字典中所有键的信息
# d.values() 返回字典中所有值的信息
# d.items() 返回字典中所有键值对的信息,以列表形式
# d.popitem() 随机取出一个键值对
d = {'中国':'北京', '美国':'华盛顿', '英国':'伦敦'}
print(d.get('中国'))
print(d.popitem())
# 修改时 d["中国"] = 'beijing'
d["中国"] = 'beijing'
print(d)
print(d.items())
items = list(d.items())
for i in range(2):
	key, value = items[i]
	print(key)
	print(value)
