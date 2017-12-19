messageFormat = '尊敬的{0}，恭喜您的手机{1}现已获得一个{2}抽奖机会，请速度来取！'
message = messageFormat.format('袁雯琦','13060011817','iPhone X')
print(message)
b = 'I\n\'m OK'
print(b)
b = 'Hello,%s'%'world'
print(b)
c = "Hi, %s, you have a iphone%d" %("xudong",10)
print(c)

a = 72
b = 85
c = (b-a)/a*100
print("小明成绩提高了%.2f%%"%c)

#开始学习条件判断
age = 2
if age >=18:
    print("you're age is",age)
    print("adult")
elif age >= 6:
    print("you're age is",age)
    print("teenager")
else:
    print("you're age is",age)
    print("kid")

#if还可以简写
if 2:
    print(True)

#再议input. 运行时，它会拦住，所以暂时关掉
# s = input("birth:")
# birth = int(s)
# if birth < 2000:
#     print("00前")
# else:
#     print("00后")

#练习
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
a = 1.75
b = 80.5
c = b/(a*a)
if c < 18.5:
    print("BMI指数=","%.2f"%c,",","过轻")
elif 18.5<=c<25:
    print("BMI指数=","%.2f"%c,",","正常")
elif 25<=c<28:
    print("BMI指数=","%.2f"%c,",","过重")
elif 28<=c<32:
    print("BMI指数=","%.2f"%c,",","肥胖")
else:
    print("BMI指数=","%.2f"%c,",","严重肥胖")

#循环
#1.
a = ['Michael',"Bart","Tracy"]
for b in a:
    print(b)
#2 计算1-10的整数和
sum = 0
list =[]
for x in range(101):
    list.append(x)
print(list)
for x in list:
    sum = sum + x
print(sum)

sum = 0
for x in range(10):
    sum = sum + x
print(sum)

#while循环
#计算100以内所有奇数之和
sum = 0
n = 1
while n <=100:
    sum = sum + n
    n = n + 2
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#请利用循环依次对list中的每个名字打印出Hello, xxx!
L = ["Michael","Bart","Tracy"]
for x in L:
    print("Hello,",x + "!")
Llen = len(L)
y = 0
while y < Llen:
    print(L[y])
    y = y + 1

#break哈哈哈
#循环打印1-10的数字
n=1
while n <= 10:
    print(n)
    n=n+1
print("END")

#打印1-9
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

#continue
#打印1-10中的奇数
n = 1
while n<=10:
    print(n)
    n=n+2

n = 0
while n < 10:
    n = n + 1
    if n%2 == 0:
        continue
    print(n)


n = 0
while n < 10:
    n=n+1
    if n%2 != 0:
        print(n)


#dic（字典）和set,dic最实用啦！dic的key必须是不可变的！！！所以可以是字符串或整数，不可以是list
#dictionary
d = {"Mic":95,"Bart":80,"Jack":74}
print(d["Mic"])
#用in判断是否存在
d = {"Mic":95,"Bart":80,"Jack":74}
print("Rose" in d)
#get
d = {"Mic":95,"Bart":80,"Jack":74}
print(d.get("Micc", None))
#Pop删除
d = {"Mic": 95, "Bart": 80, "Jack": 74}
d.pop("Mic")
print(d)
# 如果是list
# 记得打空格！
# “Mic”就是key!!!

# set是指一个无序的、无重复元素的集合:要创建一个set，需要一个list作为输入集合
s = set([1,2,3])
print(s) # 结果是{ }括号，意思是告诉你set内部有1，2,3这3个元素，显示了顺序，但不代表set有序
# 重复元素被set自动过滤
s = set([1,2,2,2,3,4,5,3])
print(s)
# 加入一个元素,add;删除一个元素，remove
s = set([1,2,3])
s.add(4)
print(s)
s.remove(4)
print(s)

# 不可变对象，str不可变，list可变
s = ["b", "a", "c"]
s.sort()
print(s)

s = "a,b,c"
s.replace("a","A")
print(s) # 无法打印A，因为字符串不能被改变




# 第二章 函数
# 调用函数的公式： http://docs.python.org/3/library/functions.html#abs；也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
# 求绝对值：abs
a = abs(-20)
print(a)
# 求最大值
a = max(1,2,-3,5,40)
print(a)

# 数据类型转换
a = int("123")
print(a)
a = int(12.34)
print(a)
a = bool("1.286739740")
print(a)

# 把n1 n2转换成十六进制的字符串
n1 = 255
n2 = 1000
a = hex(n1)
b = hex(n2)
print(a,b)

# 定义函数
x = -99
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(x))

# 空函数，用pass
x = -8
if x < 0:
    pass
print(x)

# 参数检查，用内置函数isinstance实现
x = 9
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(x))

# 返回多个值
import math
def move(x, y, step, angel=0):
    nx = x + step*math.cos(angel)
    ny = y + step*math.sin(angel)
    return nx, ny

# 计算平方根
import math
math.sqrt(2)
print(math.sqrt(2))


# 举例:请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0 的两个解。
# import math
# def quadratic(a,b,c):
# 0 = ax2 + bx + c
# 不会做一元二次方程！！！

# 函数的参数
def power(x):
    return x * x
print(power(5)) # 5的平方
# x的立方
def power(x):
    return x * x * x
print(power(2))
# 另一种方法
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2, 4))

# 设定参数的默认值
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2))

# 一年级小学生注册的函数
def enroll(name, gender):
    print("name:", name)
    print("gander:", gender)
print(enroll("Jack", "male"))

# 把年龄和城市设为默认参数
def enroll(name, gender, age=6, city="Beijing"):
    print("name:", name)
    print("gender", gender)
    print("age:", age)
    print("city:", city)
print(enroll("Jack", "Female"))

# 可变参数

#XuDong_2017年12月19日


#xiaoqi
345
123


