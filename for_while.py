
"""
Python的循环有两种，
一种是for...in循环，依次把list或tuple中的每个元素迭代出来
另一种是while循环,只要条件满足，就不断循环
"""
#for...in循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)


"""
Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。
比如range(5)生成的序列是从0开始小于5的整数
"""
list(range(5))
[0, 1, 2, 3, 4]


sum = 0
for x in range(101):
    sum = sum + x
print(sum)


#while循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#在循环中break,break语句可以提前退出循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')


#continue
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
    #打印的不再是1～10，而是1，3，5，7，9。
