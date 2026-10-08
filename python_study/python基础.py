#print()函数语法格式：
from tomlkit import value
#

print(value, ..., sep=' ', end='\n', file=None, flush=False)#输出函数
print(1,2,3,4)#1 2 3 4 默认为分隔符
print(1,2,3,4,sep='-＞')# 分隔符改为了箭头

print(1,2,3)#代表换行
print(1,2,3)

print(1,2,3,4,end='\t')#默认换行符改为了空,相当于tab键
print(1,2,3,4)

# 打开名为“报错.txt”的文件，以追加模式("a")打开   w为写入 会覆盖原文本
# 如果文件不存在，会自动创建
f = open("报错.txt","a")
print("hello world",file=f) # 将字符串“hello world”写入文件中，使用print函数，并指定输出目标为文件f
f.close() # 关闭文件，确保所有写入的内容保存到文件中

# 使用 with 语句打开文件“报错.txt”，以追加模式("a")打开
# with 语句可以确保文件在操作完成后自动关闭，避免手动关闭
with open('报错.txt', 'a') as f:
    print("hello world", file=f)  # 文件会在with语句结束时自动关闭



#input输入函数
name = input("请输入您的姓名：")
print(f"您好，{name}！")

#格式化输出

#含义
#给定一个模板，按照模板输出内容。

#格式符号
#格式化输出使用 % 和不同的字符连用，不同类型的数据需要使用不同的格式化字符。

#常用格式化字符及其含义
#%c：字符
#%s：字符串
#%d：十进制整数
#%f：浮点数

#基本格式化输出：使用％
print("姓名是%s,年龄：%d" % ("小胡", 25))

#format()格式化输出
print("姓名：{}，年龄：{}".format("小胡", 25))

#f表达式格式化输出
name = "小胡"
age = 25
print(f"姓名：{name}，年龄：{age}")


## 变量

# 变量是将数据在内存中存储后给定的一个名称，这个名称就是变量。
# 变量名是没有类型的，类型只存在于对象中，变量只是引用对象。
# Python 为动态解释型语言，在赋值操作时，类型是在运行过程中自动决定的。

#对象

# 对象是有类型的。
# 对象是分配的一块内存空间，用来表示它的值。
# Python 对象的三要素：
#     * id：对象的唯一标识符。
#     * type：对象的类型。
#     * value：对象的值.

a=1
print(1)

import keyword
print(keyword.kwlist) #打印python关键字
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


#变量的命名

#变量名只能由数字、字母和_(下划线) 组成。
#变量名不能以数字开头。
#变量名不能是 Python 关键字。
#变量名是区分大小写的。


#input()函数的使用

#input() 是 Python 中用于从用户获取输入的函数。它会在控制台显示提示信息，并等待用户输入。
#用户输入的内容会以字符串形式返回。
user_input = input("请输入一些内容: ")
print("你输入的内容是:", user_input)