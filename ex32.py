the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

 # this first kind of for-loop goes through a list
for number in the_count:     # for i in x: 该方法常常也用于爬虫取内容
     print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in i
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = [] # 列表elements为空,为空不代表没有东西ßß

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list")
    elements.append(i) # 列表elements通过append增加内容i

# now we can print them out too
for i in elements:
    print(f"Element was: {i} ")

