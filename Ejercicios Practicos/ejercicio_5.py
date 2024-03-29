doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
palabra = 'casino'

doc2 = []
res = []
for i in range(len(doc_list)):
    if palabra in doc_list[i].lower():
        res.append(i)
print(res)





