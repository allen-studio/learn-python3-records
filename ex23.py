import sys
script, input_encoding, error = sys.argv #argv 输入编码格式、报错方式


def main(language_file, encoding, errors): # 定义main()函数
    line = language_file.readline() # 传入language文件，并读取一行，读取的内容赋值给line
        
    if line: # 如果line有内容就print_line 再 return main()处理，if 如果传入文件到最后没内容了，就没有东西赋值给line了，不再执行print_line()和return main()即停止循环loop
        print_line(line, encoding, errors) # print_line传入三个参数，并调用print_line函数，实际结果参考第18行
        return main(language_file, encoding, errors) # 返回 main（），其实相当于重新从第五行开始运算，形成循环


def print_line(line, encoding, errors): # 定义print_line函数，该函数是main函数第9行分之
    next_lang = line.strip() #strip() 去掉每行字符串的首尾空值，即每行的内容
    raw_bytes = next_lang.encode(encoding, errors = errors) # 编码的每行内容
    cooked_string = raw_bytes.decode(encoding, errors = errors) #解码的每行内容

    print(raw_bytes, "<===>", cooked_string) # main()函数第九行 print_line实际执行结果，打印（左边编码内容 <====> 右边解码内容）


languages = open("languages.txt", encoding = "utf-8") # 指定打开的文件和编码为utf-8,文件默认和ex23.py再同一目录，不然要指定文件路径

main(languages, input_encoding, error)  #调用main函数，传入文件、编码格式、错误处理方式

# ex23的执行逻辑是，首先通过argv指定 编码格式、error，
# 然后执行第23行 main() 函数，main函数按第5行函数定义运行
# main()函数传入第21行的文件，另外两个参数按argv的encoding，error传入
# main()函数读取了 第21行的文本内的第一行内容，执行第8行 if line
# 第8行 if line判断有内容，执行了print_line（），print_line（）运行了第13行的函数定义，打印了第18行结果
# 运行完print_line（），程序继续运行第10行 return main()，这里运行main()相当于又回到第5行产生了循环
# 当第21行language内的文本运行完最后一行后，程序下一个循环传入的内容为空了，通过第8行if line判断内容不存在，程序循环终止