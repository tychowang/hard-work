# ex6.py string and text
type_of_people = 10
x = f"There are {type_of_people} type of people. "

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said:{x}")
print(f"I also said:'{y}'")

hilarioius = False
joke_evaluation = "Isn't that joke so funny?!{}"

print(joke_evaluation.format(hilarioius))  

w = "This is the lift side of ..."
e = "a string with a right side ."

print(w+e)
