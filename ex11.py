
print("How old are you?", end=' ') #end=''告诉print不要用转换副符结束该行，并转到下一行
age = input () #获取输入信息的函数，默认字符串。转换int:y=int(input())
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"so,you are {age} old,{height} tall and {weight} heavy")
