x = ['巧克力布丁', '草莓起司蛋糕', '海鮮總匯pizza']

# 轉成字數清單
x_len = list(map(len, x))
# x_len = [i for i in map(len, x)] (清單快寫法)
# x_len = []
# for i in map(len, x):
#     x_len.append(i)
print(x_len) # [5, 6, 9]

num = [1, 2, 3]
print(list(map(lambda i: i * i, num)))
# [1, 4, 9]

num = [1, 2, 3]
print(list(filter(lambda i: i >= 2, num)))
# [2, 3]

# 上面等同於
num = [1, 2, 3]
def f(x):
    if x >= 2:
        return True
    else:
        return False
print(list(filter(f, num)))
# [2, 3]

price = [60, 120, 380, 600]
item = ['巧克力布丁', '草莓起司蛋糕', '海鮮總匯pizza']
x = ['a', 'b', 'c']
print(list(zip(item, price, x)))

# [('巧克力布丁', 60), ('草莓起司蛋糕', 120), ('海鮮總匯pizza', 380)]