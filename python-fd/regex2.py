import re

f = open('nosql.txt')

# 查找以大写字母开头的单词
pattern = r'[A-Z]\w*'
# 查找数字（负数，小数，分数，百分数等）
pattern1 = r'-?\d+\.?/?\d*%?'

l = []

for line in f:
    l += re.findall(pattern1, line)

print(l)
