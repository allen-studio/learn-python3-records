print("What's your name?") # 新增问题
name = input() # input()函数是用来传入参数的，简单理解就是输入框，里面内容由你输入或者调用其他函数
print("How old are you?") # end = '' 作用是在打印时传参数不换行，这里换行输入更友好，所以去掉了
age = int(input()) # input()函数可以通过嵌套来指定输入类型，例如int(input())来限制只能输入整数
print("How tall are you?")# end = ''
height = float(input()) # 同上，身高可以嵌套float来实现浮点数输入,运行可以输入整数，但是会以浮点数形式显示，如输入11，会显示为11.0
print("How much do you weight?") 
weight = input()

print(f"So, you're {name}, {age} old, {height} tall and {weight} heavy.") 
# name, age, height 三个函数都是调用上面的定义函数，用了input()函数作为输入
# 如果要做一个app注册，我们可以定义 username，password两个函数，通过input（）函数传参数，然后把传递参数通过sql存储就实现了注册


