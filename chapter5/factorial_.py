from collections import Iterator, Generator


def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))
fact = factorial
print(fact)
print(fact(5))
# map返回的结果是一个迭代器，必须要用list()函数把整个序列都计算出来
print(map(factorial, range(11)), isinstance(map(factorial, range(11)), Iterator),
      isinstance(map(factorial, range(11)), Generator))
print(list(map(factorial, range(11))))
