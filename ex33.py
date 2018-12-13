i = 0
numbers = [] # numbers为空列表

while i < 6:  # 当 i < 6,初始i = 0，满足条件，执行第5行print
    print(f"At the top i is {i}")
    numbers.append(i) # 把 i 指写入列表numbers，当i = 0时，nubmers = [0]

    i = i + 1  # i = i + 1,当 i = 1，执行 i = 0 + 1
    print("numbers now: ", numbers)  # 打印第6行numbers，第一轮i = 0，所以numbers = [0]
    print(f"At the botton i is {i}") # ℹ = 0，打印0，第一轮运行结束，因为while函数，直接返回第四行继续，此时因为i = 1，把1代入运行，直至不满足 i < 6


print("The numbers: ")

for num in numbers:  # 当 i = 5,并且while 5 < 6运行结束，此时numbers = [0, 1, 2, 3, 4, 5],通过for···in···遍历
    print(num)  # 然后把从list取出的数值打印出来
