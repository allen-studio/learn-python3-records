ten_things = "Apple Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ') # 通过split把句子的空格拆成列表
print(stuff) #打印确认已经是列表了
more_stuff = ["Day", "Night", "Song", "Frisbee", 
            "corn", "Banana", "Girl", "Boy"]

while len(stuff)!= 10: # 当 stuff 列表内的元素有10个就停止
    next_one = more_stuff.pop() # more_stuff.pop()从该列表内移除pop最后一个元素，并把该元素赋值给next_one
    print("Adding", next_one)
    stuff.append(next_one) # 给stuff列表增加一个元素next_one,运行结束后统计stuff元素个数，没达到10个重复运行
    print(f"There are {len(stuff)} item now.")

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1]) #打印stuff的第2个元素（列表第一个元素位置是[0])
print(stuff[-1]) #打印stuff的最后一个元素
print(stuff.pop()) # 移除stuff的最后一个元素
print(' '.join(stuff)) # 通过join把stuff合并成句子
print('#'.join(stuff[3:5])) # 合并句子，并打印第四个到第六个之间的元素，并在中间增加 # 号
