from sys import argv

script, filename = argv

txt = open(filename) 
# filename 可制定路径 我用的mac 如果读取桌面文件，路径为 /Users/username/Desktop/filename
# 如果读取出来的是乱码，可以open(filename, encoding = "编码格式") 常见编码格式有utf-8,gbk等

# 我在terminal的运行代码如下 
# python3 ex15.py ex14.py 
# 上面命令python3开头是因为mac自带python2.x版本，安装好python3.x版本，需要用python3命令指定运行的python版本


print(f"Here is your file {filename}:")
print(txt.read())#打印刚刚读取的ex14.py文件

print("Type the filename again:")
file_again = input(">") # input输入file_again的文件，我这里是ex13.py，输入了练习13的作业内容

txt_again = open(file_again) #open打开刚输入的file_again的文件，即ex13.py

print(txt_again.read()) # 打印刚刚打开的ex13.py
