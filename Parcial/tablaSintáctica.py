import csv

from terminalesNoTerminales import producciones
from terminalesNoTerminales import noTerminales
from terminalesNoTerminales import terminales
from primerosSiguientes import primeros
from primerosSiguientes import siguientes

def parsearTable(producciones, noTerminales, terminales, primeros, siguientes):
    tablaAnalisis = {noT: {t: '' for t in terminales + ['$']} for noT in noTerminales}
    i = 0
    while i < len(producciones):
        seccion = producciones[i].split('->')
        if len(seccion) == 2:
            lhs = seccion[0].strip()
            rhs_seccion = seccion[1].strip().split()

            if rhs_seccion[0] == "''":
                for follow in siguientes[lhs]:
                    tablaAnalisis[lhs][follow] = 'ε'
            else:
                first_symbol = rhs_seccion[0]
                if first_symbol in noTerminales:
                    for first in primeros[first_symbol]:
                        if first != 'ε':
                            tablaAnalisis[lhs][first] = ' '.join(rhs_seccion)
                        else:
                            for follow in siguientes[lhs]:
                                tablaAnalisis[lhs][follow] = 'ε'
                elif first_symbol in terminales:
                    tablaAnalisis[lhs][first_symbol] = ' '.join(rhs_seccion)
        i += 1
    return tablaAnalisis

def generarTablaCSV(noTerminales, terminales, primeros, siguientes, tablaAnalisis):
    with open('Tabla Sintáctica.csv', 'w', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        encabezado = ['FIRST', 'FOLLOW', 'Nonterminal'] + terminales + ['$']
        escritor.writerow(encabezado)
        indice = 0
        while indice < len(noTerminales):
            nt_actual = noTerminales[indice]
            fila = [
                ", ".join(primeros.get(nt_actual, [])),
                ", ".join(siguientes.get(nt_actual, [])),
                nt_actual
            ]
            indice_terminal = 0
            terminales_totales = terminales + ['$']
            while indice_terminal < len(terminales_totales):
                terminal_actual = terminales_totales[indice_terminal]
                fila.append(tablaAnalisis[nt_actual].get(terminal_actual, ''))
                indice_terminal += 1

            escritor.writerow(fila)
            indice += 1
    return "Tabla sintáctica generada en CSV"

tablaParseada = parsearTable(producciones, noTerminales, terminales, primeros, siguientes)
tablaCSV = generarTablaCSV(noTerminales, terminales, primeros, siguientes, tablaParseada)