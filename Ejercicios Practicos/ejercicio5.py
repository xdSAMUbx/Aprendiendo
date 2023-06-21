#serie de fibonacci hasta el numero que queremos
def fibonnacci (num):
    serie = [0,1]
    for i in range (num):
        i = serie[-1] + serie[-2]
        serie.append(i)
    return serie
        
resultado = fibonnacci(121)
print (resultado)
    