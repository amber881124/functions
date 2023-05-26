from collections import abc

x = ['a', 'b', 'c']
e = enumerate(x)
print(isinstance(e, abc.Iterator))


x = ['a', 'b', 'c']

for i, name in enumerate(x):
    print(i, name)
# 0 a
# 1 b
# 2 c

for i in range(len(x)):
    print(i, x[i])
    # 0 a
# 1 b
# 2 c

