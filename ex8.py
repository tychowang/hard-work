#ex8.py printing，pringing
formatter="{} {} {} {}" #格式化 程序 字符串，

print(formatter.format(1,2,3,4)) #调用format函数，执行format的命令行
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
