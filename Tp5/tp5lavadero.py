import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

EXPERIMENTOS = 30
CORRIDAS = 100

A = {
    'low' : 1,
    'high': 5
}
B = {
    'low' : 1,
    'high': 3
}
C = {
    'low' : 1,
    'high': 3
}
D = {
    'low' : 3,
    'high': 6
}
E = {
    'low' : 2,
    'high': 5
}
F = {
    'low' : 4,
    'high': 8
}
G = {
    'low' : 3,
    'high': 7
}

AS = [A,B,C]
AM = [D,E]
AI = [F,G]

def calcularAcceso(listaAcceso):
    time = 0
    for tarea in listaAcceso:
        time += np.random.uniform(tarea['low'], tarea['high'])
    return time

def calcularProyecto(acs,acm,aci):
    tas = calcularAcceso(acs)
    tam = calcularAcceso(acm)
    tai = calcularAcceso(aci)
    tiempoProyecto = max(tas, tam, tai)
    if tiempoProyecto == tas:
        accesoCritico = 'AS'
    elif tiempoProyecto == tam:
        accesoCritico = 'AM'
    elif tiempoProyecto == tai:
        accesoCritico = 'AI'

    return tiempoProyecto, accesoCritico


def main():
    tiempoPromedioExperimento = []
    tiempos = []
    criticidad ={
        'AS':0,
        'AM':0,
        'AI':0
    }

    for i in range(EXPERIMENTOS):
        tiempo = 0
        for j in range(CORRIDAS):
            auxTiempo,acceso = calcularProyecto(AS,AM,AI)
            tiempo += auxTiempo
            tiempos.append(auxTiempo)
            criticidad[acceso] += 1

        tiempoPromedioExperimento.append(tiempo/CORRIDAS)
    print('Tiempo promedio de finalizacion del proyecto',np.mean(tiempoPromedioExperimento),'minutos')
    intervaloSup, intervaloInf = st.t.interval (0.99, len (tiempoPromedioExperimento) -1,np.mean (tiempoPromedioExperimento),st.sem (tiempoPromedioExperimento))
    print('Con un intervalo de confianfa entre',intervaloSup,'y', intervaloInf)

    print('Criticidad acceso superior',(criticidad['AS']/3000)*100,'%')
    print('Criticidad acceso medio',(criticidad['AM']/3000)*100,'%')
    print('Criticidad acceso inferior',(criticidad['AI']/3000)*100,'%')

    fig, axs = plt.subplots(nrows=2)

    axs[0].hist(tiempos, alpha=0.7,color="green", edgecolor="black")
    axs[0].set_xlabel("Tiempos de finalizacion (minutos)")   
    axs[0].set_ylabel("Frecuencia")
    axs[0].set_title("Distribucion de los tiempos de las 3000 corridas")

    axs[1].hist(tiempoPromedioExperimento, alpha=0.7,color="yellow", edgecolor="black")
    axs[1].set_xlabel("Tiempos de finalizacion (minutos)")
    axs[1].set_ylabel("Frecuencia")
    axs[1].set_title("Distribucion de los tiempos promedios de los 30 experimentos")
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
