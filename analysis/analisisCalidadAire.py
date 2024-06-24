import pandas as pd
import matplotlib.pyplot as plt

from generators.generadorICA import generarDatosICA

def construirDataIca():
    # Creando un dataFrame
    datosIca=generarDatosICA()
    dataFrameIca=pd.DataFrame(datosIca,columns=["comuna","Ica","fecha","id"])
    dataFrameIca.to_csv("datosIca.csv", index=False)
    print(dataFrameIca)

    datosOrdenadosPorComuna=dataFrameIca.groupby('comuna')['Ica'].mean()
    plt.figure(figsize=(20,20))
    datosOrdenadosPorComuna.plot(kind='bar',color='green')
    plt.show()

construirDataIca()