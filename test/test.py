import itertools

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == 'apple':
        print("apple ==== ")
    print(x)

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]

print(x)
print("=======================")
cars.append("Honda")
for car in cars:
    print(car)


def sum(*args):
    total = 0
    for i in args:
        total += i
    return total


print("=======================")
print(sum(1, 2, 3, 4, 5))


def log(**kwargs):
    for key, value in kwargs.items():
        print('{0} = {1}'.format(key, value))


log(key="key", code="code")

math = lambda a, b: a * b

print(math(10, 5))


def name_decorator(f):
    def wrapper(name):
        s = "Python %s" % name
        return s

    return wrapper


def chuc_danh_decorator(ten_chuc_danh):
    def ten_decorator(f):
        def wrapper(ten):
            chuoi_moi = "Xin gioi thieu %s %s" % (ten_chuc_danh, ten)
            return f(chuoi_moi)

        return wrapper

    return ten_decorator


@chuc_danh_decorator("Giao su")
def gioi_thieu(ten):
    print(ten)


@chuc_danh_decorator("Tien si")
def gioi_thieu_2(ten):
    print(ten)


gioi_thieu("Teo")
gioi_thieu_2("Ti")

# def cubic_generator(n):
# 	for i in range(n):
# 		yield i ** 3

x = iter([1, 2, 3])
print(x)
print(x.__next__())

it1 = iter([1, 2, 3])
it2 = iter([4, 5, 6])
itertools.chain(it1, it2)
mList = list(itertools.chain(it1, it2))
print(mList)


def yrange(n):
    i = 0
    while i < n:
        yield i
    i += 1
    print(i)


yrange(2)


class A:
    message = "class message"

    @classmethod
    def cfoo(cls):
        print(cls.message)

    def foo(self, message):
        self.message = message
        print(self.message)

    def __str__(self):
        return self.message


# from a import A
a = A()
a.foo('instance call')
# a.foo(a)

A.cfoo()


class S:
    nInstances = 0

    def __init__(self):
        S.nInstances = S.nInstances + 1

    @staticmethod
    def howManyInstances():
        print('Number of instances created: ', S.nInstances)


a = S()
b = S()
c = S()
S.howManyInstances()


# class Methods:
#     def i_method(self, x):
#         print(self, x)
#
#     def s_method(x):
#         print(x)
#
#     def c_method(cls, x):
#         print(cls, x)
#
#     s_method = staticmethod(s_method)
#     c_method = classmethod(c_method)
#
#
# obj = Methods()
#
# obj.i_method(1)
# Methods.i_method(obj, 2)
#
# obj.s_method(3)
# Methods.s_method(4)
#
# obj.c_method(5)
# Methods.c_method(6)


class Methods:
    def i_method(self, x):
        print(self, x)

    @staticmethod
    def s_method(x):
        print(x)

    @classmethod
    def c_method(cls, x):
        print(cls, x)


obj = Methods()

obj.i_method(1)
Methods.i_method(obj, 2)

obj.s_method(3)
Methods.s_method(4)

obj.c_method(5)
Methods.c_method(6)


# private ,public atribute

# p.py
class P:
    def __init__(self, name, alias):
        self.name = name  # public
        self.__alias = alias  # private

    def who(self):
        print('name  : ', self.name)
        print('alias : ', self.__alias)


x = P(name='Alex', alias='amen')
print(x.name)
print(x.alias)


# private ,public method

class Q:
    def __init__(self, name, alias):
        self.name = name  # public
        self.__alias = alias  # private

    def who(self):
        print('name  : ', self.name)
        print('alias : ', self.__alias)

    def __foo(self):  # private method
        print('This is private method')

    def foo(self):  # public method
        print('This is public method')
        self.__foo()


x = Q('Alex', 'amem')
# x.__foo() private method dont access
x.foo() # public method
