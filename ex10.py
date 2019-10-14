#ex10.py  what was that? 在'或者"前加入\，代表特殊字符'"
# print（I am 6'2\" tall."） 和 print（'I am 6\'2" tall.'） 都是输出I am 6'2"tall
tabby_cat = "\tI'm tabbed in." #空出四个空格长度
persian_cat = "I'm split\non a line."
backslash_cat = "I'm\\a\\cat." #\\代表一个\

fat_cat = """
I will do a list:
\t* Cat food 
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
