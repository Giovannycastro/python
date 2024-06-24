import random

def generarDatosRuido():
    encuestaRuido=[]
    for i in range(2000):
        dato={}
        id=random.randint(1,50000)
        nivelRuido=random.randint(10,90)
        comuna=random.choice(["comuna 1","comuna 2","comuna 3","comuna 4","comuna 5","comuna 6","comuna 7","comuna 8","comuna 9","comuna 10","comuna 11","comuna 12","comuna 13","comuna 14","comuna 15","comuna 16"])
        dato=[id,nivelRuido,comuna]
        encuestaRuido.append(dato)
        print(encuestaRuido)

generarDatosRuido()
        


