import csv

with open("archivos csv\\datos.csv") as archivo:
    #print(csv.reader(archivo))
    reader = csv.reader(archivo)
    print(reader)
    for row in reader:
        print(row)