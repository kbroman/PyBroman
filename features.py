#!/usr/local/bin/python

# various by python (v3.3) stuff while I learn the langugage
# (taking my features.rb script and porting it to python)

# Really useful to me:
#   google course on python:     https://developers.google.com/edu/python/
#   software carpentry bootcamp: http://software-carpentry.org/v4/python/index.html

# loops
for x in range(1, 10):
  print(x, end="")
print()

for x in range(9, 4, -1):
  print(x, end="")
print()

for x in range(0, 21, 5):
  print(x, end=" ")
print()

# string methods
print('Length of "This is a test"', end="")
print(len('This is a test'))

print('This is a test'.lower())

print('This is a test'.upper())

print('This is a test'.swapcase())

# reverse ("extended slice syntax": begin:end:step)
print("This is a test"[::-1])

# string manipulation & reg ex
import re
# sub just the first
print(re.sub('bar', 'foo', 'foobarfoobar', count=1))

# global sub
print(re.sub('bar','foo','foobarfoobar'))

print(re.sub(r'\s+', '|', "This is a test", count=1))

print(re.sub(r'\s+', '|', 'This is a test'))

text = '<h3 align="center">Popularity in 1990</h3>\n'
year = re.search(r'Popularity in (\d\d\d\d)', text).group(1)
print(year)

text = '<tr align="right"><td>7</td><td>Andrew</td><td>Stephanie</td>'
rank_and_names = re.search(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
print(rank_and_names.group())
print(rank_and_names.group(1))
print(rank_and_names.group(2))
print(rank_and_names.group(3))

rank_and_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)
print(rank_and_names)

text2 = '''<tr align="right"><td>7</td><td>Andrew</td><td>Stephanie</td>
<tr align="right"><td>8</td><td>James</td><td>Jennifer</td>
<tr align="right"><td>9</td><td>Justin</td><td>Elizabeth</td>'''
rank_and_names = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text2)
print(rank_and_names)


# split on whitespace
print("Blah blah blah. ".split())

# arrays (lists)
arr = [1, "test", 2, 3, 4]
for x in arr:
  print(str(x) + "X ", end="")
print()

# formated print
for x in arr:
  print("%sX " % x, end="")
print()

# map
x = list(map(lambda x:x+1, range(6)))
print(x)

# list comprehension
x = [y+1 for y in range(6)]
print(x)

y = list(map(lambda x:x+2, range(6)))
print(' '.join(map(str, y)))

# ranges
x = list(range(6))
y = list(range(1, 7))
z = list(range(3, 50, 5))
print(x, y, z)

# loops
for i in range(1,6):
  print("%d^2 = %d" % (i, i**2))

i = 1
while i <= 5:
  print("%d^2 = %d" % (i, i**2))
  i += 1

# other array methods
x = list(range(1,6))
y = [2, 4, 1]
print(x+y)
print(":".join(map(str, x+y)))

# aliasing
x = list(range(1,6))
y = [2, 4, 1]
z = x # aliased
zz = list(x) # a copy
id(x) == id(z)  # True
id(x) != id(zz) # True
for yy in y:
  if yy in x: x.remove(yy)
print(x, z, zz)

print(3 in x)
print(7 in x)
print(x[0]) # first element
print(x[-1]) # last element

z = range(5, 9)
print(z[-2:]) # a range
z = list(z)
print(z[-2:]) # now a list
zz = z.reverse() # doesn't return
print(z, zz) # zz = None
zz = reversed(z)
print(zz) # an iterator
zz = list(reversed(z))
print(zz) # a list

# hashes (hash is called a 'dict')
x = {"a" : 1, "b" : 2, "c" : 3}
print(x['a'])
for (value,key) in enumerate(x):
  print(key, ' -> ', value)
print(list(x.keys()))
x.pop("a")
print(x)

x = {"a" : 1, "b" : 2, "c" : 3}
z = list(x.keys())  # need list() since I'll be modifying the keys in place
for key in z: # "for key in x:" would work if I weren't modifying the keys in place
  if x[key] == 2:
    x.pop(key)
print(x)

# alternatively:
x = {"a" : 1, "b" : 2, "c" : 3}
z = [key for key in x.keys() if x[key] == 2]
for key in z:
  x.pop(key)
print(x)

x = {"a":1, "b":2}
x['d'] = x['d']+1 if 'd' in x else 1


## slices of arrays, negative index to start from end
a = list(range(2, 13, 2))
print(a[1:3])
print(a[-1])
print(a[-3:-2])
print(a[-3])
print(a[-3:-1])

## conversion between classes
int("5")        # to integer
float("6")      # to float
str(252.3)      # to string

## a bit of text manipulation
text = '''We may at once admit that any inference from the particular
to the general must be attended with some degree of uncertainty,
but this is not the same as to admit that such inference cannot
be absolutely rigorous, for the nature and degree of the uncertainty
may itself be capable of rigorous expression.'''
stopwords = 'the a by on for of are with just but and to my in I has some'.lower().split()
words = text.lower().split()
keywords = [word for word in words if word not in stopwords]
print(' '.join(keywords))
print("no. char  =", len(' '.join(keywords)))
print("no. words =", len(keywords))

## playing with map
n = 8
counts = map(lambda x: 0, range(n))
print(' '.join(map(str, counts)))
import random
x = map(lambda z: random.randint(1,8), range(1000))
counts = []
for i in range(1,9):
  counts.append( sum(z==i for z in y) )
print(' '.join(map(str, counts)))

## looping over hashes (also sorting)
words = '''We may at once admit that any inference from the particular to the general
must be attended with some degree of uncertainty, but this is not the same as to
admit that such inference cannot be absolutely rigorous, for the nature and
degree of the uncertainty may itself be capable of rigorous expression.'''.split()
import re
words = list(map(lambda word: re.sub(r'[,\.]', '', word), words))
wordcount = {}
for word in words:
  wordcount[word] = wordcount[word]+1 if word in wordcount else 1

# sort by word length
sorted(wordcount.keys(), key=len)

# sort by count
sorted(wordcount.keys(), key=lambda x: wordcount[x])

# by count then word length
sorted(wordcount.keys(), key=lambda x: [wordcount[x], len(x)])

# by word length then count
sorted(wordcount.keys(), key=lambda x: [len(x), wordcount[x]])

# by count then word length, but reversed
sorted(wordcount.keys(), key=lambda x: [wordcount[x], len(x)], reverse=True)

# using a function
def count_and_length (a):
  return [wordcount[a], len(a)]
sorted(wordcount.keys(), key=count_and_length)

## regex
import re
if not re.search(r'AM', 'am'):
  print('ok 1')
if re.search(r'(?i)AM', 'am'):
  print('ok 2')
if re.search(r'AM', 'am', re.IGNORECASE):
  print('ok 3')
multi = 'blah a number of special\nAll of these are'
if re.search(r'\Ablah', multi):
  print('ok 4')
if not re.search(r'\AAll', multi):
  print('ok 5')
if re.search(r'^blah', multi):
  print('ok 6')
if not re.search(r'^All', multi):
  print('ok 7')
if re.search(r'^A', multi, re.MULTILINE):
  print('ok 8')
if not re.search(r'special\Z', multi):
  print('ok 9')
if re.search(r'special$', multi, re.MULTILINE):
  print('ok 10')
if re.search(r'are\Z', multi, re.MULTILINE):
  print('ok 11')
if re.search(r'are\Z', multi):
  print('ok 12')
if not re.search(r'special$', multi):
  print('ok 13')
if re.search(r'special$', multi, re.MULTILINE):
  print('ok 14')
if re.search(r'are$', multi):
  print('ok 15')
if not re.search(r'blah.*are', multi):
  print('ok 16')
if re.search(r'blah.*are', multi, re.DOTALL):
  print('ok 17')
x = 'Today is 11/26/2013, while tomorrow is 11/27/2013.'
z = re.search(r'(\d+)/(\d+)/(\d+)', x)
if z:
  print('Month = %s, day = %s, year = %s' % (z.group(1), z.group(2), z.group(3)))
zz = re.findall(r'(\d+)/(\d+)/(\d+)', x)
if zz:
  print('Month = %s, day = %s, year = %s' % (zz[0][0], zz[0][1], zz[0][2]))
if len(zz) > 1:
  print('Month = %s, day = %s, year = %s' % (zz[1][0], zz[1][1], zz[1][2]))

