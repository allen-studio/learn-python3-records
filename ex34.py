animals = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
print(animals[0]) #列表第一个元素位置是[0] 
print(animals[-1]) #列表第一个元素位置是[-1]
print(animals[-2]) # 倒数第二个元素就是[-2]
print(animals[5]) # 当然也可以从[0]开始数到第六个[5]
print(animals[0:]) # 获取列表中从 [0] 到结尾的元素
print(animals[:-1]) # 获取列表中从开头 到 [-1]的元素
print(animals[:]) # 获取整个列表的元素
for animal in animals: # 通过for····in····· 遍历列表
    print(animal)  # 打印遍历出来的每一个元素

test = "python is a new programming language with computer, it's written by guido, it's a very simple programming language, i always use it to craiming some infomation in internet."# 这句子乱写的
print(test.split(' ')) # 通过split把句子分词拆成一个列表
print(len(test.split(' '))) # 通过len统计列表里有多少个元素