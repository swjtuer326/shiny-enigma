# seth(angle) 设置行进方向
# setup(width, height, startx, starty) 四个参数后两个可选
# fd()前进 bk()后退
# goto(x,y)
# left()/right()改变绝对方向
# colormode(mode)#有整数模式，小数值模式；默认小数值
# penup() 抬起画笔，不形成图案
# pendown() 落下画笔
# pensize（width) = width(width)
# pencolor(color) color为颜色字符串或r，g，b值
# turtle库详解：https://blog.csdn.net/zengxiantao1994/article/details/76588580/
# circle(r,angle)
# from turtle import*
# import ... as ... 给库定义别名
'''
turtle.setup(800, 400)
turtle.left(45)
turtle.pensize(25)
turtle.pencolor('purple')
turtle.fd(100)
turtle.right(135)
turtle.fd(100)
turtle.bk(100)
turtle.circle(-150, 90)
turtle.done()
for i in range(4):
	print(i)
'''
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor('purple')
turtle.seth(-40)
for i in range(4):
	turtle.circle(40, 80)
	turtle.circle(-40, 80)
turtle.circle(40, 40)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(25)
turtle.done()
