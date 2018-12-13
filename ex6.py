Types_of_people = 10 #赋值 types_of_people 为 10 
x = f"There are {Types_of_people} types of people."
#赋值 x 为 格式化“there are 调用变量{types_of_people} types of people.“

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said : {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {} "

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."
e = "a string with right side."

print(w+e)

