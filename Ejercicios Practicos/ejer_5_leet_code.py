strs= ['ab','a']

res = ""
strs = sorted(strs)
s1 = strs[0]
s2 = strs[-1]
for i in range(len(s1)):
    if s1[i] == s2[i]:
        res += s1[i]
    else:
        break

print(res)