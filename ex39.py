a = [1, 2, 3, 4, 5, 6] # 列表是由很多个元素组成的集合，并且该集合后由[]包括起来
print(a)
print(a[1])
b = {'name':'Allen', 'age':100, 'height':"200cm", 'weight':"50kg", 'IQ':100 * 1000} 
# 字典是由多个键值对key:value组成的集合,用{}包括起来，可以通过查询键key而知道value值
print(b['name'])
print(b['IQ'])

# 创建一个省份字典
provinces = {
    '湖南':'湘',
    '湖北':'鄂',
    '广东':'粤',
    '广西':'桂',
    '四川':'川'
}

# 创造一个城市字典
cities = {
    '帝都':'北京',
    '魔都':'上海',
    '妖都':'广州'
    }

#增加一些城市
cities['雾都'] = '重庆'
cities['鸭都'] = '南京'

print('-' * 10)
print('广东省会是：', cities['妖都'])

print('-' * 10)
print('湖南的简称是：', provinces['湖南'])

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f'{abbrev}是{city}的简称')

print('-' * 10)
for province,abbrevs in list(provinces.items()):
    print(f'{province}的简称是{abbrevs}')

print('-' * 10)
province = provinces.get('杭州市')

if not province:
    print('对不起，你查询的省份不存在')

city = cities.get('浙江省', '杭州市')
print(f'浙江省的省会城市是：{city}')




