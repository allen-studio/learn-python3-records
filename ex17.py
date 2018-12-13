from sys import argv
from os.path import exists # exists 是一个检测文件是否存在的库，如果不存在报fales，存在报true

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these tow on one line, how?
in_file = open(from_file) #通过open打开一个文件，并且赋值给in_file
indata = in_file.read() #通过in_file.read()读取里面的内容，并且赋值给indata

print(f"The input file is {len(indata)} bytes long") # len函数统计里面有多少字节

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, ctrl-c to abort.") # 按回车继续，按ctrl-c中止操作
input() # 这里的input是一个停顿命令，注释掉也可以运行，但是ctrl-c是终端中止命令，增加这个可以让程序有中止操作的机会

out_file = open(to_file,"w") # 以可写模式“w”打开to_file，并赋值给out_file（输出文件）
out_file.write(indata) # 在out_file通过write写入indta里的数据，indata里的数据来自打开in_file文件，再读取in_file里的内容，并赋值读取的内容给indata

print("Allright, all done")

out_file.close() # 关闭复制的文件
in_file.close() # 关闭来源文件