import math
import time


def euler01():
    sum = 0
    for n in range(1, 1000):
        if (n % 3 == 0) or (n % 5 == 0):
            sum += n
    return sum


def euler02():
    fib1, fib2 = 1, 2
    sum = fib2
    fib = fib1 + fib2
    while fib < 4000000:
        if fib % 2 == 0:
            sum += fib
        fib1 = fib2
        fib2 = fib
        fib = fib1 + fib2
    return sum


def euler03():
    number = 600851475143
    sqrtnumber = math.trunc(math.sqrt(number))
    primefactor = 3
    testfactor = 3
    while testfactor <= sqrtnumber:
        if number % testfactor == 0:
            number /= testfactor
            primefactor = testfactor
        else:
            testfactor += 2
    return primefactor


def euler10():
    return ""


def euler11():
    data = []
    with open("data11.txt") as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    for row in data:
        print(' '.join([str(elem) for elem in row]))
    largest_product = 0
    down = right = diagonal1 = diagonal2 = 0
    print(type(data))
    for i in range(0, 19):
        for j in range(0, 19):
            if i <= 16:
                down = data[i][j] * data[i + 1][j] * data[i + 2][j] * data[i + 3][j]
            if j <= 16:
                right = data[i][j] * data[i][j + 1] * data[i][j + 2] * data[i][j + 3]
            if i <= 16 and j <= 16:
                diagonal1 = data[i][j] * data[i + 1][j + 1] * data[i + 2][j + 2] * data[i + 3][j + 3]
            if i <= 16 and j >= 3:
                diagonal2 = data[i][j] * data[i + 1][j - 1] * data[i + 2][j - 2] * data[i + 3][j - 3]
            largest_product = max(largest_product, down, right, diagonal1, diagonal2)
    return largest_product


def euler12():
    triangle = 1
    num_triangle = 1
    num_int_divider = 1
    while num_int_divider < 500:
        num_triangle += 1
        triangle += num_triangle
        num_int_divider = 2
        for x in range(2, int(triangle ** 0.5)):
            if triangle % x == 0:
                num_int_divider += 2
            if x ** 2 == triangle:
                num_int_divider -= 1
    return triangle

def euler13():
    data = []
    with open('data13.txt') as f:
        for line in f:
            data.append(int(line))
    s = str(sum(data))[0:10]
    return s

def euler14():
    num_max = 0
    number = 0
    for n in range(13, 1000000):
        i = n
        num = 1
        while i != 1:
            i = i // 2 if i % 2 == 0 else 3 * i + 1
            num += 1
        if num_max < num:
            num_max = num
            number = n
    return number

start_time = time.time()
result = euler14()
finish_time = time.time()
print(result)
print("%s seconds" % (finish_time - start_time))
