import re

pattern = r'(ab)cd(ef)'

s = 'abcdefghigklmnabcdef'

l = re.findall(pattern, s)

print(l)


regex = re.compile(pattern)

l = regex.findall(s, 0, 10)

# ss = regex.search(s).gourp()

# print('ss : ', ss)

# print(l.pos)
# print(l.endpos)

print(l)


l = re.split(r'\s+', "hello world nihao ,china")
print(l)


s = re.sub(r"\s+", "#", "hello world nihao china", 2)
print("sub(): ", s)

it = re.finditer(r'\d+', '2008-2018 10years')


for i in it:
    print(i.group())


# fullmatch
try:
    obj = re.fullmatch(r'\w+', 'abceef123#')
    print(obj.group())
except AttributeError as e:
    print(e)

# obj = re.match(r'foo', 'Foo,food on the table')

# print(obj.group())
