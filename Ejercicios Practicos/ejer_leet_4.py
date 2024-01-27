s = "IV"
x = 0
print(len(s))
romano_a_numero = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

for i in range(len(s)):
    if i < len(s) - 1 and romano_a_numero[s[i]] < romano_a_numero[s[i + 1]]:
        x -= romano_a_numero[s[i]]
    else:
        x += romano_a_numero[s[i]]

