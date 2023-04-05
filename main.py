import csv

puntuaciones_gp = {
    'carrera_pos1'          : 25,
    'carrera_pos2'          : 18,
    'carrera_pos3'          : 15,
    'carrera_podio'         : 4,
    'clasificacion_pos1'    : 12,
    'clasificacion_pos2'    : 9,
    'clasificacion_pos3'    : 7,
    'clasificacion_podio'   : 2
}

porristas = { # que no porreros ni mamporreros
    'jos'   :   'Jose L.',
    'mar'   :   'Maria',
    'naz'   :   'Nazaret',
    'pab'   :   'Pablo',
    'ric'   :   'Ricardo',
    'ser'   :   'Sergio',
} 

circuitos = [
    'Bahrein',
    'Jeddah',
    'Melbourne',
    'Baku',
    'Miami',
    'Imola',
    'Monaco',
    'Barcelona',
    'Montreal',
    'Austria',
    'Silverstone',
    'Hungary',
    'Spa',
    'Netherlands',
    'Monza',
    'Singapore',
    'Suzuka',
    'Qatar',
    'Austin',
    'Mexico',
    'Interlagos',
    'Las Vegas',
    'Yas Marina'
]

# funciones auxiliares
def numero_valores_interseccion(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return len(lst3)

# programa principal
if __name__ == '__main__':

    porras = {}
    print("\nLeyendo archivos de porras...")
    for porrista in porristas:
        print("\tCargando porra de", porristas[porrista], '...', end=' ')
        with open('resultados/porra_'+porrista+'.csv', newline='') as f:
            reader = csv.reader(f)
            porras[porrista] = list(reader)
        print("\tOK.")

    print("\nLeyendo archivo de resultados...", end=' ')
    with open('resultados/resultados.csv', newline='') as f:
        reader = csv.reader(f)
        resultados = list(reader)
    print("\tOK.")

    print("\nCalculando puntuaciones...")
    puntuaciones = {
        'jos'   :   0,
        'mar'   :   0,
        'naz'   :   0,
        'pab'   :   0,
        'ric'   :   0,
        'ser'   :   0,
    }
    
    for porrista, porra in porras.items():
        print("\tCalculado puntuaciones de", porristas[porrista], '...')
        for index, resultado_gp in enumerate(resultados):
            print("\t-> GP de", circuitos[index], ":", end=' ')
            # CLASIFICACION
            # primero clasificacion
            print("(clasificacion)", end=' ')
            if resultado_gp[0]==porra[index][0] and not resultado_gp[0]=='XXX':
                puntuaciones[porrista] += puntuaciones_gp['clasificacion_pos1']
                print("+", puntuaciones_gp['clasificacion_pos1'], "pts", end=' ')
            # segundo clasificacion
            if resultado_gp[1]==porra[index][1] and not resultado_gp[1]=='XXX':
                puntuaciones[porrista] += puntuaciones_gp['clasificacion_pos2']
                print("+", puntuaciones_gp['clasificacion_pos2'], "pts", end=' ')
            # tercero clasificacion
            if resultado_gp[2]==porra[index][2] and not resultado_gp[2]=='XXX':
                puntuaciones[porrista] += puntuaciones_gp['clasificacion_pos3']
                print("+", puntuaciones_gp['clasificacion_pos3'], "pts", end=' ')
            # en podio de clasificacion
            puntuacion_podio = puntuaciones_gp['clasificacion_podio'] * numero_valores_interseccion(resultado_gp[0:3],porra[index][0:3])
            if puntuacion_podio > 0: 
                puntuaciones[porrista] += puntuacion_podio
                print("+", puntuacion_podio, "pts", end=' ')

            # CARRERA AL SPRINT
            if resultado_gp[3] != 'XXX': # hay carrera al sprint
                print("(sprint)", end=' ')
                # primero carrera sprint
                if resultado_gp[3]==porra[index][3] and not resultado_gp[3]=='XXX':
                    puntuaciones[porrista] += puntuaciones_gp['clasificacion_pos1']
                    print("+", puntuaciones_gp['clasificacion_pos1'], "pts", end=' ')
                # segundo carrera sprint
                if resultado_gp[4]==porra[index][4] and not resultado_gp[4]=='XXX':
                    puntuaciones[porrista] += puntuaciones_gp['clasificacion_pos2']
                    print("+", puntuaciones_gp['clasificacion_pos2'], "pts", end=' ')
                # tercero carrera sprint
                if resultado_gp[5]==porra[index][5] and not resultado_gp[5]=='XXX':
                    puntuaciones[porrista] += puntuaciones_gp['clasificacion_pos3']
                    print("+", puntuaciones_gp['clasificacion_pos3'], "pts", end=' ')
                # en podio de carrera sprint
                puntuacion_podio = puntuaciones_gp['clasificacion_podio'] * numero_valores_interseccion(resultado_gp[3:6],porra[index][3:6])
                if puntuacion_podio > 0: 
                    puntuaciones[porrista] += puntuacion_podio
                    print("+", puntuacion_podio, "pts", end=' ')

            # CARRERA
            print("(carrera)", end=' ')
            # primero carrera
            if resultado_gp[6]==porra[index][6] and not resultado_gp[6]=='XXX':
                puntuaciones[porrista] += puntuaciones_gp['carrera_pos1']
                print("+", puntuaciones_gp['carrera_pos1'], "pts", end=' ')
            # segundo carrera
            if resultado_gp[7]==porra[index][7] and not resultado_gp[7]=='XXX':
                puntuaciones[porrista] += puntuaciones_gp['carrera_pos2']
                print("+", puntuaciones_gp['carrera_pos2'], "pts", end=' ')
            # tercero carrera
            if resultado_gp[8]==porra[index][8] and not resultado_gp[8]=='XXX':
                puntuaciones[porrista] += puntuaciones_gp['carrera_pos3']
                print("+", puntuaciones_gp['carrera_pos3'], "pts", end=' ')
            # en podio de carrera
            puntuacion_podio = puntuaciones_gp['carrera_podio'] * numero_valores_interseccion(resultado_gp[6:9],porra[index][6:9])
            if puntuacion_podio > 0: 
                puntuaciones[porrista] += puntuacion_podio
                print("+", puntuacion_podio, "pts", end=' ')

            print()

    print("\n-- RESUMEN DE PUNTUACIONES --")
    for porrista in porristas:
        print("-", porristas[porrista], "\t\t\t:", puntuaciones[porrista], "pts")
    print("-----------------------------")