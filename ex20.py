from sys import argv

script, input_file = argv

def print_all(f): # f是一个变量，等待传入参数文件，
    print(f.read()) # 打印 读取的传入文件内容

def rewind(f): # 定义函数倒带，因为f已经在上面被打印了，如果没有倒带函数，下面打印每行无法执行
    f.seek(0) # seek()从第几个字符开始，如果更改数字1，就会从第二个字符开始显示第一行

def print_a_line(line_count, f): # 定义函数打印一行信息的函数，传入两个参数（打印第几行，传入文件）
    print(line_count, f.readline()) # 打印两个信息（行数，行数对应的内容）

current_file = open(input_file) # argv传入一个input_file，通过open打开，并赋值到current_file

print("First let's print the whole file:\n")

print_all(current_file) # 打印current_file的所有内容，current_file来自open(argv传入的input_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three line:")

current_line = 1 # 指定行数的数字起始值
print_a_line(current_line, current_file) # 行数1，打印行数1的内容

current_line = current_line + 1   # 行数1+1，打印行数1+1的内容
print_a_line(current_line, current_file)

current_line = current_line + 1   # 接着上面的结果运行，（行数1+1）+1，打印（行数1+1）+1的内容
print_a_line(current_line, current_file)



