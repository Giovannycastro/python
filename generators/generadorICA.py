import random

def generarDatosICA():
    datosEncuesta=[]
    for i in range(2000):
        dato={}
        comuna=random.choice(["comuna 1","comuna 2","comuna 3","comuna 4","comuna 5","comuna 6","comuna 7","comuna 8","comuna 9","comuna 10","comuna 11","comuna 12","comuna 13","comuna 14","comuna 15","comuna 16"])
        ica=random.randint(10,100)
        fecha=random.choice(["2024-06-23","2024-06-25","2024-01-30","2024-07-31"])
        id=random.randint(1,50000)
        dato=[comuna,ica,fecha,id]
        datosEncuesta.append(dato)
    return (datosEncuesta)
    

generarDatosICA()             
