# format( )方法，将字符串格式化，将字符串统一成一种格式
str1 = "{0} love {1}"  # 这里{0}、{1}是个占位符，然后将format中元素填入该位置
# 两种方式
# 普通方式
print("{0} love {1}".format('哈哈', '嘻嘻'))
print("{0} love {1}".format('啊呜', '琪琪'))
print(str1.format('哈哈', '嘻嘻'))
print(str1.format('啊呜', '琪琪'))
# format中使用元组作为参数
couple1 = ('哈哈', '嘻嘻')
couple2 = ('啊呜', '琪琪')
print(str1.format(*couple1))
print(str1.format(*couple2))

# 当然也可以不用{0},{1}...来占位,也可以用{a}、{b}...或其他带{ }东西来占位，只是要加东西,且只有一种表示方法
str2 = "{a} love {b}"
print("{a} love {b}".format(a='哈哈', b='嘻嘻'))
print("{a} love {b}".format(a='啊呜', b='琪琪'))

# 还可以混合使用{0},{1}...和{a}、{b}...来占位，只是{0}、{1}...必须放在最前面，后面的可以随意用
print("{0} love {a}".format('哈哈', a='嘻嘻'))
# print("{a} love {0}".format(a='啊呜', '琪琪'))  # 这种会报错，{0}放在其他种占位符后面是不行的

# 如果想打印出{}，就要再占位符在加一个{ }，之前我们是加一个 \ 转义，但这里不是
print("{{0}} love {{1}}".format(('啊呜', '琪琪')))
# 这里输出的结果是：{0} love {1}，使占位符没有效果了
# format方法中要打印单个大括号
print("{{".format(''))
print("{{".format(''))
# 所以最终调整为
print("{{{0}}} love {{{1}}}".format('啊呜', '琪琪'))  # 为了更清晰我们分开来"{{ {0} }} love {{ {1} }}"， {{ 和 }}用于打印 { 和 } ，故占位符仍有效果
# 打印结果：{啊呜} love {琪琪}

# 打印浮点数和整数
print("{0:.2f} and {1}".format(27.658, 123))  # 数字不用加引号
# {0:.2f}其中0是表示占的位置，python中 : 冒号代表格式化符号的开始，后面接的是python的格式化符号，.2表示小数点后要2位，多出来的会四舍五入，f表示的是浮点数
# 打印结果：27.658 and 123

print('%d + %d = %d' % (4, 5, 4+5))
print('%5.1f' % 27.658)
print('%10d' % 5)
print('%+10d' % 5)