import csv
import re

filename = r'E:\CAPGEMINI\regex_sum_1335687.txt'
f = open(filename)
d = f.read()
y = re.findall('[0-9]+', d)
sum = 0
for i in range(len(y)):
    c = int(y[i])
    sum += c

print(sum)
