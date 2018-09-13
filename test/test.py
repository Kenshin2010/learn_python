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


a = A()
a.foo('instance call')