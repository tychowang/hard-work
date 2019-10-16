#ex14.py prompting and passing
from sys import argv

script,user_name = argv,argv
prompt = '>' #让prompt代替>,以便后续代码引用。

print(f"Hi {user_name},I'm the (script)script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}? ")
likes = input(prompt)  #将命令行写入的命令存在like字符中。

print(f"where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alrighut,so you said {likes} about linking me.
you live in {lives}. Not sure where that is.
And you have a {computer} computer.NIce.
""")
