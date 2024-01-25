nums = [1,2,3,4]

res = 0
fin = []
for i in nums:
    res = i + res
    fin.append(res)

print(fin)