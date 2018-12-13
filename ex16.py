from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, hit ctrl-c.") 
print("If you do want that,hit return.")

input("Make your choise")

print("Open the file...")
target = open(filename, "w") # "w"只写模式，write
# r、w、a为打开文件的基本模式，对应着只读、只写、追加模式；read、write、add
# b、t、+、U这四个字符，与以上的文件打开模式组合使用，二进制模式，文本模式，读写模式、通用换行符，根据实际情况组合使用;
# open(file, "wb") 意思是以二进制模式写入
print("Truncating the file.Good bye!")
target.truncate() # truncate 函数是用来删除的

print("Now I'm going to ask you for three lines.")

line1 = input("line1: ") 
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")
target.write(line1) # 写入line1的输入内容到文件里
target.write("\n")  # 写入\n 是 \newline 新起一行的意思，如果没这个代码line1、line2、line3的内容都会写到同一行里
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finally, We close it.")
target.close() # 写入完毕后，通过close()保存和关闭




