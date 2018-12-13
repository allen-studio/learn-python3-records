from sys import argv
# read the WYSS section for how to run this
script, first, second, thrid = argv

print("The script called:", script) # varible1 argv 第一个参数就是文件名本身 ex13.py
print("Your first varible is:", first) # varible2 
print("Your second varible is:", second) # varible3  
print("Your thrid varible is:", thrid) # varible4
# 需要在terminals运行python ex13.py varible2 varible3 varible4 传入参数，直接IDE运行会报错 