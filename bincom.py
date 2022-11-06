# 9. Write a program to sum the first 50 fibonacci sequence.

def fib_Sum(n):
    if (n <= 0):
        return 0

    fib = [0] * (n+1)
    fib[1] = 1

    sum = fib[0] + fib[1]

    for i in range(2, 51):
        fib[i] = fib[i - 1] + fib[ i - 2]
        sum = sum + fib[i]

    return sum

print(fib_Sum(51))

# 8. Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

import random

bin = []
x = 0
while x <= 3:
    bin.append(random.randint(0, 1))
    x += 1
    print(bin)

print(type(bin))

x = str(bin).replace(',',' ')

for line in x:
    if line.strip():
        n = int(line)
    print(n)


# 7.  write a recursive searching algorithm to search for a number entered by user in a list of numbers.

def find_num(array, num):
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if array[mid] < num:
            low = mid + 1

        elif array[mid] > num:
            high = mid - 1

        else: 
            return mid

    return -1


# check
array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num = 10

position = find_num(array, num)

if position != -1:
    print(f'Element is present at index: {position}')

else:
    print('Element is not present in array')

# COLOURS OF THE DAY
import statistics

MONDAY = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
TUESDAY = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLUE', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE',' WHITE', 'BLUE', 'BLUE', 'BLUE']
WEDNESDAY = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED',' ORANGE', 'RED',' BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']
THURSDAY = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
FRIDAY = ['GREEN',' WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE']

# MONDAY
mgreen = MONDAY.count('GREEN'),
myellow = MONDAY.count('YELLOW'),
mbrown = MONDAY.count('BROWN'),
mblue = MONDAY.count('BLUE'),
mpink = MONDAY.count('PINK'),
morange = MONDAY.count('ORANGE'),
mcream = MONDAY.count('CREAM'),
mwhite = MONDAY.count('WHITE'),
mred = MONDAY.count('RED'),
marsh = MONDAY.count('ARSH'),

# TUESDAY
tgreen = TUESDAY.count('GREEN'),
tyellow = TUESDAY.count('YELLOW'),
tbrown = TUESDAY.count('BROWN'),
tblue = TUESDAY.count('BLUE'),
tpink = TUESDAY.count('PINK'),
torange = TUESDAY.count('ORANGE'),
tcream = TUESDAY.count('CREAM'),
twhite = TUESDAY.count('WHITE'),
tred = TUESDAY.count('RED'),
tarsh = TUESDAY.count('ARSH'),

# WEDNESDAY
wgreen = WEDNESDAY.count('GREEN'),
wyellow = WEDNESDAY.count('YELLOW'),
wbrown = WEDNESDAY.count('BROWN'),
wblue = WEDNESDAY.count('BLUE'),
wpink = WEDNESDAY.count('PINK'),
worange = WEDNESDAY.count('ORANGE'),
wcream = WEDNESDAY.count('CREAM'),
wwhite = WEDNESDAY.count('WHITE'),
wred = WEDNESDAY.count('RED'),
warsh = WEDNESDAY.count('ARSH'),

# THURSDAY
thgreen = THURSDAY.count('GREEN'),
thyellow = THURSDAY.count('YELLOW'),
thbrown = THURSDAY.count('BROWN'),
thblue = THURSDAY.count('BLUE'),
thpink = THURSDAY.count('PINK'),
thorange = THURSDAY.count('ORANGE'),
thcream = THURSDAY.count('CREAM'),
thwhite = THURSDAY.count('WHITE'),
thred = THURSDAY.count('RED'),
tharsh = THURSDAY.count('ARSH'),

# FRIDAY
fgreen = FRIDAY.count('GREEN'),
fyellow = FRIDAY.count('YELLOW'),
fbrown = FRIDAY.count('BROWN'),
fblue = FRIDAY.count('BLUE'),
fpink = FRIDAY.count('PINK'),
forange = FRIDAY.count('ORANGE'),
fcream = FRIDAY.count('CREAM'),
fwhite = FRIDAY.count('WHITE'),
fred = FRIDAY.count('RED'),
farsh = FRIDAY.count('ARS')



monday = mgreen,myellow,mbrown,mblue,mpink,morange,mcream,mwhite,mred,marsh
tuesday = tgreen, tyellow, tbrown, tblue, tpink, torange, tcream, twhite, tred, tarsh
wednesday = wgreen, wyellow, wbrown, wblue, wpink, worange, wcream, wwhite, wred, warsh
thursday = thgreen, thyellow, thbrown, thblue, thpink, thorange, thcream, thwhite, thred, tharsh
friday = fgreen, fyellow, fbrown, fblue, fpink, forange, fcream, fwhite, fred, farsh

print(monday)
print(tuesday)
print(wednesday)
print(thursday)
print(friday)

y = (monday, tuesday, wednesday, thursday, friday)

# Question 1
print(statistics.mean(y))

# Question 2
print(statistics.mode(y))

# Question 3
print(statistics.median(y))

# Question 4
print(statistics.variance(y))
