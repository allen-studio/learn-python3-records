formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))# 把四个数字通过.format分别传参到变量formatter的四个花括号里
print(formatter.format("one", "two", "three", "four")) #同上
print(formatter.format(True, False, False, True)) #同上
print(formatter.format(formatter, formatter, formatter, formatter))# #同上，四个花括号里分别传了4个花括号
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
)) # 四个花括号里分别传入了四句字符串