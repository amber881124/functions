# lambda x: x + 1

# def f(x):
#     retutn x + 1

# 裝在tuple(跟list得差別是不能改值)
items = [
    ('巧克力布丁', 60),
    ('草莓起司蛋糕', 120),
    ('海鮮總匯pizza', 380),
]

# 用價格排序
# key是sorted function的parameter
print(sorted(items, key=lambda x: x[1]))
# result : 
# [('巧克力布丁', 60), 
#  ('草莓起司蛋糕', 120),
#  ('海鮮總匯pizza', 380)]



# 裝在不同字典
i1 = {
    'name' :'巧克力布丁',
    'price' : 60,
}

i2 = {
    'name' :'草莓起司蛋糕',
    'price' : 120,
}

i3 = {
    'name' :'海鮮總匯pizza',
    'price' : 380,
}

items = [i1, i2, i3]

print(sorted(items, key=lambda x: x['price']))
# result : 
# [{'name': '巧克力布丁', 'price': 60}, 
#  {'name': '草莓起司蛋糕', 'price': 120}, 
#  {'name': '海鮮總匯pizza', 'price': 380}]