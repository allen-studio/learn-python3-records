def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man, that's enough for party!")
    print("Get a blanket.\n")
# 定义函数cheese_and_crackers，该函数传入2个参数chesse_count和boxes_of_crackers，然后定义打印

print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30) # 函数传入20，30两个整数参数


print("OR, we can use varibles from our script:")
amount_of_cheese = 10
amount_of_crackers = 50  

cheese_and_crackers(amount_of_cheese, amount_of_crackers) 
# 函数cheese_and crackers 传入两个变量

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
# 函数cheese_and crackers 传入两个计算的整数
print("And we can combine the two, varibles and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) 
# 函数cheese_and crackers 传入 变量+整数


