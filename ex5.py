# ex.py more variables and printing format string (格式化字符) 
my_name = 'Zed A. shaw'
my_age = 35
my_height = 74 #inches
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'Write'
my_hair = 'Brown'

print (f"Let's talk about {my_name}.")
print (f"He's {my_height} inches tall.")
print (f"He's {my_weight} pound heavy.")
print ("Actually that's not to heavy.")
print (f"He's got {my_eyes} eyes and {my_hair}hair.")
print (f"His teeth are usually {my_teeth} depenging on the coffee.")

#this line is trick ,try to get it exactly right.
total = my_age+my_height+my_weight
print (f"if i add {my_age}, {my_eyes}, and {my_weight} I get {total}.")

#改变变量名，去掉前缀“my_”，进行英寸厘米公式转换。
name = 'Zed A. shaw'
age = 35
height = 74 #inches
weight = 180 #pound
eyes = 'Blue'
teeth = 'Write'
hair = 'Brown'
height_cm = height*2.54
weight_kg = weight*0.45
print (f"Let's talk about {name}.")
print (f"He's {height} inches tall.In other words ,{height_cm}cm.")
print (f"He's {weight} pound heavy.In other words ,{weight_kg}kg.")
print ("Actually that's not to heavy.")
print (f"He's got {eyes} eyes and {hair}hair.")
print (f"His teeth are usually {teeth} depenging on the coffee.")

#this line is trick ,try to get it exactly right.
total = age+height+weight
print (f"if i add {age}, {eyes}, and {weight} I get {total}.")
