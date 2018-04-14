import re

file = open("sampleData.txt")
sum =0
for line in file:
    for no in re.findall('([0-9]+)',line):
        sum = sum + int(no) 

print(sum)